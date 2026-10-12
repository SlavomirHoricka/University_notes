import { useSyncExternalStore, type ComponentProps } from 'react';

const subscribe = (notify: () => void) => {
  window.addEventListener('popstate', notify);
  return () => window.removeEventListener('popstate', notify);
};
export function usePath() { return useSyncExternalStore(subscribe, () => window.location.pathname); }
export function navigate(path: string) {
  if (path === window.location.pathname) return;
  window.history.pushState(null, '', path);
  window.dispatchEvent(new PopStateEvent('popstate'));
}
export function Link({ href, onClick, ...props }: ComponentProps<'a'> & { href: string }) {
  return <a {...props} href={href} onClick={event => {
    onClick?.(event);
    if (!event.defaultPrevented && event.button === 0 && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey) {
      event.preventDefault(); navigate(href);
    }
  }} />;
}
export const coursePath = (key: string) => `/courses/${encodeURIComponent(key)}`;
export const weekPath = (key: string, weekId: string) => `${coursePath(key)}/weeks/${encodeURIComponent(weekId)}`;
