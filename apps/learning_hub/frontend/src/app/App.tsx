import { useEffect, useState } from 'react';
import type { components } from '../api/generated/schema';

type Health = components['schemas']['HealthResponse'];
type State = { kind: 'loading' } | { kind: 'error' } | { kind: 'loaded'; health: Health };

export function App() {
  const [state, setState] = useState<State>({ kind: 'loading' });
  useEffect(() => {
    const controller = new AbortController();
    void fetch('/api/v1/health', { signal: controller.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error('Health request failed');
        const health = await response.json() as Health;
        if (!controller.signal.aborted) setState({ kind: 'loaded', health });
      })
      .catch(() => { if (!controller.signal.aborted) setState({ kind: 'error' }); });
    return () => controller.abort();
  }, []);
  return <main>
    <h1>Uni Learning Hub</h1>
    <p>Study content will appear after checked course publication is available.</p>
    <p role="status">{state.kind === 'loading' ? 'Connecting to local service…'
      : state.kind === 'error' ? 'Local service is unavailable.'
      : state.health.ready ? 'Local service is ready.' : 'Local service connected. Setup is incomplete.'}</p>
  </main>;
}
