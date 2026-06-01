"""Reusable, brand-styled figure builders for East Meadow physics lessons.

Every lesson can call these to drop charts, graphs, and diagrams into its
`figures/` folder; the Markdown sources reference them with a relative path
(`![alt](figures/name.png)`) and pandoc embeds them into the DOCX.

Design goals: clean, high-contrast, print-friendly, consistent across the whole
curriculum. Co-brand accents: purple #662e80, blue #2ea3f2.

All builders take an output `path` (str | Path), create parent dirs, and write a
150-dpi PNG. They never call `Date.now`/random — fully deterministic.
"""
from __future__ import annotations
from pathlib import Path
from typing import Iterable, Sequence

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle

# --- Brand palette ---------------------------------------------------------
PURPLE = "#662e80"
BLUE = "#2ea3f2"
INK = "#222222"
GRID = "#d8d8e0"
ACCENT2 = "#e67e22"
GREEN = "#2e9e5b"
SERIES = [PURPLE, BLUE, ACCENT2, GREEN, "#c0392b", "#16a085"]

plt.rcParams.update({
    "font.size": 12,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "text.color": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "figure.dpi": 150,
})


def _prep(path) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def _save(fig, path) -> str:
    p = _prep(path)
    fig.savefig(p, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return str(p)


def line_graph(path, series, *, xlabel="x", ylabel="y", title="",
               markers=False, figsize=(5.0, 3.4)) -> str:
    """Plot one or more (label, xs, ys) line series. For motion graphs,
    force-vs-acceleration, I-V curves, decay curves, etc."""
    fig, ax = plt.subplots(figsize=figsize)
    for i, (label, xs, ys) in enumerate(series):
        ax.plot(xs, ys, color=SERIES[i % len(SERIES)], linewidth=2.4,
                marker="o" if markers else None, markersize=4, label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.axvline(0, color=INK, linewidth=0.8)
    if any(lbl for lbl, _, _ in series):
        ax.legend(frameon=False, fontsize=10)
    return _save(fig, path)


def bar_chart(path, categories, values, *, ylabel="", title="",
              series_labels=None, figsize=(5.0, 3.4)) -> str:
    """Bar chart. `values` is a list of numbers, or a list of lists for grouped
    bars (energy bar charts, before/after comparisons)."""
    import numpy as np
    fig, ax = plt.subplots(figsize=figsize)
    cats = list(categories)
    x = np.arange(len(cats))
    if values and isinstance(values[0], (list, tuple)):
        n = len(values)
        w = 0.8 / n
        for i, vals in enumerate(values):
            lbl = series_labels[i] if series_labels else None
            ax.bar(x + (i - (n - 1) / 2) * w, vals, w,
                   color=SERIES[i % len(SERIES)], label=lbl)
        if series_labels:
            ax.legend(frameon=False, fontsize=10)
    else:
        ax.bar(x, values, 0.6, color=PURPLE)
    ax.set_xticks(x)
    ax.set_xticklabels(cats)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    ax.grid(True, axis="y", color=GRID, linewidth=0.8)
    return _save(fig, path)


def free_body_diagram(path, forces, *, body_label="object", title="",
                      figsize=(4.2, 4.2)) -> str:
    """Free-body diagram: a central box with labeled force arrows.

    `forces` is a list of (label, dx, dy) where (dx, dy) is the arrow direction
    (need not be unit length; it's normalized for display). E.g.
    [("F_gravity", 0, -1), ("F_normal", 0, 1), ("F_applied", 1, 0), ("friction", -0.6, 0)].
    """
    import numpy as np
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title)
    # body
    ax.add_patch(Rectangle((-0.45, -0.45), 0.9, 0.9, facecolor=PURPLE,
                           edgecolor=INK, alpha=0.85, zorder=3))
    ax.text(0, 0, body_label, ha="center", va="center", color="white",
            fontsize=9, fontweight="bold", zorder=4)
    for i, (label, dx, dy) in enumerate(forces):
        mag = (dx * dx + dy * dy) ** 0.5 or 1.0
        ux, uy = dx / mag, dy / mag
        start = (ux * 0.5, uy * 0.5)
        end = (ux * 1.7, uy * 1.7)
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                     mutation_scale=18, linewidth=2.6,
                     color=SERIES[i % len(SERIES)], zorder=5))
        ax.text(ux * 1.95, uy * 1.95, label, ha="center", va="center",
                fontsize=10, color=SERIES[i % len(SERIES)], fontweight="bold")
    return _save(fig, path)


def vector_diagram(path, vectors, *, origin=(0, 0), title="", xlabel="x",
                   ylabel="y", grid=True, figsize=(4.6, 4.0), tip_to_tail=False) -> str:
    """Draw vectors as arrows. `vectors` is a list of (label, vx, vy).

    If tip_to_tail, each vector starts where the previous ended (vector
    addition); a dashed resultant from the first origin to the final tip is
    drawn. Otherwise all start at `origin`."""
    fig, ax = plt.subplots(figsize=figsize)
    x0, y0 = origin
    cx, cy = x0, y0
    xs = [x0]; ys = [y0]
    for i, (label, vx, vy) in enumerate(vectors):
        sx, sy = (cx, cy) if tip_to_tail else (x0, y0)
        ex, ey = sx + vx, sy + vy
        ax.add_patch(FancyArrowPatch((sx, sy), (ex, ey), arrowstyle="-|>",
                     mutation_scale=16, linewidth=2.4,
                     color=SERIES[i % len(SERIES)]))
        ax.text((sx + ex) / 2, (sy + ey) / 2, f" {label}", fontsize=10,
                color=SERIES[i % len(SERIES)], fontweight="bold")
        if tip_to_tail:
            cx, cy = ex, ey
        xs += [ex]; ys += [ey]
    if tip_to_tail and len(vectors) > 1:
        ax.add_patch(FancyArrowPatch((x0, y0), (cx, cy), arrowstyle="-|>",
                     mutation_scale=16, linewidth=2.4, linestyle="--",
                     color=INK))
        ax.text((x0 + cx) / 2, (y0 + cy) / 2 - 0.25, " resultant", fontsize=10,
                color=INK, fontweight="bold")
    pad = 1.0
    ax.set_xlim(min(xs) - pad, max(xs) + pad)
    ax.set_ylim(min(ys) - pad, max(ys) + pad)
    ax.set_aspect("equal")
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    if grid:
        ax.grid(True, color=GRID, linewidth=0.8)
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.axvline(0, color=INK, linewidth=0.8)
    return _save(fig, path)


if __name__ == "__main__":
    # Smoke test — render one of each into /tmp.
    line_graph("/tmp/fig_line.png",
               [("v(t)", [0, 1, 2, 3, 4], [0, 2, 4, 6, 8])],
               xlabel="time (s)", ylabel="velocity (m/s)",
               title="Constant acceleration", markers=True)
    bar_chart("/tmp/fig_bar.png", ["KE", "PE"], [[30, 0], [0, 30]],
              series_labels=["bottom", "top"], ylabel="energy (J)",
              title="Energy at two points")
    free_body_diagram("/tmp/fig_fbd.png",
                      [("F_N", 0, 1), ("F_g", 0, -1), ("F_app", 1, 0),
                       ("f_k", -0.6, 0)], body_label="box",
                      title="Free-body diagram")
    vector_diagram("/tmp/fig_vec.png",
                   [("A (4 E)", 4, 0), ("B (3 N)", 0, 3)], tip_to_tail=True,
                   title="Vector addition")
    print("wrote /tmp/fig_line.png /tmp/fig_bar.png /tmp/fig_fbd.png /tmp/fig_vec.png")
