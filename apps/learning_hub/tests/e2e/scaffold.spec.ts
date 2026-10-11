import { expect, test } from '../../frontend/tests/e2eHarness';

test('real loopback API connects to empty shell', async ({ page, request }, testInfo) => {
  const health = await request.get('/api/v1/health');
  expect(health.ok()).toBeTruthy();
  expect(await health.json()).toMatchObject({ status: 'ok', ready: false, reason: 'scaffold_only' });
  await page.goto('/');
  await expect(page.getByRole('heading', { name: 'Uni Learning Hub', level: 1 })).toBeVisible();
  await expect(page.getByRole('status')).toContainText('Setup is incomplete.');
  await expect(page.getByRole('button', { name: /complete|pass/i })).toHaveCount(0);
  await page.screenshot({ path: testInfo.outputPath('scaffold.png'), fullPage: true });
});
