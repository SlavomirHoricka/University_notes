import { vi } from 'vitest';
import type { Course, Health, HubClient, Progress, Provider, UploadReceipt, Week } from '../src/api/client';

// Fictional fixtures are imported by tests only. They are never registered in the production app.
export const testCourse: Course = {
  course_key: 'crs_opaque_A', display_name: 'Fixture finance · synthetic course',
  identity: { course_id: '2026_2027/Winter_Semester/JEM999_Finanční_fixture', academic_year: '2026_2027',
    semester: 'Winter_Semester', course_folder: 'JEM999_Finanční_fixture', course_code: 'JEM999' },
  bundle_ref: null, available_scope: ['Week one: checked sample scope'], blocked_scope: ['Week two: unresolved sample scope'], readiness: 'partial',
};
export const testProgress: Progress = { instruction_state: 'finished', assessment_submission_state: 'submitted',
  assessment_grading_state: 'finalized', canonical_commit_state: 'verified', evidence_state: 'current',
  completed: true, passed: false, needs_attention: true };
export const testWeeks: Week[] = [
  { course_key: testCourse.course_key, week_ref: { id: 'week_opaque_1', revision: 1 },
    readiness: 'ready', lessons: [{ id: 'lesson_opaque_1', revision: 1 }], progress: testProgress },
  { course_key: testCourse.course_key, week_ref: { id: 'week_opaque_2', revision: 1 },
    readiness: 'ready', lessons: [{ id: 'lesson_opaque_2', revision: 1 }], progress: null },
];
export const testHealth: Health = { ready: false, reason: 'scaffold_only', schema_version: 1, service: 'learning-hub', status: 'ok' };
export const testProvider: Provider = { account_revision: 0, eligibility: 'unknown', inference_verified: false, signed_in: false, usage: null };
export const testUpload: UploadReceipt = {
  course_key: testCourse.course_key, duplicate_source_revision_ids: [],
  sources: [{ source_id: 'source_A', source_revision_id: 'source_revision_A', course_key: testCourse.course_key,
    week_ref: testWeeks[0]!.week_ref, sha256: 'a'.repeat(64), byte_size: 7, extraction_state: 'pending',
    managed_relpath: 'sources/A.pdf', media_type: 'application/pdf', revision: 1 }],
  receipt: { receipt_id: 'receipt_A', command_id: 'command_A', command_kind: 'upload', kind: 'upload',
    aggregate_id: 'source_A', aggregate_revision: 1, durable_receipt: true, canonical_commit_state: 'not_applicable',
    canonical_event_ids: [], processing_state: 'received', received_at: '2026-10-12T10:00:00+02:00',
    status_url: '/api/v1/receipts/receipt_A' },
};
export function testClient(overrides: Partial<HubClient> = {}): HubClient {
  return { courses: vi.fn().mockResolvedValue([testCourse]), weeks: vi.fn().mockResolvedValue(testWeeks),
    health: vi.fn().mockResolvedValue(testHealth), provider: vi.fn().mockResolvedValue(testProvider),
    upload: vi.fn().mockResolvedValue(testUpload), ...overrides };
}
