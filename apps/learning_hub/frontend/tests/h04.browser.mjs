/**
 * H04 browser observations. HTTP fixtures exist solely inside this test process.
 * Run with a production preview and real loopback backend.
 */
import { chromium } from '@playwright/test';
import { mkdir, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
import process from 'node:process';
import { Buffer } from 'node:buffer';
import console from 'node:console';

const origin = process.env.H04_BROWSER_ORIGIN ?? 'http://127.0.0.1:5173';
const output = process.env.H04_SCREENSHOT_DIR ?? '/tmp/h04-browser';
await mkdir(output, { recursive: true });
const browser = await chromium.launch();
const evidence = [];
const course = {
  course_key: 'crs_opaque_A', display_name: 'Synthetic finance · fictional browser fixture',
  identity: { course_id: '2026_2027/Winter_Semester/JEM999_Finanční_fixture',
    academic_year: '2026_2027', semester: 'Winter_Semester', course_folder: 'JEM999_Finanční_fixture', course_code: 'JEM999' },
  bundle_ref: null, available_scope: ['Checked synthetic week-one scope'],
  blocked_scope: ['Unresolved synthetic week-two scope'], readiness: 'partial',
};
const weeks = [
  { course_key: course.course_key, week_ref: { id: 'week_opaque_1', revision: 1 }, readiness: 'ready',
    lessons: [{ id: 'lesson_opaque_1', revision: 1 }], progress: {
      instruction_state: 'finished', assessment_submission_state: 'submitted', assessment_grading_state: 'finalized',
      canonical_commit_state: 'verified', evidence_state: 'current', completed: true, passed: false, needs_attention: true } },
  { course_key: course.course_key, week_ref: { id: 'week_opaque_2', revision: 1 }, readiness: 'ready',
    lessons: [{ id: 'lesson_opaque_2', revision: 1 }], progress: null },
];
const provider = { account_revision: 0, signed_in: false, inference_verified: false, eligibility: 'unknown', usage: null };
async function noOverflow(page) {
  assert(await page.evaluate(() => globalThis.document.documentElement.scrollWidth <= globalThis.innerWidth + 1));
}
async function capture(page, name) {
  await noOverflow(page);
  await page.screenshot({ path: output + '/' + name + '.png', fullPage: true });
  evidence.push({ name, path: output + '/' + name + '.png', horizontal_overflow: false });
}
try {
  const real = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  await real.goto(origin);
  await real.getByText('Local service connected. Setup is incomplete.').waitFor();
  await real.getByRole('heading', { name: 'Unable to load this view' }).waitFor();
  await real.getByText('Provider status unknown').waitFor();
  await capture(real, 'production-missing-features');
  await real.close();
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  let mode = 'catalogue';
  await page.route('**/api/v1/courses', route => route.fulfill({
    status: mode === 'error' ? 503 : 200, contentType: 'application/json',
    body: JSON.stringify(mode === 'empty' ? [] : mode === 'error' ? {} : [course]),
  }));
  await page.route('**/api/v1/courses/*/weeks', route => route.fulfill({ contentType: 'application/json', body: JSON.stringify(weeks) }));
  await page.route('**/api/v1/provider/status', route => route.fulfill({ contentType: 'application/json', body: JSON.stringify(provider) }));
  await page.goto(origin);
  await page.getByRole('link', { name: course.display_name }).waitFor();
  await capture(page, 'desktop-catalogue');
  await page.getByRole('link', { name: 'View weeks' }).click();
  await page.getByRole('link', { name: 'week_opaque_2' }).waitFor();
  await capture(page, 'desktop-weeks');
  await page.getByRole('link', { name: 'week_opaque_2' }).click();
  await page.getByText('lesson_opaque_2', { exact: true }).waitFor();
  assert.equal(page.url(), origin + '/courses/crs_opaque_A/weeks/week_opaque_2');
  await page.goBack();
  await page.getByRole('link', { name: 'week_opaque_1' }).waitFor();
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(origin);
  await page.getByRole('link', { name: course.display_name }).waitFor();
  await capture(page, 'narrow-catalogue');
  await page.getByRole('button', { name: 'Menu', exact: true }).click();
  await capture(page, 'narrow-menu');
  await page.keyboard.press('Escape');
  assert.equal(await page.getByRole('button', { name: 'Menu', exact: true }).getAttribute('aria-expanded'), 'false');
  await page.keyboard.press('Tab');
  assert(await page.locator(':focus').count() > 0);
  mode = 'empty';
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto(origin);
  await page.getByRole('heading', { name: 'Your learning space is ready for its first course' }).waitFor();
  await capture(page, 'desktop-empty');
  mode = 'error';
  await page.goto(origin);
  await page.getByRole('heading', { name: 'Unable to load this view' }).waitFor();
  await capture(page, 'desktop-error');
  mode = 'catalogue';
  await page.getByRole('button', { name: 'Try again' }).click();
  await page.getByRole('link', { name: course.display_name }).waitFor();
  await page.goto(origin + '/materials');
  await page.getByLabel('Course', { exact: true }).selectOption(course.course_key);
  await page.getByLabel('Week', { exact: true }).selectOption('week_opaque_1');
  await page.getByLabel('Course source files').setInputFiles({ name: 'fictional-source.pdf', mimeType: 'application/pdf', buffer: Buffer.from('%PDF-1') });
  await page.getByText('Selected locally', { exact: true }).waitFor();
  await capture(page, 'desktop-upload-staged');
  await page.getByRole('button', { name: 'Save selected files' }).click();
  await page.getByText('Save failed', { exact: true }).waitFor();
  await capture(page, 'desktop-upload-session-required');
  assert.equal(errors.length, 0, errors.join('\n'));
  await page.close();
  await writeFile(output + '/observations.json', JSON.stringify({ fixture_scope: 'fictional/test-only', evidence, browser_errors: errors }, null, 2));
  console.log(JSON.stringify({ output, screenshots: evidence.length, result: 'passed' }));
} finally { await browser.close(); }
