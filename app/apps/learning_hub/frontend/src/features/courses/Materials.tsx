import { useCallback, useRef, useState, type ChangeEvent, type DragEvent } from 'react';
import type { HubClient, UploadReceipt } from '../../api/client';
import { useHubQuery } from '../../app/query';
import { EmptyState, ErrorState, PageHeading, PendingState } from '../../app/ui';

type FileEntry = { id: string; requestKey: string; file: File; courseKey: string; weekId: string } & (
  { state: 'staged' | 'saving' } | { state: 'failed'; error: string } | { state: 'saved'; receipt: UploadReceipt }
);
/** Unsent file bytes stay in memory across internal navigation, never in learner evidence. */
export function useMaterialsDraft() {
  const [courseKey, setCourseKey] = useState('');
  const [weekId, setWeekId] = useState('');
  const [files, setFiles] = useState<FileEntry[]>([]);
  const [notice, setNotice] = useState('');
  const savingRef = useRef(false);
  return { courseKey, setCourseKey, weekId, setWeekId, files, setFiles, notice, setNotice, savingRef };
}
export function Materials({ client, draft }: { client: HubClient; draft: ReturnType<typeof useMaterialsDraft> }) {
  const { courseKey, setCourseKey, weekId, setWeekId, files, setFiles, notice, setNotice, savingRef } = draft;
  const picker = useRef<HTMLInputElement>(null);
  const read = useCallback((signal: AbortSignal) => client.courses(signal), [client]);
  const courses = useHubQuery('courses:current-publication', read);
  const readWeeks = useCallback((signal: AbortSignal) => courseKey ? client.weeks(courseKey, signal) : Promise.resolve([]), [client, courseKey]);
  const weeks = useHubQuery(`upload-weeks:${courseKey}`, readWeeks);
  const selected = courses.state.kind === 'ready' ? courses.state.data.find(c => c.course_key === courseKey) : undefined;
  const validWeek = weeks.state.kind === 'ready' && weeks.state.data.some(w => w.week_ref.id === weekId);
  const busy = files.some(f => f.state === 'saving');
  function stage(list: FileList | null) {
    if (!selected || !validWeek) { setNotice('Choose a course and an available week before selecting files.'); return; }
    const incoming = Array.from(list ?? []);
    if (!incoming.length) return;
    const outstanding = files.filter(f => f.state !== 'saved');
    if (outstanding.length + incoming.length > 20 || [...outstanding.map(f => f.file), ...incoming].reduce((n, f) => n + f.size, 0) > 500 * 1024 * 1024 || incoming.some(f => f.size > 100 * 1024 * 1024 || f.size === 0)) {
      setNotice('Choose up to 20 nonempty files, at most 100 MiB each and 500 MiB in total.'); return;
    }
    setFiles(previous => [...previous, ...incoming.map(file => ({ id: crypto.randomUUID(), requestKey: crypto.randomUUID(), file, courseKey, weekId, state: 'staged' as const }))]);
    setNotice('Files selected locally. Save them to send their bytes to the local service.');
  }
  function pick(event: ChangeEvent<HTMLInputElement>) { stage(event.target.files); event.target.value = ''; }
  function drop(event: DragEvent<HTMLDivElement>) { event.preventDefault(); if (!busy) stage(event.dataTransfer.files); }
  async function save() {
    if (savingRef.current) return;
    savingRef.current = true;
    try {
      for (const entry of files.filter(f => f.state === 'staged' || f.state === 'failed')) {
        setFiles(previous => previous.map(f => f.id === entry.id ? { ...entry, state: 'saving' } : f));
        try {
          const receipt = await client.upload(entry.courseKey, entry.weekId, entry.file, entry.requestKey);
          setFiles(previous => previous.map(f => f.id === entry.id ? { ...entry, state: 'saved', receipt } : f));
        } catch (error) {
          setFiles(previous => previous.map(f => f.id === entry.id ? { ...entry, state: 'failed', error: error instanceof Error ? error.message : 'Saving failed. Try again.' } : f));
        }
      }
    } finally { savingRef.current = false; }
  }
  const unfinished = files.some(f => f.state === 'staged' || f.state === 'failed');
  return <><PageHeading eyebrow="Course materials" title="A home for your source materials">Choose the course and week, then save your files. Checked lessons are published after preparation and review.</PageHeading>
    {courses.state.kind === 'pending' ? <PendingState /> : courses.state.kind === 'error' ? <ErrorState message={courses.state.message} retry={courses.retry} />
      : courses.state.data.length === 0 ? <EmptyState title="Choose a course after inventory is available">There are no courses to attach materials to yet. Reload after the local course inventory is configured.</EmptyState>
        : <section className="panel"><div className="field-grid"><div className="field"><label htmlFor="upload-course">Course</label>
          <select id="upload-course" value={courseKey} disabled={busy} onChange={e => { setCourseKey(e.target.value); setWeekId(''); }}><option value="">Choose a course</option>{courses.state.data.map(c => <option key={c.course_key} value={c.course_key}>{c.display_name} · {c.identity.academic_year} · {c.identity.semester} · {c.identity.course_folder}</option>)}</select></div>
          <div className="field"><label htmlFor="upload-week">Week</label><select id="upload-week" value={weekId} disabled={!courseKey || weeks.state.kind !== 'ready' || busy} onChange={e => setWeekId(e.target.value)}><option value="">Choose a week</option>{weeks.state.kind === 'ready' && weeks.state.data.map(w => <option key={w.week_ref.id} value={w.week_ref.id}>{w.week_ref.id} · revision {w.week_ref.revision}</option>)}</select></div></div>
          {courseKey && (weeks.state.kind === 'pending' ? <p role="status">Loading available weeks…</p> : weeks.state.kind === 'error' ? <ErrorState message={weeks.state.message} retry={weeks.retry} /> : !weeks.state.data.length ? <p>No week targets available. The course service must supply a week before files can be saved.</p> : null)}
          <div className="dropzone" onDragOver={event => event.preventDefault()} onDrop={drop}><span className="state-symbol" aria-hidden="true">↑</span><h2>Drop your files here</h2><p>PDFs, slides, documents, or other course sources.<br />The service checks their actual media type.</p><button className="button primary" disabled={!selected || !validWeek || busy} onClick={() => picker.current?.click()}>Choose files</button><input className="visually-hidden" ref={picker} type="file" multiple aria-label="Course source files" tabIndex={-1} onChange={pick} /></div>
          <p className="muted">Up to 20 files · 100 MiB per file · 500 MiB per selection. Existing source revisions are preserved.</p>
          <p role="status">{notice}</p>
        </section>}
    {files.length > 0 && <section className="panel upload-results"><div className="section-heading"><h2>Your selection</h2><button className="button primary" disabled={busy || !unfinished} onClick={() => void save()}>{busy ? 'Saving…' : 'Save selected files'}</button></div>
      <ul className="file-list">{files.map(entry => <li key={entry.id}><div><strong>{entry.file.name}</strong><p>{entry.weekId} · {(entry.file.size / 1024).toFixed(1)} KiB</p>
        {entry.state === 'failed' && <p role="alert" className="error-text">{entry.error} Retry uses the same request identity.</p>}
        {entry.state === 'saved' && <><p>Durable receipt: {entry.receipt.receipt.receipt_id}</p><p>Extraction: {entry.receipt.sources.map(s => s.extraction_state).join(', ') || 'Unknown'}. Ingestion checks and publication: unknown.</p>
          {entry.receipt.sources.length > 0 && <details><summary>Source revisions</summary><ul>{entry.receipt.sources.map(source => <li key={source.source_revision_id}>{source.source_revision_id} · revision {source.revision}</li>)}</ul></details>}
          {entry.receipt.duplicate_source_revision_ids.length > 0 && <p>Duplicate source revisions retained: {entry.receipt.duplicate_source_revision_ids.join(', ')}</p>}</>}
      </div><span className={`badge ${entry.state === 'failed' ? 'attention' : 'neutral'}`}>{entry.state === 'staged' ? 'Selected locally' : entry.state === 'saving' ? 'Saving bytes…' : entry.state === 'failed' ? 'Save failed' : 'Saved · publication pending'}</span></li>)}</ul>
      <p className="muted">A storage receipt does not certify ingestion, independent checks, or publication. Check the course catalogue for published availability.</p>
    </section>}
  </>;
}
