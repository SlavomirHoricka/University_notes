import { describe, expect, it, vi } from 'vitest';
import { createHubClient } from '../src/api/client';
import { testCourse, testUpload } from './h04.fixtures';
const signal = () => new AbortController().signal;
const response = (value: unknown, status = 200) => new Response(JSON.stringify(value), { status, headers: { 'Content-Type': 'application/json' } });
describe('typed production HTTP boundary', () => {
  it('rejects invalid catalogue data instead of reporting readiness', async () => {
    const client = createHubClient(vi.fn().mockResolvedValue(response([{ ...testCourse, readiness: 'approved' }])));
    await expect(client.courses(signal())).rejects.toThrow('unsupported data');
  });
  it.each([401, 403, 404, 409, 500, 501])('surfaces HTTP %s without fixture fallback', async status => {
    const client = createHubClient(vi.fn().mockResolvedValue(response({}, status)));
    await expect(client.courses(signal())).rejects.toMatchObject({ status });
  });
  it('keeps empty catalogue and missing route distinct', async () => {
    const client = createHubClient(vi.fn().mockResolvedValue(response([])));
    await expect(client.courses(signal())).resolves.toEqual([]);
  });
  it('preserves CSRF, idempotency, opaque identity, and original multipart bytes', async () => {
    const fetcher = vi.fn().mockResolvedValue(response(testUpload, 202));
    const client = createHubClient(fetcher, 'local_test_csrf');
    const file = new File(['original'], 'original.pdf');
    await expect(client.upload(testCourse.course_key, 'week_opaque_1', file, 'request_A')).resolves.toEqual(testUpload);
    const init = fetcher.mock.calls[0]?.[1] as RequestInit;
    expect(init.headers).toEqual({ 'Idempotency-Key': 'request_A', 'X-CSRF-Token': 'local_test_csrf' });
    expect(init.body).toBeInstanceOf(FormData);
    expect((init.body as FormData).get('week_id')).toBe('week_opaque_1');
    expect((init.body as FormData).get('files')).toBe(file);
    expect(init.credentials).toBe('same-origin');
  });
  it('requires a local session and never sends unauthorized upload bytes', async () => {
    const fetcher = vi.fn();
    await expect(createHubClient(fetcher).upload('crs_opaque_A', 'week_A', new File(['data'], 'data.pdf'), 'key')).rejects.toThrow('launcher');
    expect(fetcher).not.toHaveBeenCalled();
  });
  it('rejects an upload receipt for a different selected course/week', async () => {
    const client = createHubClient(vi.fn().mockResolvedValue(response(testUpload, 202)), 'csrf');
    await expect(client.upload(testCourse.course_key, 'wrong_week', new File(['data'], 'data.pdf'), 'key')).rejects.toThrow('unsupported data');
  });
});
