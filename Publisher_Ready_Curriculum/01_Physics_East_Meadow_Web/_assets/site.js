/* Site-wide JS: progress bar, TOC scroll-spy, smooth-anchor offset, guided tour.
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

// ===========================================================
// Scroll-in animation triggers (lab-notebook redesign)
// Adds .in-view to .section and .lab elements when they enter
// the viewport. CSS keyframes (in site.css) animate them.
// Also flips body.anim-ready so the initial-hidden styles apply.
// Respects prefers-reduced-motion via the CSS gate.
// ===========================================================
(function () {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Mark the body as animation-ready *after* the page has had a chance
  // to paint, so the initial-hidden state doesn't FOUC.
  requestAnimationFrame(() => {
    document.body.classList.add("anim-ready");
  });

  if (reduce) {
    // Add .in-view to everything immediately so nothing stays hidden.
    document.querySelectorAll(".section, .lab").forEach(el => el.classList.add("in-view"));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in-view");
        observer.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.05 });

  document.querySelectorAll(".section, .lab").forEach(el => observer.observe(el));
})();

// =============================================================
// Guided Tour
// =============================================================
//
// Activates on `?tour=1` in the URL or when the user clicks any element with
// data-action="start-tour". Persists state in sessionStorage so the tour
// survives page navigation.
//
// To define the tour, edit TOUR_STEPS below. Each step is:
//   { page, selector, title, body, position? }
//
// `page` is a path relative to the site root (e.g., "/lessons/01-vectors.html").
// `selector` is matched on that page. `position` is "auto" (default), "top",
// "bottom", "left", or "right" — the tooltip's anchor relative to the target.

const TOUR_STEPS = [
  {
    page: "/",
    selector: ".hero h1",
    title: "Welcome to the Kinematics unit",
    body: "Nine phenomenon-based lessons aligned to NYSSLS HS-PS2-1, built for the joint East Meadow / Valley Stream Central pilot. This 2-minute tour will walk you through the highlights."
  },
  {
    page: "/",
    selector: ".lesson-grid",
    title: "Nine self-contained student lessons",
    body: "Each lesson is a single browser page with a unique hands-on interactive. Click any card to dive in. Let's open Vectors."
  },
  {
    page: "/lessons/01-vectors.html",
    selector: ".hero h1",
    title: "Lesson hero",
    body: "Every lesson opens with a hero — the unit/lesson context, a brief framing, and chips that tag today's pedagogy (here: Restorative Circle as the unit opener, plus Active Learning stations)."
  },
  {
    page: "/lessons/01-vectors.html",
    selector: "#investigate",
    title: "Drag-and-drop vector playground",
    body: "Click + Add vector to drop arrows on the grid, then drag the white tip handles to set magnitude and direction. Up to six vectors chain head-to-tail. The dashed black arrow is the resultant; live readouts on the right update as you drag."
  },
  {
    page: "/lessons/01-vectors.html",
    selector: ".toc",
    title: "Sticky table of contents",
    body: "Every lesson has a sticky TOC. The active section highlights as you scroll — students always know where they are in the lesson arc."
  },
  {
    page: "/lessons/04-acceleration.html",
    selector: "#investigate",
    title: "Three linked graphs",
    body: "Acceleration shows the same motion in three views — position-time, velocity-time, acceleration-time — drawing simultaneously as you slide the acceleration value. The leap from 'a is the slope of v-t' becomes visceral here."
  },
  {
    page: "/lessons/09-projectiles-at-an-angle.html",
    selector: "#investigate",
    title: "Target-shooting game",
    body: "The unit closes with a game: pick a launch speed and angle, fire, hit the target. Students discover that 30° and 60° give the same range — a felt experience of the symmetry around 45°."
  },
  {
    page: "/unit_plan.html",
    selector: "table",
    title: "Pacing calendar with strategy rotation",
    body: "Hochman literacy 3×, Active Learning 3×, BTC 2×, Restorative Circle 1× — distributed across the 2-week unit with a unit-opening circle and culminating design challenge."
  },
  {
    page: "/assessment.html",
    selector: "#stimulus",
    title: "Regents-style cluster assessment",
    body: "15 multiple choice + 1 four-part constructed response, aligned to HS-PS2-1. The full key is hidden under a click-to-reveal so you can use the page directly with students. That's the tour — explore freely."
  }
];

class Tour {
  constructor(steps) {
    this.steps = steps;
    this.current = parseInt(sessionStorage.getItem("tour:step") || "0", 10);
    this.active = sessionStorage.getItem("tour:active") === "1";
  }

  start() {
    this.active = true;
    this.current = 0;
    sessionStorage.setItem("tour:active", "1");
    sessionStorage.setItem("tour:step", "0");
    this.show();
  }

  end() {
    this.active = false;
    sessionStorage.removeItem("tour:active");
    sessionStorage.removeItem("tour:step");
    this.hidePanel();
  }

  navigate(idx) {
    const step = this.steps[idx];
    if (!step) return;
    sessionStorage.setItem("tour:step", String(idx));
    sessionStorage.setItem("tour:active", "1");
    if (this.matchesCurrentPage(step.page)) {
      this.current = idx;
      this.show();
    } else {
      const root = this.siteRoot();
      const dest = step.page === "/" ? root : root + step.page.replace(/^\//, "");
      window.location.href = dest;
    }
  }

  next() { this.hidePanel(); this.navigate(this.current + 1); }
  prev() { this.hidePanel(); this.navigate(this.current - 1); }

  // The site root is the directory containing index.html. The brand-lockup
  // anchor in the header always points to the index — relative ("index.html"
  // from root, "../index.html" from /lessons/) — so resolving that href gives
  // us a stable base, regardless of where on the site we currently are.
  siteRoot() {
    const a = document.querySelector(".brand-lockup");
    if (a && a.getAttribute("href")) {
      const indexUrl = new URL(a.getAttribute("href"), window.location.href);
      return new URL("./", indexUrl).href;
    }
    return new URL("./", window.location.href).href;
  }

  // Tour-relative path: where are we in the site, expressed like the manifest's
  // `page` field ("/", "/lessons/01-vectors.html", etc.).
  relativePath() {
    const root = this.siteRoot();
    const here = window.location.href.split("?")[0].split("#")[0];
    if (!here.startsWith(root)) return here; // safety — won't match anyway
    let rel = "/" + here.slice(root.length);
    if (rel.endsWith("/")) rel += "index.html";
    return rel;
  }

  matchesCurrentPage(page) {
    const here = this.relativePath();
    const target = page === "/" ? "/index.html" : page;
    return here === target;
  }

  show() {
    const step = this.steps[this.current];
    if (!step) { this.end(); return; }
    if (!this.matchesCurrentPage(step.page)) return;
    const target = document.querySelector(step.selector);
    if (!target) {
      // Element not on this page — wait briefly in case of late layout, then skip forward.
      setTimeout(() => {
        if (!document.querySelector(step.selector)) this.next();
      }, 600);
      return;
    }
    target.scrollIntoView({ behavior: "smooth", block: "center" });
    target.classList.add("tour-highlight");
    this.renderPanel(step);
  }

  renderPanel(step) {
    this.hidePanel(false); // keep highlight; only remove panel
    const panel = document.createElement("div");
    panel.id = "tour-panel";
    const isLast = this.current === this.steps.length - 1;
    panel.innerHTML = `
      <div class="tour-step-info">
        <span class="dot-row">${this.steps.map((_, i) => `<span class="dot${i === this.current ? " active" : ""}"></span>`).join("")}</span>
        <span>Step ${this.current + 1} of ${this.steps.length}</span>
      </div>
      <h4></h4>
      <p></p>
      <div class="tour-controls">
        <button class="tour-skip">Skip tour</button>
        <button class="tour-prev" ${this.current === 0 ? "disabled" : ""}>← Back</button>
        <button class="tour-next primary">${isLast ? "Finish" : "Next →"}</button>
      </div>
    `;
    panel.querySelector("h4").textContent = step.title;
    panel.querySelector("p").textContent = step.body;
    document.body.appendChild(panel);
    panel.querySelector(".tour-skip").onclick = () => this.end();
    panel.querySelector(".tour-prev").onclick = () => this.prev();
    panel.querySelector(".tour-next").onclick = () => isLast ? this.end() : this.next();
  }

  hidePanel(removeHighlight = true) {
    document.getElementById("tour-panel")?.remove();
    if (removeHighlight) {
      document.querySelectorAll(".tour-highlight").forEach(el => el.classList.remove("tour-highlight"));
    }
  }
}

(function () {
  const tour = new Tour(TOUR_STEPS);
  window.tour = tour;

  // Auto-start when ?tour=1 is in the URL
  const params = new URLSearchParams(window.location.search);
  if (params.get("tour") === "1") {
    sessionStorage.setItem("tour:active", "1");
    sessionStorage.setItem("tour:step", "0");
    // Strip the param so back/forward doesn't re-trigger
    params.delete("tour");
    const clean = window.location.pathname + (params.toString() ? "?" + params.toString() : "") + window.location.hash;
    window.history.replaceState({}, "", clean);
    tour.active = true;
    tour.current = 0;
  }

  // Click-to-start triggers
  document.addEventListener("click", (e) => {
    const trigger = e.target.closest("[data-action='start-tour']");
    if (trigger) {
      e.preventDefault();
      tour.start();
    }
  });

  // Resume if active
  if (tour.active) {
    setTimeout(() => tour.show(), 250);
  }
})();
