import type { components } from '../generated/schema';

type Schema = components['schemas'];
export type Course = Schema['CourseCatalogueV1'];
export type Week = Schema['WeekSummaryV1'];
export type Progress = Schema['LessonProgressV1'];
export type Provider = Schema['ProviderStatusV1'];
export type UploadReceipt = Schema['UploadReceiptV1'];
export type Health = Schema['HealthResponse'];

export class HubError extends Error {
  constructor(message: string, readonly status?: number) { super(message); }
}

export interface HubClient {
  courses(signal: AbortSignal): Promise<Course[]>;
  weeks(courseKey: string, signal: AbortSignal): Promise<Week[]>;
  health(signal: AbortSignal): Promise<Health>;
  provider(signal: AbortSignal): Promise<Provider>;
  upload(courseKey: string, weekId: string, file: File, requestKey: string): Promise<UploadReceipt>;
}

const record = (v: unknown): v is Record<string, unknown> => typeof v === 'object' && v !== null;
const strings = (v: unknown): v is string[] => Array.isArray(v) && v.every(x => typeof x === 'string');
const opaqueCourseKey = (v: unknown) => typeof v === 'string' && /^crs_[A-Za-z0-9_-]{8,64}$/.test(v);
const ref = (v: unknown) => record(v) && typeof v.id === 'string' && v.id.length > 0 && v.id.length <= 500
  && v.id !== '.' && v.id !== '..' && typeof v.revision === 'number' && Number.isSafeInteger(v.revision) && v.revision >= 1;
const readiness = (v: unknown) => ['ready', 'partial', 'stale', 'blocked', 'unavailable'].includes(String(v));
const integer = (v: unknown) => typeof v === 'number' && Number.isSafeInteger(v) && v >= 0;
const isoTime = (v: unknown) => typeof v === 'string' && Number.isFinite(Date.parse(v));
function bundle(v: unknown) {
  return record(v) && typeof v.bundle_id === 'string' && v.bundle_schema_version === 1
    && typeof v.course_id === 'string' && integer(v.ingestion_revision) && typeof v.plan_version === 'string'
    && typeof v.source_version === 'string' && typeof v.public_digest === 'string' && typeof v.private_digest === 'string';
}
function course(v: unknown): v is Course {
  if (!record(v) || !record(v.identity)) return false;
  return opaqueCourseKey(v.course_key) && typeof v.display_name === 'string'
    && typeof v.identity.course_id === 'string' && typeof v.identity.course_folder === 'string'
    && typeof v.identity.academic_year === 'string'
    && ['Winter_Semester', 'Summer_Semester'].includes(String(v.identity.semester))
    && (v.identity.course_code === null || typeof v.identity.course_code === 'string')
    && strings(v.available_scope) && strings(v.blocked_scope) && readiness(v.readiness)
    && (v.bundle_ref === null || (bundle(v.bundle_ref) && record(v.bundle_ref) && v.bundle_ref.course_id === v.identity.course_id));
}
function progress(v: unknown): v is Progress {
  return record(v) && ['not_started', 'in_progress', 'finished'].includes(String(v.instruction_state))
    && ['not_started', 'in_progress', 'submitted'].includes(String(v.assessment_submission_state))
    && ['absent', 'pending', 'finalized', 'unscorable'].includes(String(v.assessment_grading_state))
    && ['pending', 'verified', 'conflict', 'unknown'].includes(String(v.canonical_commit_state))
    && ['current', 'stale', 'reassessment_needed', 'unknown'].includes(String(v.evidence_state))
    && typeof v.completed === 'boolean' && (v.passed === null || typeof v.passed === 'boolean')
    && (v.needs_attention === null || typeof v.needs_attention === 'boolean');
}
function week(v: unknown): v is Week {
  return record(v) && typeof v.course_key === 'string' && ref(v.week_ref) && readiness(v.readiness)
    && Array.isArray(v.lessons) && v.lessons.every(ref) && (v.progress === null || progress(v.progress));
}
function provider(v: unknown): v is Provider {
  return record(v) && typeof v.signed_in === 'boolean' && typeof v.inference_verified === 'boolean'
    && Number.isInteger(v.account_revision)
    && ['verified', 'unverified', 'denied', 'missing_grant', 'unknown'].includes(String(v.eligibility))
    && (v.usage === null || (record(v.usage) && isoTime(v.usage.measured_at) && typeof v.usage.scope === 'string'
      && (v.usage.reset_at === null || isoTime(v.usage.reset_at))
      && (v.usage.used_percent === null || (typeof v.usage.used_percent === 'number' && Number.isFinite(v.usage.used_percent)
        && v.usage.used_percent >= 0 && v.usage.used_percent <= 100))));
}
function health(v: unknown): v is Health {
  return record(v) && v.schema_version === 1 && v.service === 'learning-hub'
    && v.status === 'ok' && v.ready === false && v.reason === 'scaffold_only';
}
function upload(v: unknown): v is UploadReceipt {
  return record(v) && typeof v.course_key === 'string' && record(v.receipt)
    && v.receipt.kind === 'upload' && v.receipt.durable_receipt === true
    && typeof v.receipt.receipt_id === 'string' && typeof v.receipt.command_id === 'string'
    && integer(v.receipt.aggregate_revision) && isoTime(v.receipt.received_at)
    && ['received', 'pending', 'completed', 'blocked'].includes(String(v.receipt.processing_state))
    && strings(v.duplicate_source_revision_ids)
    && Array.isArray(v.sources) && v.sources.every(s => record(s)
      && typeof s.source_revision_id === 'string' && typeof s.course_key === 'string'
      && typeof s.source_id === 'string' && integer(s.revision) && typeof s.sha256 === 'string'
      && integer(s.byte_size) && typeof s.media_type === 'string' && typeof s.managed_relpath === 'string'
      && ref(s.week_ref) && ['pending', 'complete', 'partial', 'blocked'].includes(String(s.extraction_state)));
}

/** One transport boundary. No fixture fallback and no optimistic mutation success. */
export function createHubClient(fetcher: typeof fetch = (...args) => fetch(...args), csrfToken?: string): HubClient {
  async function request<T>(path: string, validate: (v: unknown) => v is T, init: RequestInit = {}): Promise<T> {
    let response: Response;
    try { response = await fetcher(`/api/v1${path}`, { credentials: 'same-origin', ...init }); }
    catch (error) {
      if (error instanceof DOMException && error.name === 'AbortError') throw error;
      throw new HubError('Cannot reach the local service. Start the hub, then try again.');
    }
    if (!response.ok) {
      const message = response.status === 401 || response.status === 403
        ? 'Open the hub from its local launcher to restore your session.'
        : response.status === 404 || response.status === 501
          ? 'This service feature is not available yet.'
          : response.status === 409 ? 'The source changed. Refresh before trying again.'
            : 'The local service could not finish this request. Try again.';
      throw new HubError(message, response.status);
    }
    let value: unknown;
    try { value = await response.json(); } catch { throw new HubError('The service returned an unreadable response.'); }
    if (!validate(value)) throw new HubError('The service returned unsupported data. Refresh after updating the hub.');
    return value;
  }
  return {
    courses: signal => request('/courses', (v): v is Course[] => Array.isArray(v) && v.every(course), { signal }),
    weeks: (key, signal) => opaqueCourseKey(key) ? request(`/courses/${encodeURIComponent(key)}/weeks`,
      (v): v is Week[] => Array.isArray(v) && v.every(week) && v.every(w => w.course_key === key), { signal })
      : Promise.reject(new HubError('This course route has an unsupported identifier. Open it from Courses.')),
    health: signal => request('/health', health, { signal }),
    provider: signal => request('/provider/status', provider, { signal }),
    async upload(key, weekId, file, requestKey) {
      if (!opaqueCourseKey(key)) throw new HubError('This course route has an unsupported identifier. Open it from Courses.');
      // H03 supplies the local-session contract. Until it is present, missing authorization is explicit.
      if (!csrfToken) throw new HubError('Open the hub from its local launcher to enable saving materials.');
      const body = new FormData();
      body.set('week_id', weekId);
      body.append('files', file);
      return request(`/courses/${encodeURIComponent(key)}/uploads`,
        (v): v is UploadReceipt => upload(v) && v.course_key === key
          && v.sources.every(s => s.course_key === key && s.week_ref.id === weekId),
        { method: 'POST', headers: { 'Idempotency-Key': requestKey, 'X-CSRF-Token': csrfToken }, body });
    },
  };
}
