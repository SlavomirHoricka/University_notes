import { useCallback, useEffect, useState } from 'react';

export type QueryState<T> = { kind: 'pending' } | { kind: 'error'; message: string } | { kind: 'ready'; data: T };

/** Shared read hook; keys include the published identity so versions cannot share a read. */
export function useHubQuery<T>(key: string, read: (signal: AbortSignal) => Promise<T>) {
  const [attempt, setAttempt] = useState(0);
  const [snapshot, setSnapshot] = useState<{ key: string; attempt: number; state: QueryState<T> }>();
  useEffect(() => {
    const controller = new AbortController();
    void read(controller.signal).then(data => {
      if (!controller.signal.aborted) setSnapshot({ key, attempt, state: { kind: 'ready', data } });
    }).catch((error: unknown) => {
      if (!controller.signal.aborted) setSnapshot({ key, attempt, state: { kind: 'error',
        message: error instanceof Error ? error.message : 'The request failed. Try again.' } });
    });
    return () => controller.abort();
  }, [key, attempt, read]);
  const state: QueryState<T> = snapshot?.key === key && snapshot.attempt === attempt ? snapshot.state : { kind: 'pending' };
  return { state, retry: useCallback(() => setAttempt(x => x + 1), []) };
}
