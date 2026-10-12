import { expect, test } from '../../frontend/tests/e2eHarness';

test('real loopback API connects to the course shell without claiming readiness', async ({ page, request }, testInfo) => {
  const health = await request.get('/api/v1/health');
  expect(health.ok()).toBeTruthy();
  expect(await health.json()).toMatchObject({ status: 'ok', ready: false, reason: 'scaffold_only' });
  await page.goto('/');
  await expect(page.getByRole('heading', { name: 'Make room for learning.', level: 1, exact: true })).toBeVisible();
  const serviceStatus = page.getByRole('region', { name: 'Local service and AI status', exact: true });
  await expect(serviceStatus.getByRole('status')).toHaveText('Local service connected. Setup is incomplete.');
  await expect(page.getByRole('button', { name: /complete|pass/i })).toHaveCount(0);
  await page.screenshot({ path: testInfo.outputPath('scaffold.png'), fullPage: true });
});
