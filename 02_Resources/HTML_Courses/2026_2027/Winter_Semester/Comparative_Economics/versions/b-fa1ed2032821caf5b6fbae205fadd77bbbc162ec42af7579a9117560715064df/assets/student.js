
(() => {
  'use strict';
  const studentContext = JSON.parse(document.getElementById("course-context").textContent);
  const sections = studentContext.navigation;
  const script = document.currentScript;
  const courseRoot = new URL('../../', script.src);
  const sidebar = document.querySelector('.sidebar');
  const hub = document.createElement('a');
  hub.className = 'hub-link'; hub.textContent = '← Course hub';
  const hubUrl = new URL(location.href);
  const path = decodeURIComponent(hubUrl.pathname);
  const marker = '/' + studentContext.course_id + '/';
  const position = path.lastIndexOf(marker);
  if (position >= 0) { hubUrl.pathname = path.slice(0, position) + '/index.html'; hubUrl.hash = ''; hubUrl.search = ''; hub.href = hubUrl.href; }
  else hub.hidden = true;
  sidebar.insertBefore(hub, sidebar.querySelector('.contents-link'));
  const nav = sidebar.querySelector('nav');
  const mobile = document.createElement('button');
  mobile.type = 'button'; mobile.className = 'nav-switch'; mobile.textContent = 'Browse lessons and sections';
  mobile.setAttribute('aria-expanded', 'false'); nav.id = 'course-navigation'; mobile.setAttribute('aria-controls', nav.id);
  sidebar.insertBefore(mobile, nav);
  mobile.addEventListener('click', () => { const open = mobile.getAttribute('aria-expanded') !== 'true'; mobile.setAttribute('aria-expanded', String(open)); nav.dataset.open = String(open); });
  const current = JSON.parse(document.getElementById('course-context').textContent).lesson_id;
  document.body.classList.add('student-course');
  nav.querySelectorAll('a.lesson-link').forEach((link, index) => {
    const lid = new URL(link.href).pathname.split('/').pop().replace('.html', '');
    const wrap = document.createElement('div'); wrap.className = 'lesson-entry';
    const head = document.createElement('div'); head.className = 'lesson-entry-head';
    link.replaceWith(wrap); head.append(link); wrap.append(head);
    const list = document.createElement('ul'); list.className = 'lesson-sections'; list.id = `lesson-parts-${index}`;
    list.hidden = lid !== current;
    const toggle = document.createElement('button'); toggle.type = 'button'; toggle.className = 'lesson-toggle';
    toggle.setAttribute('aria-label', `Sections in ${link.textContent.trim()}`); toggle.setAttribute('aria-controls', list.id); toggle.setAttribute('aria-expanded', String(!list.hidden));
    const chevron = document.createElement('span'); chevron.setAttribute('aria-hidden', 'true'); chevron.textContent = '›'; toggle.append(chevron);
    head.append(toggle); wrap.append(list);
    (sections[lid] || []).forEach(part => {
      const li = document.createElement('li'); if (part.sub) li.className = 'subsection';
      const a = document.createElement('a'); a.href = link.href.split('#')[0] + '#' + part.id; a.textContent = part.label;
      li.append(a); list.append(li);
    });
    toggle.addEventListener('click', () => { list.hidden = !list.hidden; toggle.setAttribute('aria-expanded', String(!list.hidden)); });
  });
  const update = id => {
    sidebar.querySelectorAll('.lesson-sections a').forEach(a => {
      if (new URL(a.href).pathname === location.pathname && new URL(a.href).hash === '#' + id) a.setAttribute('aria-current', 'location');
      else a.removeAttribute('aria-current');
    });
  };
  const observed = [...document.querySelectorAll('main section.section')];
  const observer = new IntersectionObserver(entries => {
    const visible = entries.filter(e => e.isIntersecting).sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible.length) update(visible[0].target.id);
  }, {rootMargin: '-5% 0px -65% 0px'});
  observed.forEach(el => observer.observe(el));
  if (location.hash) update(decodeURIComponent(location.hash.slice(1)));
  else if (observed.length) update(observed[0].id);
  // Keep late-review material closed until the reader chooses to open it.
  if (current) {
    const questions = studentContext.quiz || [];
    if (questions.length) {
    const quizWidgets = questions.map(question => {
      const first = document.querySelector(`input[name="${question.id}"]`);
      return first.closest('.practice');
    });
    const context = JSON.parse(document.getElementById('course-context').textContent);
    const namespace = `uni-html:${context.course_id}:${context.lesson_id}:${context.revision}:`;
    const score = document.createElement('p'); score.className = 'quiz-score'; score.setAttribute('role', 'status'); score.setAttribute('aria-live', 'polite');
    questions.forEach((question, index) => {
      const widget = quizWidgets[index];
      const feedback = widget.querySelector('.feedback');
      widget.querySelector('button').addEventListener('click', () => {
        const selected = widget.querySelector('input:checked');
        if (!selected) {
          feedback.textContent = 'Choose one answer before checking.'; feedback.className = 'feedback error';
          return;
        }
        const choice = Number(selected.value);
        const correct = choice === question.correct_index;
        feedback.textContent = (correct ? '' : 'Not yet. ') + question.feedback[choice];
        feedback.className = correct ? 'feedback' : 'feedback error';
        widget.querySelector('fieldset').setAttribute('aria-invalid', String(!correct));
      });
      widget.querySelectorAll('input').forEach(input => input.addEventListener('change', () => {
        feedback.textContent = ''; widget.querySelector('fieldset').removeAttribute('aria-invalid'); score.textContent = '';
      }));
    });
    const actions = document.createElement('div'); actions.className = 'quiz-actions';
    const checkAll = document.createElement('button'); checkAll.type = 'button'; checkAll.className = 'button'; checkAll.textContent = 'Check all answers';
    const reset = document.createElement('button'); reset.type = 'button'; reset.className = 'button secondary'; reset.textContent = 'Start again';
    actions.append(checkAll, reset, score); quizWidgets.at(-1).after(actions);
    checkAll.addEventListener('click', () => {
      let correct = 0, answered = 0;
      questions.forEach((question, index) => {
        quizWidgets[index].querySelector('button').click();
        const selected = quizWidgets[index].querySelector('input:checked');
        if (selected) { answered++; if (Number(selected.value) === question.correct_index) correct++; }
      });
      score.textContent = `${correct} / ${questions.length} correct.` + (answered < questions.length ? ` ${questions.length - answered} unanswered.` : ' Review the feedback above.');
    });
    reset.addEventListener('click', () => {
      questions.forEach((question, index) => {
        const widget = quizWidgets[index];
        widget.querySelectorAll('input').forEach(input => {input.checked = false;});
        widget.querySelector('.feedback').textContent = ''; widget.querySelector('fieldset').removeAttribute('aria-invalid');
        widget.querySelectorAll('details.solution-block').forEach(details => {details.open = false;});
        try {localStorage.removeItem(namespace + question.id);} catch {}
      });
      score.textContent = '';
    });
    }
    const body = document.querySelector('#later-review > .section-body');
    if (body) {
    const widgets = [...body.querySelectorAll(':scope > .practice')];
    const disclosure = document.createElement('details'); disclosure.className = 'later-questions';
    const summary = document.createElement('summary'); summary.textContent = 'Open later-review questions'; disclosure.append(summary);
    widgets.forEach(widget => disclosure.append(widget)); body.append(disclosure);
    }
    document.querySelectorAll('a[href]').forEach(a => a.addEventListener('click', () => {
      const target = new URL(a.href);
      if (target.pathname === location.pathname && target.hash) {
        const el = document.getElementById(decodeURIComponent(target.hash.slice(1)));
        for (let parent = el?.parentElement; parent; parent = parent.parentElement) if (parent.tagName === 'DETAILS') parent.open = true;
      }
    }));
  }
})();
