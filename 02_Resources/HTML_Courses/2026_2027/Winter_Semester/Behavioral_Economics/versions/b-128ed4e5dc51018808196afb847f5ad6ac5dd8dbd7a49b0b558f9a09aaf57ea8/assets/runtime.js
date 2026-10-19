/* Offline lesson behavior. Local practice is never learner evidence. */
(() => {
  'use strict';
  const context = JSON.parse(document.getElementById('course-context').textContent);
  const namespace = `uni-html:${context.course_id}:${context.lesson_id}:${context.revision}:`;
  const read = key => { try { return localStorage.getItem(namespace + key); } catch { return null; } };
  const save = (key, value) => { try { localStorage.setItem(namespace + key, value); } catch { /* Optional browser convenience. */ } };
  const root = document.querySelector('main');
  try {
    renderMathInElement(document.body, {
      delimiters: [{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],
      throwOnError: true,
      errorCallback: (message, error) => { throw error || new Error(message); }
    });
    document.documentElement.dataset.mathStatus = 'passed';
  } catch (error) {
    document.documentElement.dataset.mathStatus = 'failed';
    const notice = document.createElement('p');
    notice.className = 'math-failure'; notice.setAttribute('role', 'alert');
    notice.textContent = 'Some mathematics could not be displayed. This page needs a rendering correction.';
    root.prepend(notice);
    console.error('HTML course math rendering failed', error);
  }

  document.querySelectorAll('[data-widget="numeric"], [data-widget="choice"]').forEach(widget => {
    const feedback = widget.querySelector('.feedback');
    const input = widget.querySelector('input');
    const key = input.id || input.name;
    const previous = read(key);
    if (previous !== null) {
      if (widget.dataset.widget === 'numeric') input.value = previous;
      else widget.querySelectorAll('input').forEach(choice => { choice.checked = choice.value === previous; });
    }
    widget.querySelector('button').addEventListener('click', () => {
      const numeric = widget.dataset.widget === 'numeric';
      const selected = numeric ? input : widget.querySelector('input:checked');
      const raw = selected ? selected.value.trim() : '';
      if (!raw) {
        feedback.textContent = numeric ? 'Enter an answer first.' : 'Choose an answer first.';
        feedback.className = 'feedback error'; return;
      }
      const number = Number(raw);
      const correct = numeric
        ? Number.isFinite(number) && Math.abs(number - Number(widget.dataset.answer)) <= Number(widget.dataset.tolerance)
        : raw === widget.dataset.answer;
      save(key, raw);
      feedback.textContent = correct
        ? 'That matches the checked answer. Reveal the explanation to compare the reasoning.'
        : 'That does not match the checked answer yet. Try again, or reveal the explanation.';
      feedback.className = 'feedback' + (correct ? '' : ' error');
      if (numeric) input.setAttribute('aria-invalid', String(!correct));
    });
  });

  document.querySelectorAll('textarea[data-draft]').forEach(field => {
    field.value = read(field.dataset.draft) || '';
    field.addEventListener('input', () => save(field.dataset.draft, field.value));
  });

  document.querySelectorAll('[data-widget="residual-plot"]').forEach(widget => {
    const config = JSON.parse(widget.dataset.config);
    const canvas = widget.querySelector('canvas'), range = widget.querySelector('input[type=range]');
    const output = widget.querySelector('.slider-number'), sse = widget.querySelector('.sse');
    const points = config.points;
    function draw() {
      const width = canvas.clientWidth, height = canvas.clientHeight, dpr = devicePixelRatio || 1;
      canvas.width = width * dpr; canvas.height = height * dpr;
      const ctx = canvas.getContext('2d'); ctx.scale(dpr,dpr);
      const slope = Number(range.value), intercept = config.intercept;
      let x0 = Math.min(0, ...points.map(p=>p[0])), x1 = Math.max(...points.map(p=>p[0]));
      if (x0 === x1) { x0 -= 1; x1 += 1; }
      const xpad = (x1-x0)*.08; x1 += xpad;
      let y0 = Math.min(0, ...points.map(p=>p[1]), intercept+slope*x0, intercept+slope*x1);
      let y1 = Math.max(...points.map(p=>p[1]), intercept+slope*x0, intercept+slope*x1);
      if (y0 === y1) { y0 -= 1; y1 += 1; }
      const ypad = (y1-y0)*.13; y1 += ypad;
      const left=45, right=12, top=15, bottom=33;
      const xx=x=>left+(x-x0)/(x1-x0)*(width-left-right);
      const yy=y=>height-bottom-(y-y0)/(y1-y0)*(height-top-bottom);
      ctx.clearRect(0,0,width,height); ctx.lineWidth=1; ctx.strokeStyle='#929b8f';
      ctx.beginPath(); ctx.moveTo(left,top); ctx.lineTo(left,height-bottom); ctx.lineTo(width-right,height-bottom); ctx.stroke();
      ctx.font='12px Georgia'; ctx.fillStyle='#657165';
      for(let i=0;i<=4;i++) {
        const x=x0+i*(x1-x0)/4, y=y0+i*(y1-y0)/4;
        ctx.textAlign='center'; ctx.fillText(Number(x.toFixed(1)),xx(x),height-12);
        ctx.textAlign='right'; ctx.fillText(Number(y.toFixed(1)),left-9,yy(y)+4);
      }
      let error=0;
      points.forEach(([x,y],i)=>{
        const fitted=intercept+slope*x; error+=(y-fitted)**2;
        ctx.strokeStyle=i===2?'#a14436':'#b2bfad'; ctx.lineWidth=i===2?1.8:1.2;
        ctx.beginPath(); ctx.moveTo(xx(x),yy(y)); ctx.lineTo(xx(x),yy(fitted)); ctx.stroke();
        ctx.fillStyle=i===2?'#a14436':'#164e3e'; ctx.beginPath(); ctx.arc(xx(x),yy(y),4,0,Math.PI*2); ctx.fill();
      });
      ctx.strokeStyle='#164e3e'; ctx.lineWidth=2;
      ctx.beginPath(); ctx.moveTo(xx(x0),yy(intercept+slope*x0)); ctx.lineTo(xx(x1),yy(intercept+slope*x1)); ctx.stroke();
      output.textContent=slope.toFixed(2); sse.textContent=error.toFixed(2);
      canvas.setAttribute('aria-label', `${points.length} observations, intercept ${intercept}, slope ${slope.toFixed(2)}. Sum of squared residuals ${error.toFixed(2)}.`);
    }
    range.addEventListener('input',draw);
    widget.querySelector('button').addEventListener('click',()=>{range.value=config.slope;draw();});
    new ResizeObserver(draw).observe(canvas); draw();
  });

  if(context.lesson_id) {
    addEventListener('pagehide',()=>save('position',String(scrollY)));
    if(!location.hash) {
      const y=Number(read('position'));
      if(Number.isFinite(y)&&y>0) document.fonts.ready.then(()=>requestAnimationFrame(()=>scrollTo(0,y)));
    }
  }
})();
