import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../src/app/App';
import { testClient, testCourse, testUpload } from './h04.fixtures';
import type { HubClient } from '../src/api/client';

beforeEach(() => { window.history.replaceState(null, '', '/materials'); vi.stubGlobal('scrollTo', vi.fn()); });
async function chooseTarget() {
  const course = await screen.findByLabelText('Course');
  fireEvent.change(course, { target: { value: testCourse.course_key } });
  await screen.findByRole('option', { name: /week_opaque_1/ });
  fireEvent.change(screen.getByLabelText('Week'), { target: { value: 'week_opaque_1' } });
}
function selectFile(name = 'fixture.pdf') {
  fireEvent.change(screen.getByLabelText('Course source files'), { target: { files: [new File(['%PDF-1'], name, { type: 'application/pdf' })] } });
}
describe('H04-A4 per-file upload boundary', () => {
  it('requires server course/week identity before choosing files', async () => {
    render(<App client={testClient()} />);
    expect(await screen.findByRole('button', { name: 'Choose files' })).toBeDisabled();
    await chooseTarget();
    expect(screen.getByRole('button', { name: 'Choose files' })).toBeEnabled();
  });
  it('distinguishes local staging, saving, and durable saved bytes from publication', async () => {
    let resolve!: (value: typeof testUpload) => void;
    const upload = vi.fn<HubClient['upload']>(() => new Promise(r => { resolve = r; }));
    render(<App client={testClient({ upload })} />);
    await chooseTarget(); selectFile();
    expect(screen.getByText('Selected locally')).toBeVisible();
    expect(upload).not.toHaveBeenCalled();
    fireEvent.click(screen.getByRole('button', { name: 'Save selected files' }));
    expect(screen.getByText('Saving bytes…')).toBeVisible();
    expect(screen.getByRole('button', { name: 'Saving…' })).toBeDisabled();
    resolve(testUpload);
    expect(await screen.findByText('Saved · publication pending')).toBeVisible();
    expect(screen.getByText(/Ingestion checks and publication: unknown/)).toBeVisible();
    expect(upload.mock.calls[0]?.slice(0, 2)).toEqual([testCourse.course_key, 'week_opaque_1']);
  });
  it('retries transport failure with identical bytes/request key and retains staged files across navigation', async () => {
    const upload = vi.fn().mockRejectedValueOnce(new Error('disconnected')).mockResolvedValue(testUpload);
    render(<App client={testClient({ upload })} />);
    await chooseTarget(); selectFile();
    fireEvent.click(screen.getByRole('link', { name: 'Overview' }));
    expect(window.location.pathname).toBe('/');
    fireEvent.click(screen.getByRole('link', { name: 'Materials' }));
    expect(screen.getByText('fixture.pdf')).toBeVisible();
    fireEvent.click(screen.getByRole('button', { name: 'Save selected files' }));
    expect(await screen.findByText('Save failed')).toBeVisible();
    fireEvent.click(screen.getByRole('button', { name: 'Save selected files' }));
    expect(await screen.findByText('Saved · publication pending')).toBeVisible();
    expect(upload.mock.calls[1]).toEqual(upload.mock.calls[0]);
  });
  it('retains original selected target after changing course/week', async () => {
    const client = testClient();
    render(<App client={client} />);
    await chooseTarget(); selectFile();
    fireEvent.change(screen.getByLabelText('Week'), { target: { value: 'week_opaque_2' } });
    fireEvent.click(screen.getByRole('button', { name: 'Save selected files' }));
    await waitFor(() => expect(client.upload).toHaveBeenCalled());
    expect(vi.mocked(client.upload).mock.calls[0]?.[1]).toBe('week_opaque_1');
  });
  it('supports drag/drop with the same local-selection boundary', async () => {
    const client = testClient();
    render(<App client={client} />);
    await chooseTarget();
    fireEvent.drop(screen.getByText('Drop your files here').parentElement!, { dataTransfer: { files: [new File(['source'], 'drag.pdf')] } });
    expect(screen.getByText('drag.pdf')).toBeVisible();
    expect(client.upload).not.toHaveBeenCalled();
  });
  it('explains empty week targets and preserves duplicate source revisions', async () => {
    render(<App client={testClient({ upload: vi.fn().mockResolvedValue({ ...testUpload, duplicate_source_revision_ids: ['prior_revision'] }) })} />);
    await chooseTarget(); selectFile(); fireEvent.click(screen.getByRole('button', { name: 'Save selected files' }));
    expect(await screen.findByText('Duplicate source revisions retained: prior_revision')).toBeVisible();
  });
});
