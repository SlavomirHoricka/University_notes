import { useCallback, useEffect, useRef, useState, type ReactNode } from 'react';
import { createHubClient, type HubClient } from '../api/client';
import { Catalogue, CoursePage } from '../features/courses/Catalogue';
import { Materials, useMaterialsDraft } from '../features/courses/Materials';
import { Link, usePath } from './navigation';
import { useHubQuery } from './query';
import { EmptyState, PageHeading } from './ui';

const productionClient = createHubClient();
const navigation = [
  { path: '/', label: 'Overview', symbol: '◫' },
  { path: '/courses', label: 'Courses', symbol: '▤' },
  { path: '/materials', label: 'Materials', symbol: '▱' },
  { path: '/agents', label: 'Agents', symbol: '◇' },
  { path: '/settings', label: 'Settings', symbol: '⚙' },
];
function active(path: string, current: string) { return path === '/' ? current === '/' : current === path || current.startsWith(`${path}/`); }
export function SidebarNav({ path, onNavigate }: { path: string; onNavigate: () => void }) {
  return <nav aria-label="Main navigation">{navigation.map(item => <Link key={item.path} href={item.path}
    className={`nav-link ${active(item.path, path) ? 'active' : ''}`} aria-current={active(item.path, path) ? 'page' : undefined} onClick={onNavigate}>
    <span className="nav-symbol" aria-hidden="true">{item.symbol}</span>{item.label}</Link>)}</nav>;
}
export function ServiceStatus({ client }: { client: HubClient }) {
  const readHealth = useCallback((signal: AbortSignal) => client.health(signal), [client]);
  const health = useHubQuery('health', readHealth);
  const readProvider = useCallback((signal: AbortSignal) => client.provider(signal), [client]);
  const provider = useHubQuery('provider:account', readProvider);
  return <section className="service-status" aria-label="Local service and AI status"><h2>Local connection</h2>
    <div role="status"><p><span className={`connection-dot ${health.state.kind === 'ready' ? 'connected' : ''}`} aria-hidden="true" />
      {health.state.kind === 'pending' ? 'Connecting to local service…' : health.state.kind === 'error' ? 'Local service is unavailable.'
        : 'Local service connected. Setup is incomplete.'}</p></div>
    {health.state.kind === 'error' && <button className="text-button" onClick={health.retry}>Retry connection</button>}
    <hr /><p className="status-label">AI account</p>
    <p>{provider.state.kind === 'pending' ? 'Checking provider…' : provider.state.kind === 'error' ? 'Provider status unknown'
      : provider.state.data.signed_in ? 'Signed in' : 'Not signed in'}</p>
    {provider.state.kind === 'ready' && <><p>Eligibility: {provider.state.data.eligibility.replaceAll('_', ' ')}</p><p>Inference: {provider.state.data.inference_verified ? 'Verified' : 'Not verified'}</p></>}
    {provider.state.kind === 'ready' && provider.state.data.usage ? <div className="muted">
      <p>Reported usage: {provider.state.data.usage.used_percent === null ? 'unknown' : `${provider.state.data.usage.used_percent}% used`}</p>
      <p>Reported reset: {provider.state.data.usage.reset_at ? new Date(provider.state.data.usage.reset_at).toLocaleString() : 'unknown'}</p>
      <p>Scope: {provider.state.data.usage.scope}<br />Measured: {new Date(provider.state.data.usage.measured_at).toLocaleString()}</p>
    </div> : <p className="muted">Usage and reset time unknown.</p>}
    {provider.state.kind === 'error' && <button className="text-button" onClick={provider.retry}>Retry provider status</button>}
  </section>;
}
export function AppShell({ path, client, children }: { path: string; client: HubClient; children: ReactNode }) {
  const [menuOpen, setMenuOpen] = useState(false);
  const menuButton = useRef<HTMLButtonElement>(null);
  const main = useRef<HTMLElement>(null);
  const previousPath = useRef(path);
  useEffect(() => {
    if (previousPath.current !== path) {
      previousPath.current = path;
      (main.current?.querySelector<HTMLElement>('h1') ?? main.current)?.focus();
      window.scrollTo({ top: 0, behavior: 'instant' });
    }
  }, [path]);
  const label = navigation.find(item => active(item.path, path))?.label ?? 'Learning hub';
  return <div className="app-layout"><a className="skip-link" href="#main-content">Skip to content</a>
    <aside className={`sidebar ${menuOpen ? 'menu-open' : ''}`} aria-label="Learning hub" onKeyDown={event => {
      if (event.key === 'Escape') { setMenuOpen(false); menuButton.current?.focus(); }
    }}><Link href="/" className="brand"><span className="brand-mark" aria-hidden="true">L</span><span>Learnspace<small>Personal learning hub</small></span></Link>
      <button ref={menuButton} className="menu-button" aria-expanded={menuOpen} aria-controls="primary-navigation" onClick={() => setMenuOpen(x => !x)}>{menuOpen ? 'Close menu' : 'Menu'}</button>
      <div id="primary-navigation" className="sidebar-navigation"><p className="eyebrow">Your workspace</p><SidebarNav path={path} onNavigate={() => setMenuOpen(false)} />
        <div className="sidebar-note"><span aria-hidden="true">✦</span><strong>One topic at a time.</strong><p>Checked content. Your pace. Room to revisit.</p></div></div>
      <div className="sidebar-foot"><span className="avatar" aria-hidden="true">U</span><div><strong>Your learning space</strong><small>On this computer</small></div></div>
    </aside>
    <div className="workspace"><header className="topbar"><span>Workspace <span aria-hidden="true">/</span> <strong>{label}</strong></span><span className="local-label">Local workspace</span></header>
      <div className="content-layout"><main ref={main} id="main-content" tabIndex={-1}>{children}</main>
        <aside className="right-rail" aria-label="Workspace information"><ServiceStatus client={client} /><section className="rail-note"><p className="eyebrow">Learning without locks</p><h2>Keep exploring.</h2><p>Published weeks remain available. A review recommendation can help you choose your next step.</p></section></aside>
      </div>
    </div>
  </div>;
}
function route(path: string, client: HubClient, draft: ReturnType<typeof useMaterialsDraft>) {
  if (path === '/' || path === '/courses') return <Catalogue client={client} dashboard={path === '/'} />;
  if (path === '/materials') return <Materials client={client} draft={draft} />;
  const match = /^\/courses\/([^/]+)(?:\/weeks\/([^/]+))?$/.exec(path);
  if (match?.[1]) {
    try { return <CoursePage client={client} courseKey={decodeURIComponent(match[1])} {...(match[2] ? { weekId: decodeURIComponent(match[2]) } : {})} />; }
    catch { /* malformed routes remain visible errors, not guessed identities */ }
  }
  if (path === '/agents' || path === '/settings') return <><PageHeading eyebrow="Your workspace" title={path === '/agents' ? 'Agents' : 'Settings'} />
    <EmptyState title={path === '/agents' ? 'Preparation activity will appear here' : 'Account controls are being connected'}>
      {path === '/agents' ? 'Job timelines and controls become available when the durable preparation service is connected.' : 'The local connection panel shows the current service and provider state. Account actions become available when the supported provider flow is connected.'}</EmptyState></>;
  return <><PageHeading eyebrow="Learning hub" title="Page unavailable" /><EmptyState title="This route is not available">Open Courses to choose a published course and week.</EmptyState></>;
}
export function App({ client = productionClient }: { client?: HubClient }) {
  const path = usePath();
  const draft = useMaterialsDraft();
  return <AppShell path={path} client={client}>{route(path, client, draft)}</AppShell>;
}
