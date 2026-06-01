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
    sides = [((0, 0.6), (0.18, 0)), ((0, -0.6), (0.18, 0)),
             ((-0.6, 0), (0, 0.18)), ((0.6, 0), (0, 0.18))]
    placed = 0
    for first, off in sides:
        if placed >= valence:
            break
        ax.add_patch(Circle(first, 0.06, facecolor=INK))
        placed += 1
    for first, off in sides:
        if placed >= valence:
            break
        ax.add_patch(Circle((first[0] + off[0], first[1] + off[1]), 0.06, facecolor=INK))
        placed += 1
    return _save(fig, path)


# --- Diagrams --------------------------------------------------------------
def classification_tree(path, *, figsize=(7.2, 4.6)) -> str:
    """Flowchart classifying matter: Matter -> (Pure Substances -> Elements,
    Compounds) and (Mixtures -> Homogeneous, Heterogeneous)."""
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
    xs = np.linspace(1, 3, 50)
    # concave meniscus dipping to h at the center
    meniscus_y = h - 0.18 * (1 - ((xs - 2) / 1) ** 2)
    ax.plot(xs, meniscus_y, color=BLUE, linewidth=2)
    for i in range(11):
        y = i
        ax.plot([2.8, 3], [y, y], color=INK, linewidth=1)
        ax.text(3.15, y, f"{int(capacity * i / 10)}", va="center", fontsize=7, color=INK)
    # annotate at the bottom of the meniscus (center)
    meniscus_center_y = h - 0.18
    ax.annotate(f"read here\n{reading} mL", xy=(2, meniscus_center_y),
                xytext=(3.4, meniscus_center_y + 1.4),
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
    return _save(fig, path)


def separation_apparatus(path, *, kind, figsize=(4.4, 4.0)) -> str:
    """Schematic of a separation setup. `kind` in {'filtration','distillation',
    'chromatography'}."""
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(kind.capitalize(), fontsize=12, fontweight="bold")
    if kind == "filtration":
        ax.add_patch(plt.Polygon([(3, 7), (7, 7), (5, 4)], closed=True,
                     fill=False, edgecolor=INK, linewidth=1.8))
        ax.plot([5, 5], [4, 3], color=INK, linewidth=1.5)
        ax.add_patch(Rectangle((3.4, 0.5), 3.2, 2.3, fill=False, edgecolor=INK, linewidth=1.8))
        ax.add_patch(Rectangle((3.4, 0.5), 3.2, 1.0, facecolor=BLUE, alpha=0.4, edgecolor="none"))
        ax.text(5, 7.6, "residue (solid) stays in paper", ha="center", fontsize=8, color=PURPLE)
        ax.text(5, 0.1, "filtrate (liquid)", ha="center", fontsize=8, color=BLUE)
    elif kind == "distillation":
        ax.add_patch(Circle((2.4, 2.6), 1.3, fill=False, edgecolor=INK, linewidth=1.8))
        ax.add_patch(Circle((2.4, 2.6), 1.3, facecolor=BLUE, alpha=0.35, edgecolor="none"))
        ax.plot([2.4, 2.4], [3.9, 6], color=INK, linewidth=1.6)
        ax.plot([2.4, 8], [6, 4.2], color=INK, linewidth=1.6)
        ax.add_patch(Circle((8.4, 3.4), 1.0, fill=False, edgecolor=INK, linewidth=1.8))
        ax.text(2.4, 0.8, "mixture (heat)", ha="center", fontsize=8, color=PURPLE)
        ax.text(8.4, 1.9, "pure distillate", ha="center", fontsize=8, color=BLUE)
    elif kind == "chromatography":
        ax.add_patch(Rectangle((4, 1), 2, 8, fill=False, edgecolor=INK, linewidth=1.8))
        ax.plot([4, 6], [2, 2], color=INK, linewidth=1, linestyle="--")
        for cy, c in [(3.2, PURPLE), (5.0, BLUE), (6.6, ACCENT2)]:
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
    return line_graph(path, [("", xs, values)], xlabel="", ylabel=ylabel,
                      title=title, markers=True)


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
