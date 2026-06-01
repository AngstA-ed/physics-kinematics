# Chemistry East Meadow Refactor — Unit 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the chemistry pilot — Unit 1 (Safety & Measurement), 8 phenomenon-based 5E lessons + Unit Plan — as brand-styled DOCX with rich visuals, using the same markdown→pandoc pipeline as the physics refactor.

**Architecture:** A new parallel track `Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/` holds markdown sources. The existing `tools/build_lessons.py` gains an additive `--root` flag so it can build any course tree; chemistry reuses the physics brand `reference.docx`. A new broad figure library `tools/figures_chem.py` (matplotlib, brand palette) plus a per-unit generator `tools/_gen_chem_unit01_figures.py` render PNGs that pandoc embeds. All documents conform to the existing `tools/lesson_schema.yaml` (no schema change).

**Tech Stack:** Python 3.14 (venv at `.venv/`), matplotlib (Agg), pandoc via `tools/pandoc_runner.py`, pytest. Markdown authored by hand; DOCX generated.

**Reference exemplar:** `Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/02_Forces/02_Newtons_Second_Law_and_Net_Force/` (Teacher_Guide.md, Student_Worksheet.md, Student_Notes.md, Answer_Key.md) — every chemistry document mirrors this voice, depth, and structure.

**Always run from project root with the venv active:** `source .venv/bin/activate`

---

## File Structure

| File | Responsibility |
|---|---|
| `tools/build_lessons.py` (modify) | Add `resolve_build_root()` helper + `--root` flag; build any course tree |
| `tools/figures_chem.py` (create) | Broad, reusable brand-styled chemistry figure builders |
| `tools/_gen_chem_unit01_figures.py` (create) | One-off generator: renders Unit 1's specific PNGs into each lesson's `figures/` |
| `tests/tools/test_build_root.py` (create) | Unit tests for `resolve_build_root()` |
| `tests/tools/test_figures_chem.py` (create) | Smoke test: every figure builder writes a non-empty PNG |
| `Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/_assets/brand/reference.docx` (create) | Copy of the physics brand reference |
| `Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/README.md` (create) | Authoring notes for the chem track |
| `…/01_Safety_and_Measurement/Unit_Plan.md` (create) | Unit plan |
| `…/01_Safety_and_Measurement/0N_<Lesson>/{Teacher_Guide,Student_Worksheet,Student_Notes,Answer_Key}.md` (create ×8) | The 8 lessons |

---

## Task 1: Add `--root` flag to the build pipeline

**Files:**
- Modify: `tools/build_lessons.py` (the `main()` function near line 196, and add a helper above it)
- Test: `tests/tools/test_build_root.py`

- [ ] **Step 1: Write the failing test**

Create `tests/tools/test_build_root.py`:

```python
from pathlib import Path
from tools.build_lessons import resolve_build_root, DEFAULT_REFACTOR


def test_default_root_uses_physics_refactor():
    root, ref = resolve_build_root(None, None)
    assert root == DEFAULT_REFACTOR.resolve()
    # physics brand reference exists in the repo
    assert ref is not None and ref.name == "reference.docx"


def test_custom_root_default_reference_under_that_root(tmp_path):
    brand = tmp_path / "_assets" / "brand"
    brand.mkdir(parents=True)
    (brand / "reference.docx").write_bytes(b"x")
    root, ref = resolve_build_root(str(tmp_path), None)
    assert root == tmp_path.resolve()
    assert ref == tmp_path / "_assets" / "brand" / "reference.docx"


def test_custom_root_missing_reference_returns_none(tmp_path):
    root, ref = resolve_build_root(str(tmp_path), None)
    assert root == tmp_path.resolve()
    assert ref is None


def test_explicit_reference_overrides(tmp_path):
    f = tmp_path / "myref.docx"
    f.write_bytes(b"x")
    root, ref = resolve_build_root(str(tmp_path), str(f))
    assert ref == f
```

- [ ] **Step 2: Run test to verify it fails**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_build_root.py -v`
Expected: FAIL — `ImportError: cannot import name 'resolve_build_root'`.

- [ ] **Step 3: Add the helper function**

In `tools/build_lessons.py`, add this function immediately after the `DEFAULT_REFERENCE` definition (around line 31):

```python
def resolve_build_root(root_arg: str | None, reference_arg: str | None):
    """Resolve the course refactor root and its brand reference doc.

    `root_arg` defaults to the physics refactor. When a custom root is given and
    no explicit `--reference` is passed, the reference defaults to
    `<root>/_assets/brand/reference.docx`. Returns (root: Path, reference: Path|None).
    """
    root = Path(root_arg).resolve() if root_arg else DEFAULT_REFACTOR.resolve()
    if reference_arg:
        ref = Path(reference_arg)
    else:
        ref = root / "_assets" / "brand" / "reference.docx"
    return root, (ref if ref.is_file() else None)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_build_root.py -v`
Expected: PASS (4 passed).

- [ ] **Step 5: Wire the helper into `main()` and add the `--root` flag**

Replace the body of `main()` from the `argparse` block through the target-resolution branch. The current code is:

```python
    p = argparse.ArgumentParser()
    p.add_argument("target", nargs="?", default="", help="Unit or lesson folder (relative to refactor root)")
    p.add_argument("--schema", default=str(ROOT / "tools" / "lesson_schema.yaml"))
    p.add_argument("--reference", default=str(DEFAULT_REFERENCE))
    args = p.parse_args()

    schema_path = Path(args.schema)
    reference = Path(args.reference) if Path(args.reference).is_file() else None

    if args.target:
        target = (DEFAULT_REFACTOR / args.target).resolve()
    else:
        target = DEFAULT_REFACTOR.resolve()

    if _is_lesson_folder(target):
        report = build_target(target, schema_path=schema_path, reference_doc=reference)
    elif target == DEFAULT_REFACTOR.resolve():
        report = {"built": [], "failed": []}
        for unit in sorted(target.iterdir()):
            if unit.is_dir() and unit.name.startswith(("0", "1")) and unit.name != "_assets":
                sub = build_target(unit, schema_path=schema_path, reference_doc=reference)
                report["built"] += sub["built"]
                report["failed"] += sub["failed"]
    else:
        report = build_target(target, schema_path=schema_path, reference_doc=reference)
```

Replace it with (changes: add `--root`, default `--reference` to `None`, use `resolve_build_root`, and use `refactor_root` instead of `DEFAULT_REFACTOR`):

```python
    p = argparse.ArgumentParser()
    p.add_argument("target", nargs="?", default="", help="Unit or lesson folder (relative to refactor root)")
    p.add_argument("--root", default=None, help="Course refactor root (default: physics)")
    p.add_argument("--schema", default=str(ROOT / "tools" / "lesson_schema.yaml"))
    p.add_argument("--reference", default=None)
    args = p.parse_args()

    schema_path = Path(args.schema)
    refactor_root, reference = resolve_build_root(args.root, args.reference)

    if args.target:
        target = (refactor_root / args.target).resolve()
    else:
        target = refactor_root.resolve()

    if _is_lesson_folder(target):
        report = build_target(target, schema_path=schema_path, reference_doc=reference)
    elif target == refactor_root.resolve():
        report = {"built": [], "failed": []}
        for unit in sorted(target.iterdir()):
            if unit.is_dir() and unit.name.startswith(("0", "1")) and unit.name != "_assets":
                sub = build_target(unit, schema_path=schema_path, reference_doc=reference)
                report["built"] += sub["built"]
                report["failed"] += sub["failed"]
    else:
        report = build_target(target, schema_path=schema_path, reference_doc=reference)
```

- [ ] **Step 6: Run the full existing suite to confirm no regression**

Run: `source .venv/bin/activate && python -m pytest tests/tools/ -q`
Expected: PASS — all prior tests plus the 4 new ones (34 total) green.

- [ ] **Step 7: Commit**

```bash
git add tools/build_lessons.py tests/tools/test_build_root.py
git commit -m "feat(tools): add --root flag so build_lessons can build any course tree

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 2: Scaffold the chemistry refactor track

**Files:**
- Create: `Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/_assets/brand/reference.docx` (copy)
- Create: `Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/README.md`
- Create: the eight empty lesson directories + `figures/` under `01_Safety_and_Measurement/`

- [ ] **Step 1: Create directories and copy the brand reference**

```bash
cd /Users/hoopie/Projects/Curricula
CHEM="Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor"
PHYS="Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor"
mkdir -p "$CHEM/_assets/brand"
cp "$PHYS/_assets/brand/reference.docx" "$CHEM/_assets/brand/reference.docx"
cp "$PHYS/_assets/brand/brand.css" "$CHEM/_assets/brand/brand.css"
cp "$PHYS/_assets/brand/em_logo.svg" "$CHEM/_assets/brand/em_logo.svg"
cp "$PHYS/_assets/brand/vs_logo.svg" "$CHEM/_assets/brand/vs_logo.svg"
for d in 01_Lab_Safety 02_Measurement_and_SI_Units 03_Significant_Figures_and_Scientific_Notation \
         04_Dimensional_Analysis 05_Density 06_Gram_Formula_Mass 07_Percent_Composition \
         08_Chemistry_Reference_Tables; do
  mkdir -p "$CHEM/01_Safety_and_Measurement/$d/figures"
done
ls -R "$CHEM" | head -40
```

Expected: the tree exists with `_assets/brand/reference.docx` and eight lesson folders each containing an empty `figures/`.

- [ ] **Step 2: Write the track README**

Create `Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/README.md`:

```markdown
# Chemistry — East Meadow Refactor

Phenomenon-based 5E rebuild of the Valley Stream / East Meadow Chemistry
curriculum, parallel to `01_Physics_East_Meadow_Refactor/`. Markdown sources are
built to brand-styled DOCX.

## Sources of truth
- Sequence & content: `../02_Chemistry/Valley_Stream_Chemistry_Scope_Sequence.docx`
- Instructional framework: `../02_Chemistry/Copy of 1. East Meadow Valley Stream Chem 5_6_26.pptx`
  (NYSSLS Lesson Observation Checklist, ABCs = Activity Before Content, ≤3 vocab
  in the 2nd half, OPTIC/CER literacy, Regents 60/40).

## Build
```
source .venv/bin/activate
python tools/_gen_chem_unit01_figures.py            # render figures
python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor 01_Safety_and_Measurement
```
Output: `Teacher_Guide.docx`, `Student_Worksheet.docx`, `Student_Notes.docx`,
`Answer_Key.docx` per lesson + `Unit_Plan.docx`. Build must report 0 failures.

## Status
- [x] Unit 1 — Safety & Measurement (pilot)
- [ ] Units 2–11 (future cycles)
```

- [ ] **Step 3: Commit**

```bash
git add Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor
git commit -m "scaffold(chem): chemistry refactor track + brand assets + Unit 1 dirs

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 3: Build the broad chemistry figure library

**Files:**
- Create: `tools/figures_chem.py`
- Test: `tests/tools/test_figures_chem.py`

- [ ] **Step 1: Write the failing smoke test**

Create `tests/tools/test_figures_chem.py`:

```python
from pathlib import Path
import tools.figures_chem as fc


def test_every_builder_writes_a_nonempty_png(tmp_path):
    calls = {
        "particle_model": lambda p: fc.particle_model(
            p, [("element", "single"), ("compound", "AB"), ("mixture", "A+B")]),
        "bohr_model": lambda p: fc.bohr_model(p, protons=6, neutrons=6, shells=[2, 4],
                                              label="Carbon-12"),
        "lewis_structure": lambda p: fc.lewis_structure(p, "O", valence=6),
        "classification_tree": lambda p: fc.classification_tree(p),
        "graduated_cylinder": lambda p: fc.graduated_cylinder(p, reading=36.5,
                                                              capacity=50),
        "dimensional_analysis_track": lambda p: fc.dimensional_analysis_track(
            p, [("2.5 mol", ""), ("6.02e23 atoms", "1 mol")]),
        "separation_apparatus": lambda p: fc.separation_apparatus(p, kind="filtration"),
        "reaction_energy_diagram": lambda p: fc.reaction_energy_diagram(
            p, reactant=30, product=10, activation=55, title="Exothermic"),
        "density_graph": lambda p: fc.density_graph(
            p, volumes=[1, 2, 3, 4], masses=[2.7, 5.4, 8.1, 10.8],
            substance="aluminum"),
        "heating_curve": lambda p: fc.heating_curve(p),
        "titration_curve": lambda p: fc.titration_curve(p),
        "periodic_trend": lambda p: fc.periodic_trend(
            p, elements=["Li", "Na", "K"], values=[152, 186, 227],
            ylabel="atomic radius (pm)", title="Radius increases down a group"),
        "composition_pie": lambda p: fc.composition_pie(
            p, parts=[("H", 11.2), ("O", 88.8)], title="Water (H2O)"),
    }
    for name, fn in calls.items():
        out = tmp_path / f"{name}.png"
        fn(out)
        assert out.exists(), f"{name} did not write a file"
        assert out.stat().st_size > 1000, f"{name} wrote a suspiciously small file"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_figures_chem.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'tools.figures_chem'`.

- [ ] **Step 3: Write `tools/figures_chem.py`**

Create `tools/figures_chem.py` with the full content below. It reuses the brand palette and `_save`/`_prep` from `tools/figures.py`.

```python
"""Reusable, brand-styled chemistry figure builders for East Meadow lessons.

Mirrors tools/figures.py (physics). Same palette, 150 dpi, deterministic
(no Date.now / random). Markdown references the PNGs with a relative path
(`![alt](figures/name.png)`); pandoc embeds them into the DOCX.
"""
from __future__ import annotations
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, FancyBboxPatch

from tools.figures import (
    PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, SERIES, line_graph, bar_chart,
    _prep, _save,
)


# --- Models ----------------------------------------------------------------
def particle_model(path, panels, *, title="", figsize=(7.5, 2.8)) -> str:
    """Side-by-side particle panels. `panels` is a list of (label, kind) where
    kind is 'single' (one element, identical atoms), 'AB' (compound, bonded
    pairs), or 'A+B' (mixture, two separate atom types unbonded)."""
    fig, axes = plt.subplots(1, len(panels), figsize=figsize)
    if len(panels) == 1:
        axes = [axes]
    rng = np.linspace(0.2, 0.8, 3)
    for ax, (label, kind) in zip(axes, panels):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(label, fontsize=11, fontweight="bold")
        pts = [(x, y) for y in rng for x in rng]
        if kind == "single":
            for (x, y) in pts:
                ax.add_patch(Circle((x, y), 0.07, facecolor=PURPLE, edgecolor=INK))
        elif kind == "AB":
            for (x, y) in pts:
                ax.add_patch(Circle((x - 0.05, y), 0.06, facecolor=PURPLE, edgecolor=INK, zorder=3))
                ax.add_patch(Circle((x + 0.05, y), 0.045, facecolor=BLUE, edgecolor=INK, zorder=3))
                ax.plot([x - 0.05, x + 0.05], [y, y], color=INK, linewidth=1.2, zorder=2)
        elif kind == "A+B":
            for i, (x, y) in enumerate(pts):
                c = PURPLE if i % 2 == 0 else BLUE
                r = 0.07 if i % 2 == 0 else 0.05
                ax.add_patch(Circle((x, y), r, facecolor=c, edgecolor=INK))
    if title:
        fig.suptitle(title, fontsize=12, fontweight="bold")
    return _save(fig, path)


def bohr_model(path, *, protons, neutrons, shells, label="", figsize=(4.2, 4.2)) -> str:
    """Bohr model: nucleus (p+/n0 count) ringed by electron shells.
    `shells` is a list of electron counts per shell, innermost first."""
    fig, ax = plt.subplots(figsize=figsize)
    n = len(shells)
    lim = n + 1.2
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_aspect("equal"); ax.axis("off")
    if label:
        ax.set_title(label, fontsize=12, fontweight="bold")
    ax.add_patch(Circle((0, 0), 0.55, facecolor=PURPLE, edgecolor=INK, zorder=4))
    ax.text(0, 0, f"{protons}p\n{neutrons}n", ha="center", va="center",
            color="white", fontsize=9, fontweight="bold", zorder=5)
    for i, count in enumerate(shells, start=1):
        ax.add_patch(Circle((0, 0), i, fill=False, edgecolor=GRID, linewidth=1.2, zorder=1))
        for k in range(count):
            ang = 2 * np.pi * k / count + (0.3 * i)
            ax.add_patch(Circle((i * np.cos(ang), i * np.sin(ang)), 0.13,
                         facecolor=BLUE, edgecolor=INK, zorder=3))
    return _save(fig, path)


def lewis_structure(path, symbol, *, valence, figsize=(2.6, 2.6)) -> str:
    """Lewis electron-dot symbol: element symbol with `valence` dots placed on
    the four sides (paired after the first four)."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_aspect("equal"); ax.axis("off")
    ax.text(0, 0, symbol, ha="center", va="center", fontsize=30, fontweight="bold", color=INK)
    # side slots: (dx, dy) for first electron on each side, then the pairing offset
    sides = [((0, 0.6), (0.18, 0)), ((0, -0.6), (0.18, 0)),
             ((-0.6, 0), (0, 0.18)), ((0.6, 0), (0, 0.18))]
    placed = 0
    for first, off in sides:
        if placed >= valence:
            break
        ax.add_patch(Circle(first, 0.06, facecolor=INK))
        placed += 1
    # second pass: pair up remaining electrons
    for first, off in sides:
        if placed >= valence:
            break
        ax.add_patch(Circle((first[0] + off[0], first[1] + off[1]), 0.06, facecolor=INK))
        placed += 1
    return _save(fig, path)


# --- Diagrams --------------------------------------------------------------
def classification_tree(path, *, figsize=(7.2, 4.6)) -> str:
    """Flowchart classifying matter: Matter → (Pure Substances → Elements,
    Compounds) and (Mixtures → Homogeneous, Heterogeneous)."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")

    def box(x, y, text, color=PURPLE):
        ax.add_patch(FancyBboxPatch((x - 1.1, y - 0.4), 2.2, 0.8,
                     boxstyle="round,pad=0.05", facecolor=color, edgecolor=INK, alpha=0.9))
        ax.text(x, y, text, ha="center", va="center", color="white",
                fontsize=9, fontweight="bold")

    def link(x1, y1, x2, y2):
        ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                     mutation_scale=14, color=INK, linewidth=1.4))

    box(6, 7.2, "MATTER")
    box(3, 5.2, "Pure Substances", BLUE); box(9, 5.2, "Mixtures", ACCENT2)
    box(1.5, 3.0, "Elements", BLUE); box(4.5, 3.0, "Compounds", BLUE)
    box(7.5, 3.0, "Homogeneous", ACCENT2); box(10.5, 3.0, "Heterogeneous", ACCENT2)
    for (x2, y2) in [(3, 5.6), (9, 5.6)]:
        link(6, 6.8, x2, y2)
    link(3, 4.8, 1.5, 3.4); link(3, 4.8, 4.5, 3.4)
    link(9, 4.8, 7.5, 3.4); link(9, 4.8, 10.5, 3.4)
    ax.text(1.5, 2.0, "(one atom\ntype)", ha="center", fontsize=8, color=INK)
    ax.text(4.5, 2.0, "(2+ atoms\nbonded)", ha="center", fontsize=8, color=INK)
    ax.text(7.5, 2.0, "(uniform,\ne.g. saltwater)", ha="center", fontsize=8, color=INK)
    ax.text(10.5, 2.0, "(non-uniform,\ne.g. trail mix)", ha="center", fontsize=8, color=INK)
    return _save(fig, path)


def graduated_cylinder(path, *, reading, capacity, figsize=(2.6, 4.6)) -> str:
    """A graduated cylinder filled to `reading` (of `capacity`), drawn with a
    concave meniscus and tick marks — read at the bottom of the meniscus."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 4); ax.set_ylim(-0.5, 11); ax.axis("off")
    ax.add_patch(Rectangle((1, 0), 2, 10, fill=False, edgecolor=INK, linewidth=1.8))
    frac = reading / capacity
    h = 10 * frac
    ax.add_patch(Rectangle((1, 0), 2, h, facecolor=BLUE, alpha=0.45, edgecolor="none"))
    # concave meniscus
    xs = np.linspace(1, 3, 50)
    ax.plot(xs, h + 0.18 * np.sin(np.pi * (xs - 1) / 2) ** 2 * 0 - 0.18 *
            (1 - ((xs - 2) / 1) ** 2), color=BLUE, linewidth=2)
    for i in range(11):
        y = i
        ax.plot([2.8, 3], [y, y], color=INK, linewidth=1)
        ax.text(3.15, y, f"{int(capacity * i / 10)}", va="center", fontsize=7, color=INK)
    ax.annotate(f"read here\n{reading} mL", xy=(2, h - 0.18), xytext=(3.4, h + 1.4),
                fontsize=8, color=PURPLE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=PURPLE))
    ax.text(2, 10.5, "mL", ha="center", fontsize=9, fontweight="bold", color=INK)
    return _save(fig, path)


def dimensional_analysis_track(path, steps, *, title="", figsize=(7.5, 2.2)) -> str:
    """Factor-label 'railroad track' diagram. `steps` is a list of
    (numerator, denominator) string pairs; the first denominator is usually ''."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, len(steps) * 3 + 0.5); ax.set_ylim(0, 3); ax.axis("off")
    if title:
        ax.set_title(title, fontsize=11, fontweight="bold")
    ax.plot([0.2, len(steps) * 3 + 0.3], [1.5, 1.5], color=INK, linewidth=1.6)
    for i, (num, den) in enumerate(steps):
        cx = i * 3 + 1.5
        if i > 0:
            ax.plot([cx - 1.5, cx - 1.5], [0.5, 2.5], color=INK, linewidth=1.6)
        ax.text(cx, 2.05, num, ha="center", va="center", fontsize=10,
                color=PURPLE, fontweight="bold")
        if den:
            ax.text(cx, 0.95, den, ha="center", va="center", fontsize=10,
                    color=BLUE, fontweight="bold")
        ax.add_patch(FancyArrowPatch((cx + 1.3, 1.5), (cx + 1.55, 1.5),
                     arrowstyle="-|>", mutation_scale=10, color=INK)) if i < len(steps) - 1 else None
    return _save(fig, path)


def separation_apparatus(path, *, kind, figsize=(4.4, 4.0)) -> str:
    """Schematic of a separation setup. `kind` in {'filtration','distillation',
    'chromatography'}."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(kind.capitalize(), fontsize=12, fontweight="bold")
    if kind == "filtration":
        ax.add_patch(plt.Polygon([(3, 7), (7, 7), (5, 4)], closed=True,
                     fill=False, edgecolor=INK, linewidth=1.8))   # funnel
        ax.plot([5, 5], [4, 3], color=INK, linewidth=1.5)
        ax.add_patch(Rectangle((3.4, 0.5), 3.2, 2.3, fill=False, edgecolor=INK, linewidth=1.8))
        ax.add_patch(Rectangle((3.4, 0.5), 3.2, 1.0, facecolor=BLUE, alpha=0.4, edgecolor="none"))
        ax.text(5, 7.6, "residue (solid) stays in paper", ha="center", fontsize=8, color=PURPLE)
        ax.text(5, 0.1, "filtrate (liquid)", ha="center", fontsize=8, color=BLUE)
    elif kind == "distillation":
        ax.add_patch(Circle((2.4, 2.6), 1.3, fill=False, edgecolor=INK, linewidth=1.8))
        ax.add_patch(Circle((2.4, 2.6), 1.3, facecolor=BLUE, alpha=0.35, edgecolor="none"))
        ax.plot([2.4, 2.4], [3.9, 6], color=INK, linewidth=1.6)
        ax.plot([2.4, 8], [6, 4.2], color=INK, linewidth=1.6)           # condenser
        ax.add_patch(Circle((8.4, 3.4), 1.0, fill=False, edgecolor=INK, linewidth=1.8))
        ax.text(2.4, 0.8, "mixture (heat)", ha="center", fontsize=8, color=PURPLE)
        ax.text(8.4, 1.9, "pure distillate", ha="center", fontsize=8, color=BLUE)
    elif kind == "chromatography":
        ax.add_patch(Rectangle((4, 1), 2, 8, fill=False, edgecolor=INK, linewidth=1.8))
        ax.plot([4, 6], [2, 2], color=INK, linewidth=1, linestyle="--")  # origin line
        for i, (cy, c) in enumerate([(3.2, PURPLE), (5.0, BLUE), (6.6, ACCENT2)]):
            ax.add_patch(Circle((5, cy), 0.28, facecolor=c, edgecolor="none"))
        ax.text(5, 0.4, "solvent rises, dyes separate", ha="center", fontsize=8, color=INK)
    return _save(fig, path)


def reaction_energy_diagram(path, *, reactant, product, activation, title="",
                            figsize=(5.0, 3.6)) -> str:
    """Reaction-coordinate diagram with an activation-energy hump."""
    fig, ax = plt.subplots(figsize=figsize)
    peak = max(reactant, product) + activation
    xs = np.linspace(0, 10, 200)
    ys = np.piecewise(
        xs,
        [xs < 3, (xs >= 3) & (xs <= 7), xs > 7],
        [lambda x: reactant + 0 * x,
         lambda x: reactant + (peak - reactant) * np.sin(np.pi * (x - 3) / 8) ** 2,
         lambda x: product + 0 * x])
    ax.plot(xs, ys, color=PURPLE, linewidth=2.6)
    ax.axhline(reactant, color=GRID, linewidth=0.8); ax.axhline(product, color=GRID, linewidth=0.8)
    ax.annotate("", xy=(3, peak), xytext=(3, reactant),
                arrowprops=dict(arrowstyle="<->", color=ACCENT2))
    ax.text(3.2, (peak + reactant) / 2, "activation\nenergy", color=ACCENT2, fontsize=9)
    ax.text(0.3, reactant, "reactants", color=INK, fontsize=9, va="bottom")
    ax.text(9.7, product, "products", color=INK, fontsize=9, va="bottom", ha="right")
    ax.set_xlabel("reaction progress"); ax.set_ylabel("energy (kJ)")
    if title:
        ax.set_title(title)
    ax.set_xticks([])
    return _save(fig, path)


# --- Graphs ----------------------------------------------------------------
def density_graph(path, *, volumes, masses, substance="", figsize=(5.0, 3.6)) -> str:
    """Mass vs. volume scatter + best-fit line; slope = density (annotated)."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(volumes, masses, color=PURPLE, zorder=3, s=36)
    m = masses[-1] / volumes[-1] if volumes[-1] else 0
    xs = np.linspace(0, max(volumes) * 1.05, 50)
    ax.plot(xs, m * xs, color=BLUE, linewidth=2.2,
            label=f"slope = density = {m:.2f} g/mL")
    ax.set_xlabel("volume (mL)"); ax.set_ylabel("mass (g)")
    ax.set_title(f"Mass vs. Volume{' — ' + substance if substance else ''}")
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.legend(frameon=False, fontsize=9)
    return _save(fig, path)


def heating_curve(path, *, substance="water", figsize=(5.4, 3.6)) -> str:
    """Temperature-vs-time heating curve with melting and boiling plateaus."""
    t = [0, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8]
    temp = [-20, -10, 0, 0, 25, 60, 90, 100, 100, 110, 120]
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(t, temp, color=PURPLE, linewidth=2.6)
    ax.axhline(0, color=GRID, linewidth=0.8); ax.axhline(100, color=GRID, linewidth=0.8)
    ax.text(2, 6, "melting (solid+liquid)", fontsize=8, color=BLUE)
    ax.text(6, 106, "boiling (liquid+gas)", fontsize=8, color=ACCENT2)
    ax.set_xlabel("time / heat added"); ax.set_ylabel("temperature (°C)")
    ax.set_title(f"Heating Curve of {substance}")
    ax.grid(True, color=GRID, linewidth=0.6)
    return _save(fig, path)


def titration_curve(path, *, figsize=(5.0, 3.6)) -> str:
    """Strong acid–strong base titration curve (pH vs. volume of base)."""
    v = np.linspace(0, 50, 200)
    ph = 1 + 13 / (1 + np.exp(-(v - 25) * 0.8))
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(v, ph, color=PURPLE, linewidth=2.6)
    ax.axhline(7, color=GRID, linewidth=0.8)
    ax.axvline(25, color=ACCENT2, linewidth=1.2, linestyle="--")
    ax.text(26, 3, "equivalence\npoint", fontsize=8, color=ACCENT2)
    ax.set_xlabel("volume of base added (mL)"); ax.set_ylabel("pH")
    ax.set_title("Titration Curve")
    ax.grid(True, color=GRID, linewidth=0.6)
    return _save(fig, path)


def periodic_trend(path, *, elements, values, ylabel="", title="", figsize=(5.0, 3.4)) -> str:
    """Thin wrapper over line_graph for periodic-trend plots (radius, IE, EN)."""
    xs = list(range(len(elements)))
    out = line_graph(path, [("", xs, values)], xlabel="", ylabel=ylabel,
                     title=title, markers=True)
    return out


def composition_pie(path, parts, *, title="", figsize=(4.2, 4.2)) -> str:
    """Percent-by-mass pie chart. `parts` is a list of (label, percent)."""
    labels = [f"{l} ({p:.1f}%)" for l, p in parts]
    sizes = [p for _, p in parts]
    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(sizes, labels=labels, colors=SERIES[:len(parts)],
           textprops={"fontsize": 9, "color": INK},
           wedgeprops={"edgecolor": "white", "linewidth": 1.5})
    ax.set_aspect("equal")
    if title:
        ax.set_title(title, fontweight="bold")
    return _save(fig, path)


if __name__ == "__main__":
    import tempfile, os
    d = tempfile.mkdtemp()
    particle_model(os.path.join(d, "pm.png"),
                   [("element", "single"), ("compound", "AB"), ("mixture", "A+B")])
    print("smoke render ok:", d)
```

- [ ] **Step 4: Run the smoke test to verify it passes**

Run: `source .venv/bin/activate && python -m pytest tests/tools/test_figures_chem.py -v`
Expected: PASS — `test_every_builder_writes_a_nonempty_png` green. If a builder raises, fix that builder until the test passes.

- [ ] **Step 5: Commit**

```bash
git add tools/figures_chem.py tests/tools/test_figures_chem.py
git commit -m "feat(tools): broad brand-styled chemistry figure library + smoke test

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Task 4: Per-unit figure generator for Unit 1

**Files:**
- Create: `tools/_gen_chem_unit01_figures.py`

This renders the specific PNG instances each lesson references, into each lesson's `figures/` folder. Custom one-off diagrams that aren't general enough for the library (lab-safety equipment panel, accuracy/precision targets, ice-vs-water particle spacing) live here, exactly as `_gen_forces_figures.py` holds physics one-offs.

- [ ] **Step 1: Write the generator**

Create `tools/_gen_chem_unit01_figures.py`:

```python
"""One-off generator: figures for Chemistry Unit 1 (Safety & Measurement).

Run from project root with the venv active:
    python tools/_gen_chem_unit01_figures.py
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

from tools.figures import PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, _save, bar_chart
from tools.figures_chem import (
    particle_model, classification_tree, graduated_cylinder,
    dimensional_analysis_track, density_graph, composition_pie,
)

UNIT = Path("Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/01_Safety_and_Measurement")


def fig_dir(lesson: str) -> Path:
    d = UNIT / lesson / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


# --- Custom one-offs not in the shared library -----------------------------
def lab_safety_panel(path):
    """Labeled panel of core lab-safety equipment."""
    fig, ax = plt.subplots(figsize=(7.5, 2.6))
    ax.set_xlim(0, 5); ax.set_ylim(0, 2); ax.axis("off")
    ax.set_title("Know your safety equipment", fontsize=12, fontweight="bold")
    items = ["goggles", "apron", "eyewash\nstation", "fire\nextinguisher", "fume\nhood"]
    for i, name in enumerate(items):
        x = i + 0.5
        ax.add_patch(Rectangle((x - 0.38, 0.6), 0.76, 0.8, facecolor=SERIES_SAFE(i),
                     edgecolor=INK, alpha=0.85))
        ax.text(x, 1.0, str(i + 1), ha="center", va="center", color="white",
                fontsize=14, fontweight="bold")
        ax.text(x, 0.35, name, ha="center", va="center", fontsize=8, color=INK)
    return _save(fig, path)


def SERIES_SAFE(i):
    return [PURPLE, BLUE, ACCENT2, GREEN, "#c0392b"][i % 5]


def accuracy_precision_targets(path):
    """Three dartboard targets: accurate+precise, precise-not-accurate,
    neither — the classic measurement contrast."""
    fig, axes = plt.subplots(1, 3, figsize=(7.5, 2.8))
    titles = ["accurate &\nprecise", "precise,\nnot accurate", "neither"]
    clusters = [
        [(0, 0), (0.1, 0.05), (-0.05, 0.1), (0.05, -0.08)],
        [(0.55, 0.5), (0.6, 0.55), (0.5, 0.6), (0.58, 0.48)],
        [(0.4, -0.3), (-0.5, 0.2), (0.1, 0.6), (-0.3, -0.5)],
    ]
    for ax, title, pts in zip(axes, titles, clusters):
        ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=10, fontweight="bold")
        for r, c in [(0.9, GRID), (0.6, "white"), (0.3, GRID), (0.12, ACCENT2)]:
            ax.add_patch(Circle((0, 0), r, facecolor=c, edgecolor=INK, linewidth=0.8, zorder=1))
        for (x, y) in pts:
            ax.add_patch(Circle((x, y), 0.06, facecolor=PURPLE, edgecolor=INK, zorder=4))
    return _save(fig, path)


def ice_vs_water_particles(path):
    """Particle spacing: open hexagonal ice lattice (less dense) vs. close-packed
    liquid water — why ice floats."""
    fig, axes = plt.subplots(1, 2, figsize=(6.5, 3.2))
    for ax, (title, openness) in zip(axes, [("ice (solid)", 0.34), ("water (liquid)", 0.22)]):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=11, fontweight="bold")
        ys = np.arange(0.15, 0.95, openness)
        xs = np.arange(0.15, 0.95, openness)
        for j, y in enumerate(ys):
            for x in xs:
                ox = (openness / 2) if j % 2 else 0
                ax.add_patch(Circle((x + ox, y), 0.05, facecolor=BLUE, edgecolor=INK))
    fig.suptitle("Ice is LESS dense than water (open lattice)", fontsize=11, fontweight="bold")
    return _save(fig, path)


def build_all():
    # L01 Lab Safety
    lab_safety_panel(fig_dir("01_Lab_Safety") / "safety_equipment.png")
    # L02 Measurement
    graduated_cylinder(fig_dir("02_Measurement_and_SI_Units") / "graduated_cylinder.png",
                       reading=36.5, capacity=50)
    accuracy_precision_targets(fig_dir("02_Measurement_and_SI_Units") / "accuracy_precision.png")
    # L03 Sig Figs
    graduated_cylinder(fig_dir("03_Significant_Figures_and_Scientific_Notation") / "reading_precision.png",
                       reading=27.5, capacity=50)
    # L04 Dimensional Analysis
    dimensional_analysis_track(
        fig_dir("04_Dimensional_Analysis") / "atoms_to_moles.png",
        [("2.5 mol Cu", ""), ("6.02×10²³ atoms", "1 mol")],
        title="Converting moles → atoms")
    # L05 Density
    density_graph(fig_dir("05_Density") / "density_graph.png",
                  volumes=[1, 2, 3, 4, 5], masses=[2.7, 5.4, 8.1, 10.8, 13.5],
                  substance="aluminum")
    ice_vs_water_particles(fig_dir("05_Density") / "ice_vs_water.png")
    # L06 Gram Formula Mass
    bar_chart(fig_dir("06_Gram_Formula_Mass") / "molar_masses.png",
              ["H₂O", "CO₂", "NaCl", "C₆H₁₂O₆"], [18, 44, 58.5, 180],
              ylabel="gram formula mass (g/mol)", title="Mass of one mole")
    # L07 Percent Composition
    composition_pie(fig_dir("07_Percent_Composition") / "water_composition.png",
                    parts=[("H", 11.2), ("O", 88.8)], title="Percent by mass — water (H₂O)")
    # L08 Reference Tables
    classification_tree(fig_dir("08_Chemistry_Reference_Tables") / "matter_map.png")


if __name__ == "__main__":
    build_all()
    print("Unit 1 figures rendered.")
```

- [ ] **Step 2: Run the generator**

Run: `source .venv/bin/activate && python tools/_gen_chem_unit01_figures.py`
Expected: prints `Unit 1 figures rendered.` and each lesson's `figures/` now holds its PNG(s). If a NameError/import error appears, fix it (note: `SERIES_SAFE` is defined in this file; `bar_chart` is imported from `tools.figures`).

- [ ] **Step 3: Verify the PNGs exist**

```bash
find Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/01_Safety_and_Measurement -name '*.png' | sort
```
Expected: 10 PNGs across the eight lesson folders.

- [ ] **Step 4: Commit**

```bash
git add tools/_gen_chem_unit01_figures.py Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/01_Safety_and_Measurement
git commit -m "feat(chem): Unit 1 figure generator + rendered PNGs

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

## Shared lesson document skeletons (used by Tasks 5–12)

Every lesson authors four markdown files. The skeletons below are the **exact
heading structure** the schema validates (`tools/lesson_schema.yaml`). The
executor fills each section with full 5E prose **matching the depth and voice of
the Forces exemplar** at
`…/01_Physics_East_Meadow_Refactor/02_Forces/02_Newtons_Second_Law_and_Net_Force/`.
Per-lesson facts (phenomenon, vocab, figures, numbers, exit ticket + answers)
come from the lesson's brief in its task. Do **not** leave any blank — these are
finished classroom documents.

**`Teacher_Guide.md` headings (14, in order):**
```
# <Lesson Title> — Teacher Guide
## Cover
## Curated Resources (from East Meadow Scope & Sequence)
### NYSSLS Standards
### Phenomenon
### Javalab / Labs
### Assessments
## Lesson Overview            (table: Duration, NYSSLS link, CCC focus, Strategy chips, Materials, Safety, Prior knowledge; then "Lesson objectives — students can:")
## Phase 1 · Engage *(0 – 10 min)*
## Phase 2 · Explore *(10 – 30 min)*
## Phase 3 · Explain *(30 – 36 min)*
## Phase 4 · Elaborate *(36 – 40 min)*
## Phase 5 · Evaluate *(40 – 42 min)*
## Common Misconceptions
## Access & Differentiation   (ELL/ENL, IEP/SPED, Extensions)
## Strategy Spotlight
## NYSSLS Observation Checklist Crosswalk   (table mapping all 8 checklist items → where they appear)
## Companion Materials
## Key Vocabulary (max 3)
```
Phases include minute-by-minute sub-headings, **sample teacher language** (block-quotes), and **anticipated student responses**, and must embed the lesson's figure(s) with descriptive alt text. ABCs: Explore (activity) precedes Explain (content). Vocabulary (≤3) is introduced in Phase 3 (second half).

**`Student_Worksheet.md` headings (8):** `## Phenomenon`, `## Notice & Wonder`, `## Initial Model`, `## Investigation`, `## Make It Make Sense`, `## Vocabulary in Action`, `## Revise Your Model`, `## Exit Ticket`. Opens with the title block + `Name / Date / Period` line. No answers. Embed the figure(s).

**`Student_Notes.md` headings (5):** `## Learning Targets`, `## Key Vocabulary`, `## Guided Notes`, `## Worked Example`, `## Summary`. Opens with title block + Name/Date/Period. Guided Notes use fill-in-the-blank cloze. Embed the figure(s).

**`Answer_Key.md` headings (4):** `## Cover`, `## Make-It-Make-Sense Answers`, `## Exit Ticket Answer`, `## Closing Reflection (rubric)`. Each Make-It-Make-Sense and Exit Ticket answer carries a rubric note and the NYSSLS code.

**The NYSSLS Observation Checklist Crosswalk table** (same 8 rows in every lesson; fill the "Where it appears" column per lesson):

| # | Checklist item | Where it appears in this lesson |
|---|---|---|
| 1 | Local/relatable phenomenon | |
| 2 | Turn and Talk (2–3×) | |
| 3 | Students develop questions/models/procedures | |
| 4 | CCC defined and used | |
| 5 | ENL — ≤ 3 vocab, second half | |
| 6 | Revisit phenomenon with evidence | |
| 7 | ENL/SPED supports | |
| 8 | Assessment check | |

**Per-lesson verification (run after authoring each lesson's four files):**

```bash
source .venv/bin/activate
python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor 01_Safety_and_Measurement/<NN_Folder>
```
Expected: `Built 4 artifacts` and **no** "FAILED" line. If a validation error prints (e.g. missing heading, >3 vocab, MC answer bolded), fix the markdown and rebuild until clean. Then commit that lesson.

---

## Task 5: Lesson 01 — Lab Safety

**Files (create):** `…/01_Safety_and_Measurement/01_Lab_Safety/{Teacher_Guide,Student_Worksheet,Student_Notes,Answer_Key}.md`

**Brief:**
- **Title:** Lab Safety & Working Like a Scientist
- **Phenomenon:** A short news clip / story of a school-lab accident caused by skipped safety steps (goggles off, wrong glove, no fume hood) vs. the same procedure done safely. *Driving question:* What routines let chemists work with dangerous substances and stay safe?
- **NYSSLS Standards heading text:** "Foundational lab-safety and SEP practice (Planning & Carrying Out Investigations). No content PE — establishes the safe-investigation routines every later HS-PS1 lab depends on."
- **CCC focus:** Cause and Effect (unsafe action → predictable hazard; control → prevention).
- **Strategy chip:** RESTORATIVE CIRCLE (unit-opening circle: "a time I had to be careful").
- **Materials:** safety contract, goggles/apron, SDS sample, room safety-equipment map.
- **Vocabulary (≤3):** **SDS (Safety Data Sheet)**, **PPE (personal protective equipment)**, **hazard**.
- **Figure:** `figures/safety_equipment.png` (embed in Teacher Guide + Worksheet).
- **Investigation:** safety-equipment scavenger hunt (locate & state the purpose of each item) + SDS interpretation (find the hazard + first-aid line for a common reagent).
- **Make It Make Sense:** 3 scenarios — student names the missing PPE / hazard / correct response.
- **Exit Ticket:** Given a lab scenario (heating a liquid that can splash), (a) name two pieces of PPE required and why, (b) cite where you'd find its hazards (SDS), (c) one sentence: why the routine matters. **Answers:** (a) goggles (eye splash) + apron (skin/clothes); (b) the SDS; (c) routines make the cause-effect of hazards predictable and preventable.

- [ ] **Step 1:** Author `Teacher_Guide.md` per the skeleton + brief (full 5E prose, crosswalk filled, embed `safety_equipment.png`).
- [ ] **Step 2:** Author `Student_Worksheet.md` (8 sections; scavenger-hunt + SDS table; embed figure).
- [ ] **Step 3:** Author `Student_Notes.md` (Learning Targets, the 3 vocab, cloze Guided Notes, a worked "read-the-SDS" example, Summary).
- [ ] **Step 4:** Author `Answer_Key.md` (4 sections, rubrics, NYSSLS tag = "SEP-3 / foundational").
- [ ] **Step 5:** Build & verify:
  `python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor 01_Safety_and_Measurement/01_Lab_Safety` → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit: `git add … && git commit -m "feat(chem): Unit 1 Lesson 01 — Lab Safety (5E DOCX-only)"` (with Co-Authored-By trailer).

---

## Task 6: Lesson 02 — Measurement & SI Units

**Files (create):** `…/02_Measurement_and_SI_Units/{Teacher_Guide,Student_Worksheet,Student_Notes,Answer_Key}.md`

**Brief:**
- **Phenomenon:** The 1999 Mars Climate Orbiter loss (pounds vs. newtons) — a $125M spacecraft lost to a unit mismatch. *Driving question:* Why does the whole world's science agree on one set of units?
- **NYSSLS:** HS-PS1-7 (mathematical representations — numerical/graphical quantitative information).
- **CCC focus:** Scale, Proportion, and Quantity.
- **Strategy chip:** ACTIVE LEARNING (measurement stations).
- **Materials:** graduated cylinders, triple-beam balance, thermometer, ruler, assorted objects.
- **Vocabulary (≤3):** **SI unit**, **precision**, **accuracy**.
- **Figures:** `figures/graduated_cylinder.png` (read to the meniscus) + `figures/accuracy_precision.png` (dartboard targets). Embed both.
- **Investigation:** measurement stations — read a graduated cylinder (meniscus), mass on a balance, temperature; record with correct units; compare repeated trials to discuss precision vs. accuracy.
- **Make It Make Sense:** identify the SI unit + instrument for mass/volume/length/temperature; classify two data sets as precise/accurate/both/neither.
- **Exit Ticket:** A student measures a liquid four times: 24.9, 25.0, 24.8, 25.1 mL (true value 30.0 mL). (a) Precise? (b) Accurate? (c) one sentence why. **Answers:** (a) yes — values cluster tightly; (b) no — far from 30.0; (c) precision = agreement among trials, accuracy = closeness to true value.

- [ ] **Step 1–4:** Author the four documents per skeleton + brief (embed both figures in Teacher Guide & Worksheet; OPTIC callout on reading the dartboard figure in Strategy Spotlight).
- [ ] **Step 5:** Build & verify (`… 01_Safety_and_Measurement/02_Measurement_and_SI_Units`) → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit `feat(chem): Unit 1 Lesson 02 — Measurement & SI Units`.

---

## Task 7: Lesson 03 — Significant Figures & Scientific Notation

**Files (create):** `…/03_Significant_Figures_and_Scientific_Notation/{…}.md`

**Brief:**
- **Phenomenon:** Two students measure the same pencil and report 15 cm vs. 15.0 cm vs. 15.00 cm — a calculator says a derived answer is 15.2837 cm. *Driving question:* How precise are we *allowed* to claim our answer is?
- **NYSSLS:** Foundational quantitative skill → supports HS-PS1-7. (Slide 12: "No math operation for sig figs — round to three.")
- **CCC focus:** Scale, Proportion, and Quantity.
- **Strategy chip:** BTC (random groups, vertical surfaces, sig-fig thin-slice).
- **Vocabulary (≤3):** **significant figures**, **scientific notation**, **precision**.
- **Figure:** `figures/reading_precision.png` (graduated cylinder — the last digit is estimated). Embed.
- **Investigation:** sig-fig sorting (cards: how many sig figs?) + measure to the correct number of digits (one estimated digit) + convert standard ↔ scientific notation.
- **Make It Make Sense:** count sig figs (5 items incl. leading/trailing zeros); round a calculated result to 3 sig figs; convert 0.000452 and 92,500,000 to scientific notation.
- **Exit Ticket:** (a) sig figs in 0.03080? (b) write 6,420,000 in scientific notation; (c) round 7.86342 to 3 sig figs. **Answers:** (a) 4; (b) 6.42×10⁶; (c) 7.86.

- [ ] **Step 1–4:** Author the four documents.
- [ ] **Step 5:** Build & verify (`…/03_Significant_Figures_and_Scientific_Notation`) → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit `feat(chem): Unit 1 Lesson 03 — Significant Figures & Scientific Notation`.

---

## Task 8: Lesson 04 — Dimensional Analysis

**Files (create):** `…/04_Dimensional_Analysis/{…}.md`

**Brief:**
- **Phenomenon:** A recipe / dosage that must be converted across units (or "how many atoms are in a copper penny?") — quantities span from the macroscopic to 10²³. *Driving question:* How do we convert between very large and very small quantities (atoms ↔ grams)?
- **NYSSLS:** HS-PS1-7 (use the mole to convert between atomic and macroscopic scale).
- **CCC focus:** Scale, Proportion, and Quantity.
- **Strategy chip:** HOCHMAN (Because/But/So on why the units cancel).
- **Vocabulary (≤3):** **conversion factor**, **dimensional analysis**, **metric prefix**.
- **Figure:** `figures/atoms_to_moles.png` (railroad-track factor-label). Embed.
- **Investigation:** build conversion "trains" — units cancel diagonally; practice metric-prefix conversions (km↔m↔cm↔mm) and mol↔atoms with Avogadro's number.
- **Make It Make Sense:** convert 2.5 km → cm; 0.75 mol → atoms; 250 mL → L.
- **Exit Ticket:** (a) Convert 3.0 mol Cu to atoms (show the track); (b) convert 5,400 mg to g; (c) one sentence: how do you know the units are right? **Answers:** (a) 3.0 × 6.02×10²³ = 1.8×10²⁴ atoms; (b) 5.4 g; (c) the unwanted units cancel top-and-bottom, leaving the target unit.

- [ ] **Step 1–4:** Author the four documents (embed the railroad-track figure; Hochman spotlight on "units cancel because…").
- [ ] **Step 5:** Build & verify (`…/04_Dimensional_Analysis`) → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit `feat(chem): Unit 1 Lesson 04 — Dimensional Analysis`.

---

## Task 9: Lesson 05 — Density

**Files (create):** `…/05_Density/{…}.md`

**Brief:**
- **Phenomenon:** Ice floats on its own liquid (most solids sink in theirs) — a glass of ice water. *Driving question:* Why does ice float when most solids sink?
- **NYSSLS:** HS-PS2-6 (molecular-level structure → material function).
- **CCC focus:** Structure and Function (particle spacing → bulk density).
- **Strategy chip:** ACTIVE LEARNING (density lab).
- **Vocabulary (≤3):** **density**, **mass**, **volume**.
- **Figures:** `figures/density_graph.png` (mass vs. volume; slope = density) + `figures/ice_vs_water.png` (open ice lattice vs. packed water). Embed both.
- **Investigation:** measure mass & volume of metal samples; plot mass vs. volume; slope = density; identify the metal from a density table; explain ice via particle spacing.
- **Make It Make Sense:** D = m/V calcs (find D, find m, find V); why does the slope = density; predict float/sink given densities.
- **Exit Ticket:** A 13.5 g aluminum cube displaces 5.0 mL of water. (a) density? (b) will it float in water (D=1.0 g/mL)? (c) one sentence: how does particle spacing explain ice floating? **Answers:** (a) 2.7 g/mL; (b) no, sinks (2.7 > 1.0); (c) ice's open hexagonal lattice spreads particles farther apart, so ice is less dense than liquid water.

- [ ] **Step 1–4:** Author the four documents (OPTIC spotlight on reading the mass-vs-volume slope; embed both figures).
- [ ] **Step 5:** Build & verify (`…/05_Density`) → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit `feat(chem): Unit 1 Lesson 05 — Density`.

---

## Task 10: Lesson 06 — Gram Formula Mass

**Files (create):** `…/06_Gram_Formula_Mass/{…}.md`

**Brief:**
- **Phenomenon:** Equal *numbers* of atoms of different elements weigh wildly different amounts (a mole of carbon = 12 g, a mole of gold = 197 g — same count, same scoop size, different mass). *Driving question:* Why do equal numbers of atoms have such different masses?
- **NYSSLS:** HS-PS1-2 (identify/describe the molar mass of all components of a reaction).
- **CCC focus:** Scale, Proportion, and Quantity.
- **Strategy chip:** HOCHMAN (appositive defining gram formula mass).
- **Vocabulary (≤3):** **gram formula mass**, **molar mass**, **mole**.
- **Figure:** `figures/molar_masses.png` (bar chart of GFM for H₂O, CO₂, NaCl, glucose). Embed.
- **Investigation:** compute GFM from formulas using the periodic table; "mass of one mole" demo comparison.
- **Make It Make Sense:** GFM of H₂O, CaCl₂, C₆H₁₂O₆ (show the add-up).
- **Exit Ticket:** (a) GFM of CO₂? (b) GFM of NaOH? (c) one sentence: why is gold's molar mass larger than carbon's for the same number of atoms? **Answers:** (a) 44 g/mol (12 + 2×16); (b) 40 g/mol (23+16+1); (c) each gold atom has far more protons+neutrons, so the same count of atoms has more mass.

- [ ] **Step 1–4:** Author the four documents (embed the bar chart).
- [ ] **Step 5:** Build & verify (`…/06_Gram_Formula_Mass`) → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit `feat(chem): Unit 1 Lesson 06 — Gram Formula Mass`.

---

## Task 11: Lesson 07 — Percent Composition

**Files (create):** `…/07_Percent_Composition/{…}.md`

**Brief:**
- **Phenomenon:** Two fertilizers both claim "nitrogen" but one grows greener grass — the % nitrogen by mass differs. *Driving question:* How can we tell what a compound is made of without taking it apart?
- **NYSSLS:** Foundational quantitative skill → supports HS-PS1-2.
- **CCC focus:** Scale, Proportion, and Quantity.
- **Strategy chip:** BTC (percent-composition thin-slice).
- **Vocabulary (≤3):** **percent composition**, **gram formula mass**, **mass ratio**.
- **Figure:** `figures/water_composition.png` (pie — 11.2% H / 88.8% O). Embed.
- **Investigation:** % by mass = (mass of element / GFM) × 100; compute for water and a fertilizer compound; (optional) percent water in a hydrate lab data.
- **Make It Make Sense:** % composition of each element in CO₂ and in NaCl; which of two compounds is richer in nitrogen.
- **Exit Ticket:** For H₂O (GFM 18): (a) % H by mass? (b) % O by mass? (c) one sentence: why do the percents add to 100? **Answers:** (a) (2/18)×100 = 11.1%; (b) (16/18)×100 = 88.9%; (c) every gram of the compound is accounted for by its elements, so the parts sum to the whole.

- [ ] **Step 1–4:** Author the four documents (embed the pie).
- [ ] **Step 5:** Build & verify (`…/07_Percent_Composition`) → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit `feat(chem): Unit 1 Lesson 07 — Percent Composition`.

---

## Task 12: Lesson 08 — The 2025 Chemistry Reference Tables

**Files (create):** `…/08_Chemistry_Reference_Tables/{…}.md`

**Brief:**
- **Phenomenon:** Every Regents chemist is handed the *same* booklet on test day — top scorers find an answer in seconds; others never open it. *Driving question:* How does one document support every chemistry concept on the exam?
- **NYSSLS:** Foundational test-readiness / SEP (obtaining & using information). Per slide 12: "assume tables are given within the clusters."
- **CCC focus:** Patterns (the tables organize recurring data patterns).
- **Strategy chip:** ACTIVE LEARNING (reference-tables scavenger hunt).
- **Vocabulary (≤3):** **reference table**, **density** (revisit), **standard pressure/temperature (STP)**.
- **Figure:** `figures/matter_map.png` (classification tree — a concept map tying Unit 1 together). Embed.
- **Investigation:** "find the data" stations — locate density of water, an element's properties, unit symbols, STP values in the 2025 tables; compare with the old edition.
- **Make It Make Sense:** which table holds X? (3 lookups); use a table value in a one-step calc.
- **Exit Ticket:** (a) Which table gives the density of water? (b) what are STP conditions? (c) one sentence: why practice using the tables before the exam? **Answers:** (a) the physical-constants/properties table; (b) 101.3 kPa and 273 K (0 °C); (c) fluency means finding the right datum fast, turning recall into a lookup skill.

- [ ] **Step 1–4:** Author the four documents (this lesson also serves as the Unit 1 synthesis — the concept-map figure reviews matter classification + measurement; "when you see ___ = do ___" Regents-verb decoder in Strategy Spotlight).
- [ ] **Step 5:** Build & verify (`…/08_Chemistry_Reference_Tables`) → 4 artifacts, no FAILED.
- [ ] **Step 6:** Commit `feat(chem): Unit 1 Lesson 08 — Chemistry Reference Tables`.

---

## Task 13: Unit Plan

**Files (create):** `…/01_Safety_and_Measurement/Unit_Plan.md`

Mirror the Forces `Unit_Plan.md`. Required headings: `## Cover`, `## Unit Scope (from East Meadow Scope & Sequence)`, `## Pacing Calendar`, `## Strategy Rotation`, `## NYSSLS Coverage Matrix`, `## Vocabulary Scope`.

- [ ] **Step 1: Author `Unit_Plan.md`** with these tables:

  - **Cover:** "Unit 1: Safety & Measurement", "East Meadow Schools × Valley Stream Central High School District", "8 lessons · ~8 instructional periods (42 min)", "Format: DOCX (Teacher Guide · Student Worksheet · Student Notes · Answer Key per lesson)".
  - **Unit Scope:** 1-paragraph overview (foundational safety + quantitative skills underpinning all of HS-PS1) + a lesson table (01–08 with core idea), drawn from the Scope & Sequence Table 0.
  - **Pacing Calendar:** Day | Lesson | Phenomenon anchor | Strategy (use each lesson's brief).
  - **Strategy Rotation:** RESTORATIVE CIRCLE (L01) · ACTIVE LEARNING (L02, L05, L08) · BTC (L03, L07) · HOCHMAN (L04, L06).
  - **NYSSLS Coverage Matrix:** HS-PS1-7 → L02, L04; HS-PS1-2 → L06, L07; HS-PS2-6 → L05; Foundational (SEP) → L01, L03, L08.
  - **Vocabulary Scope:** one row per lesson listing its ≤3 terms (from the briefs).

- [ ] **Step 2: Build & verify the unit plan**

  `python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor 01_Safety_and_Measurement` → builds the Unit Plan + all 8 lessons; expect `Built 33 artifacts` (32 lesson DOCX + 1 unit plan DOCX) and **no FAILED**.

- [ ] **Step 3: Commit** `feat(chem): Unit 1 Unit Plan + full-unit build`.

---

## Task 14: Full-unit verification & wrap-up

**Files:** none new — verification only.

- [ ] **Step 1: Re-render figures + clean build from scratch**

```bash
source .venv/bin/activate
python tools/_gen_chem_unit01_figures.py
python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor 01_Safety_and_Measurement
```
Expected: `Built 33 artifacts. Report: build_report.md`, no FAILED line. Inspect `build_report.md` to confirm 0 failures.

- [ ] **Step 2: Run the full test suite**

Run: `python -m pytest tests/tools/ -q`
Expected: all green (34+ tests, incl. `test_build_root.py` and `test_figures_chem.py`).

- [ ] **Step 3: Spot-check generated DOCX**

```bash
python - <<'PY'
from docx import Document
import glob
for p in sorted(glob.glob("Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor/01_Safety_and_Measurement/0*/Teacher_Guide.docx"))[:3]:
    d = Document(p)
    imgs = len(d.inline_shapes)
    heads = [x.text for x in d.paragraphs if x.style.name.startswith("Heading")][:6]
    print(p.split("/")[-2], "| inline images:", imgs, "| first heads:", heads)
PY
```
Expected: each Teacher Guide reports ≥1 inline image and the 5E headings — confirming figures embed and styling applied.

- [ ] **Step 4: Update memory + RESUME note (optional but recommended)**

Add a one-line pointer in the project memory index for the chemistry pilot, and note Units 2–11 as the next cycle.

- [ ] **Step 5: Final commit + offer to push / open PR**

```bash
git add -A && git commit -m "chore(chem): Unit 1 pilot verified — clean build, tests green

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```
Then offer to push `chemistry-east-meadow-refactor` and open a PR (per the finishing-a-development-branch skill).

---

## Self-Review notes (for the executor)

- **Spec coverage:** Task 1 = pipeline `--root` (spec §6); Tasks 2 = track + brand (spec §3); Task 3 = broad figure library (spec §5); Task 4 = per-unit figures (spec §5); Tasks 5–12 = the 8 S&S Unit-1 lessons (spec §2, §4); Task 13 = Unit Plan (spec §4); Task 14 = testing/verification (spec §8). PowerPoint fidelity (spec §7) is enforced in every lesson via the crosswalk + ABCs + literacy callouts.
- **No schema change** — all documents conform to the existing `tools/lesson_schema.yaml`.
- **Figure-name consistency:** the names in `_gen_chem_unit01_figures.py` (`safety_equipment.png`, `graduated_cylinder.png`, `accuracy_precision.png`, `reading_precision.png`, `atoms_to_moles.png`, `density_graph.png`, `ice_vs_water.png`, `molar_masses.png`, `water_composition.png`, `matter_map.png`) must exactly match the `![alt](figures/…)` paths authored in the lesson markdown.
- **Vocab cap:** every lesson lists exactly ≤3 terms in both `Student_Notes.md` Key Vocabulary and the Teacher Guide "Key Vocabulary (max 3)" — the validator hard-fails on a 4th.
- **MC answer emphasis:** if any Regents-style MC items are added later, never bold/italicize the correct option (validator hard-fails).
