import type { ReactNode } from 'react';
import type { Course, Progress } from '../api/client';

export function PageHeading({ eyebrow, title, children }: { eyebrow: string; title: string; children?: ReactNode }) {
  return <header className="page-heading"><p className="eyebrow">{eyebrow}</p><h1 tabIndex={-1}>{title}</h1>{children && <p className="lede">{children}</p>}</header>;
}
export function EmptyState({ title, children }: { title: string; children: ReactNode }) {
  return <section className="state-panel"><span className="state-symbol" aria-hidden="true">◇</span><h2>{title}</h2><p>{children}</p></section>;
}
export function PendingState({ children = 'Loading checked course data…' }: { children?: ReactNode }) {
  return <div className="state-panel" role="status"><span className="loading-dot" aria-hidden="true" /><p>{children}</p></div>;
}
export function ErrorState({ message, retry }: { message: string; retry: () => void }) {
  return <section className="state-panel error-panel" role="alert"><h2>Unable to load this view</h2><p>{message}</p><button className="button secondary" onClick={retry}>Try again</button></section>;
}
const readinessLabels: Record<Course['readiness'], string> = {
  ready: 'Published · checked', partial: 'Partial coverage', stale: 'Publication stale', blocked: 'Preparation blocked', unavailable: 'Not published',
};
export function ReadinessBadge({ value }: { value: Course['readiness'] }) {
  return <span className={`badge readiness-${value}`}>{readinessLabels[value]}</span>;
}
export function AttentionBadge({ value }: { value: Progress['needs_attention'] }) {
  return <span className={`badge ${value ? 'attention' : 'neutral'}`}>{value === null ? 'Attention unknown' : value ? 'Needs attention' : 'No attention flagged'}</span>;
}
/** Process facts never turn into acquisition or retention claims. */
export function ProcessProgress({ progress }: { progress: Progress | null }) {
  if (!progress) return <div className="process-facts"><p>Instruction: <strong>Unknown</strong></p><p>Assessment: <strong>Unknown</strong></p><AttentionBadge value={null} /></div>;
  const verified = progress.canonical_commit_state === 'verified' && progress.evidence_state === 'current';
  const instruction = { not_started: 'Not started', in_progress: 'In progress', finished: 'Finished' }[progress.instruction_state];
  const assessment = progress.assessment_grading_state === 'pending' ? 'Grading pending'
    : progress.assessment_grading_state === 'unscorable' ? 'Unscorable'
      : progress.assessment_grading_state === 'finalized' ? 'Graded'
        : { not_started: 'Not started', in_progress: 'In progress', submitted: 'Submitted' }[progress.assessment_submission_state];
  return <div className="process-facts"><p>Instruction: <strong>{verified ? instruction : 'Evidence pending or unknown'}</strong></p>
    <p>Assessment: <strong>{assessment}</strong></p>
    <p>Process: <strong>{verified ? progress.completed ? 'Completed' : 'Outstanding activity' : 'Unverified'}</strong></p>
    <p>Pass: <strong>{verified && progress.passed !== null ? progress.passed ? 'Passed' : 'Not passed' : 'Unknown'}</strong></p>
    {!verified && <p className="muted">Evidence: {progress.evidence_state.replaceAll('_', ' ')} · {progress.canonical_commit_state}</p>}
    <AttentionBadge value={verified ? progress.needs_attention : null} /></div>;
}
