import { useCallback } from 'react';
import type { Course, HubClient, Week } from '../../api/client';
import { coursePath, Link, weekPath } from '../../app/navigation';
import { useHubQuery } from '../../app/query';
import { EmptyState, ErrorState, PageHeading, PendingState, ProcessProgress, ReadinessBadge } from '../../app/ui';

export function CourseIdentity({ course }: { course: Course }) {
  return <p className="identity">{course.identity.academic_year.replace('_', '–')} · {course.identity.semester.replace('_', ' ')}<br />
    <span>{course.identity.course_folder}</span>{course.identity.course_code && <span> · {course.identity.course_code}</span>}</p>;
}
export function Coverage({ course }: { course: Course }) {
  return <div className="coverage"><p><strong>{course.available_scope.length}</strong> available scope {course.available_scope.length === 1 ? 'entry' : 'entries'} · <strong>{course.blocked_scope.length}</strong> blocked</p>
    <p className="muted">Progress covers available required activities only. Full semester completion is unknown.</p>
    {course.available_scope.length > 0 && <details><summary>Available scope</summary><ul>{course.available_scope.map((scope, i) => <li key={`${i}:${scope}`}>{scope}</li>)}</ul></details>}
    {course.blocked_scope.length > 0 && <details><summary>Blocked scope</summary><ul>{course.blocked_scope.map((scope, i) => <li key={`${i}:${scope}`}>{scope}</li>)}</ul></details>}
  </div>;
}
export function CourseCard({ course }: { course: Course }) {
  return <article className="course-card"><div className="course-top"><span className="course-symbol" aria-hidden="true">▤</span><ReadinessBadge value={course.readiness} /></div>
    <h2><Link href={coursePath(course.course_key)}>{course.display_name}</Link></h2><CourseIdentity course={course} />
    <Coverage course={course} /><ProcessProgress progress={null} />
    <div className="course-footer"><span className="muted">Explore at your pace</span><Link className="text-link" href={coursePath(course.course_key)}>View weeks <span aria-hidden="true">→</span></Link></div>
  </article>;
}
export function Catalogue({ client, dashboard }: { client: HubClient; dashboard: boolean }) {
  const read = useCallback((signal: AbortSignal) => client.courses(signal), [client]);
  const { state, retry } = useHubQuery('courses:current-publication', read);
  return <><PageHeading eyebrow="Your learning space" title={dashboard ? 'Make room for learning.' : 'Your courses'}>
    Checked materials, short lessons, and a clear place to pick up again.</PageHeading>
    {state.kind === 'pending' ? <PendingState /> : state.kind === 'error' ? <ErrorState message={state.message} retry={retry} />
      : state.data.length === 0 ? <EmptyState title="Your learning space is ready for its first course">Courses appear here when the local service has a course inventory. Checked publication makes lessons available.</EmptyState>
        : <>
          {dashboard && <div className="summary-grid"><article className="summary-card"><span>Courses in your catalogue</span><strong>{state.data.length}</strong></article>
            <article className="summary-card"><span>Courses with checked publication</span><strong>{state.data.filter(c => c.bundle_ref !== null).length}</strong></article>
            <article className="summary-card"><span>Learning evidence</span><strong className="summary-text">Unknown</strong><small>Open a course for its current process status.</small></article></div>}
          <div className="section-heading"><h2>Continue exploring</h2>{dashboard && <Link className="text-link" href="/courses">All courses →</Link>}</div>
          <div className="course-grid">{state.data.map(c => <CourseCard key={c.course_key} course={c} />)}</div>
        </>}
    <section className="panel quiet-panel"><span className="eyebrow">From source to study</span><h2>A checked path into each topic</h2><p>Save materials to a course and week. Preparation and independent checks happen before new lessons are published.</p><Link className="text-link" href="/materials">Open materials →</Link></section>
  </>;
}
export function WeekList({ courseKey, weeks, selected }: { courseKey: string; weeks: Week[]; selected?: string }) {
  if (!weeks.length) return <EmptyState title="No weeks available yet">Published weeks will appear after materials have been prepared and checked.</EmptyState>;
  return <ol className="week-list">{weeks.map((week, i) => <li key={`${week.week_ref.id}:${week.week_ref.revision}`}>
    <article className={`week-card ${selected === week.week_ref.id ? 'selected' : ''}`}>
      <div className="week-heading"><div><p className="eyebrow">Week in published order · {i + 1}</p><h2><Link href={weekPath(courseKey, week.week_ref.id)}>{week.week_ref.id}</Link></h2></div><ReadinessBadge value={week.readiness} /></div>
      <p className="muted">Revision {week.week_ref.revision} · {week.lessons.length} prepared lesson {week.lessons.length === 1 ? 'reference' : 'references'}</p>
      <ProcessProgress progress={week.progress} />
      {week.lessons.length > 0 && <ol className="lesson-list">{week.lessons.map(lesson => <li key={`${lesson.id}:${lesson.revision}`}><div><strong>{lesson.id}</strong><p>Teaching estimate: unknown · Separate quiz estimate: unknown</p><p>Required / optional status: unknown</p></div><span className="badge neutral">Revision {lesson.revision}</span></li>)}</ol>}
      <p className="muted">Lesson titles, estimates, and study actions will appear when the service supplies prepared lesson metadata.</p>
    </article>
  </li>)}</ol>;
}
export function CoursePage({ client, courseKey, weekId }: { client: HubClient; courseKey: string; weekId?: string }) {
  const readCourses = useCallback((signal: AbortSignal) => client.courses(signal), [client]);
  const catalogue = useHubQuery('courses:current-publication', readCourses);
  const course = catalogue.state.kind === 'ready' ? catalogue.state.data.find(c => c.course_key === courseKey) : undefined;
  const readWeeks = useCallback((signal: AbortSignal) => client.weeks(courseKey, signal), [client, courseKey]);
  const weeks = useHubQuery(`weeks:${courseKey}:${JSON.stringify(course?.bundle_ref ?? null)}`, readWeeks);
  if (catalogue.state.kind === 'pending') return <PendingState />;
  if (catalogue.state.kind === 'error') return <ErrorState message={catalogue.state.message} retry={catalogue.retry} />;
  if (!course) return <EmptyState title="Course not found">This course is not in the current catalogue. Return to Courses to choose an available course.</EmptyState>;
  const displayed = weeks.state.kind === 'ready' && weekId ? weeks.state.data.filter(w => w.week_ref.id === weekId) : weeks.state.kind === 'ready' ? weeks.state.data : [];
  return <><Link className="text-link" href={weekId ? coursePath(courseKey) : '/courses'}>← {weekId ? 'All weeks' : 'All courses'}</Link>
    <PageHeading eyebrow={weekId ? 'Course week' : 'Course overview'} title={course.display_name} /><CourseIdentity course={course} />
    <section className="panel course-overview"><ReadinessBadge value={course.readiness} /><Coverage course={course} /><p>Published weeks remain available independently of previous scores.</p><Link className="text-link" href="/materials">Add course materials →</Link></section>
    {weeks.state.kind === 'pending' ? <PendingState children="Loading course weeks…" />
      : weeks.state.kind === 'error' ? <ErrorState message={weeks.state.message} retry={weeks.retry} />
        : weekId && !displayed.length ? <EmptyState title="Week not found">This week is not in the current publication. Use All weeks to choose a published week.</EmptyState>
          : <WeekList courseKey={courseKey} weeks={displayed} {...(weekId ? { selected: weekId } : {})} />}
  </>;
}
