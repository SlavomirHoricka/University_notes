import { fireEvent, render, screen, within } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../src/app/App';
import { testClient, testCourse, testWeeks } from './h04.fixtures';

beforeEach(() => { window.history.replaceState(null, '', '/'); vi.stubGlobal('scrollTo', vi.fn()); });
describe('H04 shell and truthful catalogue', () => {
  it('shows backend course identity and scope without learner claims (H04-A2)', async () => {
    render(<App client={testClient()} />);
    expect(screen.getByRole('heading', { level: 1 })).toHaveTextContent('Make room for learning.');
    expect(await screen.findByText('Local service connected. Setup is incomplete.')).toBeVisible();
    expect(await screen.findByRole('link', { name: testCourse.display_name })).toHaveAttribute('href', '/courses/crs_opaque_A');
    expect(screen.getByText('JEM999_Finanční_fixture')).toBeVisible();
    expect(screen.getByText(/Full semester completion is unknown/)).toBeVisible();
    expect(screen.getByText('Attention unknown')).toBeVisible();
    expect(screen.queryByRole('button', { name: /complete/i })).toBeNull();
    expect(localStorage.length).toBe(0);
  });
  it('distinguishes an empty catalogue from an error', async () => {
    render(<App client={testClient({ courses: vi.fn().mockResolvedValue([]) })} />);
    expect(await screen.findByRole('heading', { name: 'Your learning space is ready for its first course' })).toBeVisible();
    expect(screen.queryByText('Courses in your catalogue')).toBeNull();
  });
  it('reports service failure and recovers through retry', async () => {
    const courses = vi.fn().mockRejectedValueOnce(new Error('offline')).mockResolvedValue([testCourse]);
    render(<App client={testClient({ courses, health: vi.fn().mockRejectedValue(new Error('offline')) })} />);
    expect(await screen.findByText('Local service is unavailable.')).toBeVisible();
    expect(await screen.findByRole('alert')).toHaveTextContent('offline');
    fireEvent.click(screen.getByRole('button', { name: 'Try again' }));
    expect(await screen.findByRole('link', { name: testCourse.display_name })).toBeVisible();
  });
  it('keeps pending catalogue and provider states unknown', async () => {
    render(<App client={testClient({ courses: () => new Promise(() => {}), provider: () => new Promise(() => {}) })} />);
    expect(screen.getByText('Loading checked course data…')).toBeVisible();
    expect(screen.getByText('Checking provider…')).toBeVisible();
    expect(screen.getByText('Usage and reset time unknown.')).toBeVisible();
  });
  it('uses opaque week links and leaves later published weeks accessible after failure (H04-A1)', async () => {
    window.history.replaceState(null, '', '/courses/crs_opaque_A');
    render(<App client={testClient()} />);
    const nextWeek = await screen.findByRole('link', { name: testWeeks[1]!.week_ref.id });
    expect(nextWeek).toHaveAttribute('href', '/courses/crs_opaque_A/weeks/week_opaque_2');
    expect(nextWeek).not.toHaveAttribute('aria-disabled');
    expect(screen.getByText('Not passed')).toBeVisible();
    fireEvent.click(nextWeek);
    expect(await screen.findByRole('link', { name: /All weeks/ })).toBeVisible();
    expect(window.location.pathname).toBe('/courses/crs_opaque_A/weeks/week_opaque_2');
    const main = within(screen.getByRole('main'));
    expect(await main.findByText('lesson_opaque_2')).toBeVisible();
    expect(main.queryByText('lesson_opaque_1')).toBeNull();
  });
  it('rejects malformed route escapes without losing the shell', async () => {
    window.history.replaceState(null, '', '/courses/%ZZ');
    render(<App client={testClient()} />);
    expect(screen.getByRole('heading', { name: 'Page unavailable' })).toBeVisible();
    expect(await screen.findByText('Not signed in')).toBeVisible();
  });
  it('supports keyboard menu state and Escape focus', () => {
    render(<App client={testClient()} />);
    const menu = screen.getByRole('button', { name: 'Menu' });
    fireEvent.click(menu);
    expect(menu).toHaveAttribute('aria-expanded', 'true');
    fireEvent.keyDown(screen.getByRole('navigation', { name: 'Main navigation' }), { key: 'Escape' });
    expect(menu).toHaveAttribute('aria-expanded', 'false');
    expect(menu).toHaveFocus();
  });
});
