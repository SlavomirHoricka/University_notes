import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: '../tests/e2e',
  fullyParallel: false,
  use: { baseURL: 'http://127.0.0.1:5173' },
  webServer: [
    { command: 'uv run --locked uvicorn learning_hub.application.core.bootstrap:create_app --factory --host 127.0.0.1 --port 8765',
      cwd: '..', url: 'http://127.0.0.1:8765/api/v1/health', reuseExistingServer: false },
    { command: 'npm run dev', url: 'http://127.0.0.1:5173', reuseExistingServer: false },
  ],
});
