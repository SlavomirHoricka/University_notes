import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../src/app/App';

describe('truthful empty scaffold', () => {
  it('shows incomplete setup without learner claims', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true,
      json: async () => ({ schema_version: 1, service: 'learning-hub', status: 'ok',
        ready: false, reason: 'scaffold_only' }) }));
    render(<App />);
    expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('Uni Learning Hub');
    expect(await screen.findByText('Local service connected. Setup is incomplete.')).toBeVisible();
    expect(screen.queryByRole('button', { name: /complete/i })).toBeNull();
  });
  it('reports service failure', async () => {
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new Error('offline')));
    render(<App />);
    expect(await screen.findByText('Local service is unavailable.')).toBeVisible();
  });
});
