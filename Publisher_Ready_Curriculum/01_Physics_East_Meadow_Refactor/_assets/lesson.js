/* Lesson interactive helpers. Lessons may inline additional logic. */

/**
 * Bind a slider input to a target element's text content via a formatter.
 * @param {string} sliderId
 * @param {string} readoutId
 * @param {(value: number) => string} formatter
 * @returns {HTMLInputElement | null}
 */
export function bindSlider(sliderId, readoutId, formatter) {
  const slider = document.getElementById(sliderId);
  const readout = document.getElementById(readoutId);
  if (!slider || !readout) return null;
  const update = () => { readout.textContent = formatter(parseFloat(slider.value)); };
  slider.addEventListener("input", update);
  update();
  return slider;
}

/** Helper for SVG element creation with attributes. */
export function svgEl(tag, attrs = {}) {
  const el = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, String(v));
  return el;
}

/** Reveal a hidden hint element. */
export function revealHint(hintId) {
  const el = document.getElementById(hintId);
  if (el) el.hidden = false;
}
