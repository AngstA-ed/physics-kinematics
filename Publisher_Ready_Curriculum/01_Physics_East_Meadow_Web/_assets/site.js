/* Site-wide JS: progress bar, TOC scroll-spy, smooth-anchor offset.
 * Each lesson page imports this once. Lesson-specific interactives live inline.
 */

// --- Reading progress bar ---
(function () {
  const bar = document.querySelector(".progress-bar");
  if (!bar) return;
  const update = () => {
    const h = document.documentElement;
    const max = h.scrollHeight - h.clientHeight;
    const pct = max > 0 ? (h.scrollTop / max) * 100 : 0;
    bar.style.width = pct + "%";
  };
  document.addEventListener("scroll", update, { passive: true });
  update();
})();

// --- TOC scroll-spy ---
(function () {
  const tocLinks = document.querySelectorAll(".toc a[href^='#']");
  if (!tocLinks.length) return;
  const targets = Array.from(tocLinks).map(a => {
    const id = a.getAttribute("href").slice(1);
    return { link: a, target: document.getElementById(id) };
  }).filter(t => t.target);

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const match = targets.find(t => t.target === entry.target);
      if (!match) return;
      if (entry.isIntersecting) {
        tocLinks.forEach(l => l.classList.remove("active"));
        match.link.classList.add("active");
      }
    });
  }, { rootMargin: "-30% 0px -55% 0px", threshold: 0 });
  targets.forEach(t => observer.observe(t.target));
})();

// --- Helpers exported for lesson interactives ---
export function svgEl(tag, attrs = {}) {
  const el = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [k, v] of Object.entries(attrs)) {
    el.setAttribute(k, String(v));
  }
  return el;
}

export function bindSlider(sliderId, readoutId, formatter = v => v.toFixed(1)) {
  const slider = document.getElementById(sliderId);
  const readout = document.getElementById(readoutId);
  if (!slider || !readout) return null;
  const update = () => { readout.textContent = formatter(parseFloat(slider.value)); };
  slider.addEventListener("input", update);
  update();
  return slider;
}

export const G = 9.8;

export function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

export function lerp(a, b, t) { return a + (b - a) * t; }
