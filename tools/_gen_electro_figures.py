"""One-off generator: figures for Unit 06 Electrostatics lessons.

Run from project root with the venv active:
    python tools/_gen_electro_figures.py

Charge/field diagrams are hand-rolled matplotlib here (the shared helper
library covers graphs, FBDs, and vector diagrams, but not +/- charges or
field lines). The Coulomb F-vs-r graph and the field-vector diagram do use
the shared helpers.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle

from tools.figures import (
    line_graph, vector_diagram,
    PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, _save,
)

UNIT = Path("Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/06_Electrostatics")

POS = "#c0392b"   # red for positive charge
NEG = "#2e5cb8"   # blue for negative charge


def fig_dir(lesson: str) -> Path:
    d = UNIT / lesson / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _charge(ax, xy, sign, *, r=0.42, fs=20):
    """Draw a charged sphere with a + or - sign."""
    color = POS if sign > 0 else NEG
    ax.add_patch(Circle(xy, r, facecolor=color, edgecolor=INK, zorder=4))
    ax.text(xy[0], xy[1], "+" if sign > 0 else "−", ha="center",
            va="center", color="white", fontsize=fs, fontweight="bold",
            zorder=5)


# ---------------------------------------------------------------------------
# L01 — Electric Charge
# ---------------------------------------------------------------------------
def attract_repel(path):
    """Three panels: like + repel, like - repel, unlike attract."""
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4))
    fig.suptitle("Like charges repel; unlike charges attract",
                 fontsize=13, fontweight="bold")
    panels = [
        (1, 1, "Repel", "out"),
        (-1, -1, "Repel", "out"),
        (1, -1, "Attract", "in"),
    ]
    for ax, (s1, s2, label, direction) in zip(axes, panels):
        ax.set_xlim(-3, 3)
        ax.set_ylim(-2, 2)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(label, fontsize=12)
        left, right = (-1.4, 0), (1.4, 0)
        _charge(ax, left, s1)
        _charge(ax, right, s2)
        if direction == "out":
            ax.add_patch(FancyArrowPatch((-1.9, 0), (-2.6, 0), arrowstyle="-|>",
                         mutation_scale=16, linewidth=2.4, color=INK))
            ax.add_patch(FancyArrowPatch((1.9, 0), (2.6, 0), arrowstyle="-|>",
                         mutation_scale=16, linewidth=2.4, color=INK))
        else:
            ax.add_patch(FancyArrowPatch((-0.95, 0), (-0.25, 0), arrowstyle="-|>",
                         mutation_scale=16, linewidth=2.4, color=INK))
            ax.add_patch(FancyArrowPatch((0.95, 0), (0.25, 0), arrowstyle="-|>",
                         mutation_scale=16, linewidth=2.4, color=INK))
    return _save(fig, path)


def charged_balloon(path):
    """A negatively charged balloon clinging to a neutral wall, with the wall
    surface polarized (+ near the balloon)."""
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 7)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Charged balloon clings to a neutral wall")
    # wall
    ax.add_patch(Rectangle((6.2, 0), 1.8, 7, facecolor="#ece9f2",
                 edgecolor=INK, zorder=1))
    ax.text(7.1, 6.5, "wall", ha="center", fontsize=10, color=INK)
    # balloon (negative)
    ax.add_patch(Circle((3.4, 3.5), 1.5, facecolor=BLUE, edgecolor=INK,
                 alpha=0.85, zorder=3))
    ax.text(3.4, 3.5, "rubbed\nballoon", ha="center", va="center",
            color="white", fontsize=10, fontweight="bold", zorder=4)
    for y in (4.4, 3.5, 2.6):
        ax.text(4.7, y, "−", color="white", fontsize=16,
                fontweight="bold", ha="center", va="center", zorder=4)
    # wall surface polarizes: + appear on the near face
    for y in (4.4, 3.5, 2.6):
        ax.text(6.35, y, "+", color=POS, fontsize=16, fontweight="bold",
                ha="center", va="center", zorder=2)
    # attraction arrow
    ax.add_patch(FancyArrowPatch((5.0, 1.4), (6.1, 1.4), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=ACCENT2, zorder=5))
    ax.text(5.55, 0.9, "attraction", ha="center", color=ACCENT2,
            fontsize=10, fontweight="bold")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L02 — Conductors, Insulators, Charging by Conduction
# ---------------------------------------------------------------------------
def conductor_vs_insulator(path):
    """Two panels: conductor (charge spreads freely) vs insulator (charge
    stays put where placed)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.6))
    titles = ["Conductor: charge moves freely",
              "Insulator: charge stays put"]
    for ax, title, spread in zip(axes, titles, [True, False]):
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 5)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=12)
        ax.add_patch(Rectangle((1, 1.5), 6, 2, facecolor="#ece9f2",
                     edgecolor=INK, zorder=1))
        if spread:
            xs = np.linspace(1.6, 6.4, 6)
        else:
            xs = np.array([1.7, 2.0, 2.3, 2.0, 2.3])
        ys = ([2.5] * len(xs)) if spread else [2.9, 2.5, 2.5, 2.1, 2.9]
        for x, y in zip(xs, ys):
            ax.text(x, y, "−", color=NEG, fontsize=16, fontweight="bold",
                    ha="center", va="center", zorder=3)
        note = "electrons spread out evenly" if spread else "electrons cannot migrate"
        ax.text(4, 0.7, note, ha="center", fontsize=10, color=INK)
    return _save(fig, path)


def conduction_steps(path):
    """Three-panel charging by conduction: charged rod -> contact -> both share
    the same sign."""
    fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.4))
    fig.suptitle("Charging by conduction: contact shares charge (same sign)",
                 fontsize=13, fontweight="bold")
    steps = ["1. Charged rod approaches", "2. Contact transfers charge",
             "3. Both now negative"]
    for ax, title in zip(axes, steps):
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 5)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=11)
        # sphere on a stand
        ax.add_patch(Rectangle((4.6, 0.3), 0.5, 1.3, facecolor="#bbb",
                     edgecolor=INK, zorder=1))
    # Panel 1: rod (neg) near neutral sphere
    ax = axes[0]
    ax.add_patch(Rectangle((0.6, 2.0), 2.6, 0.5, facecolor=BLUE,
                 edgecolor=INK, zorder=2))
    ax.text(1.9, 2.25, "− − −", color="white", fontsize=11,
            ha="center", va="center", fontweight="bold", zorder=3)
    ax.add_patch(Circle((4.9, 2.6), 0.9, facecolor="#ece9f2", edgecolor=INK,
                 zorder=2))
    ax.text(4.9, 2.6, "neutral", ha="center", va="center", fontsize=8)
    # Panel 2: touching
    ax = axes[1]
    ax.add_patch(Rectangle((1.2, 2.2), 2.6, 0.5, facecolor=BLUE,
                 edgecolor=INK, zorder=2))
    ax.add_patch(Circle((4.9, 2.6), 0.9, facecolor="#ece9f2", edgecolor=INK,
                 zorder=2))
    ax.text(3.9, 2.45, "→", fontsize=18, ha="center", va="center",
            color=INK, zorder=3)
    ax.text(4.9, 2.6, "− −", color=NEG, ha="center", va="center",
            fontsize=12, fontweight="bold", zorder=3)
    # Panel 3: rod removed, sphere negative
    ax = axes[2]
    ax.add_patch(Circle((4.9, 2.6), 0.9, facecolor=BLUE, edgecolor=INK,
                 alpha=0.85, zorder=2))
    ax.text(4.9, 2.6, "− −", color="white", ha="center", va="center",
            fontsize=12, fontweight="bold", zorder=3)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L03 — Charging by Induction and Polarization
# ---------------------------------------------------------------------------
def induction_steps(path):
    """Four-panel charging by induction of a neutral sphere using a negative
    rod (no contact): approach -> ground -> remove ground -> remove rod."""
    fig, axes = plt.subplots(1, 4, figsize=(12.0, 3.4))
    fig.suptitle("Charging by induction (no contact): final charge is OPPOSITE the rod",
                 fontsize=12, fontweight="bold")
    titles = ["1. Bring − rod near", "2. Ground the far side",
              "3. Remove ground", "4. Remove rod → + sphere"]
    for ax, title in zip(axes, titles):
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 5)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=10)
    # common rod drawer
    def rod(ax):
        ax.add_patch(Rectangle((0.2, 3.0), 1.8, 0.45, facecolor=BLUE,
                     edgecolor=INK, zorder=2))
        ax.text(1.1, 3.22, "−−−", color="white", fontsize=9,
                ha="center", va="center", fontweight="bold", zorder=3)

    def sphere(ax, fc="#ece9f2"):
        ax.add_patch(Circle((5.2, 2.4), 1.1, facecolor=fc, edgecolor=INK,
                     zorder=2))
    # Panel 1: rod near, polarized sphere (+ near rod, - far)
    rod(axes[0]); sphere(axes[0])
    axes[0].text(4.4, 2.4, "+", color=POS, fontsize=15, fontweight="bold",
                 ha="center", va="center", zorder=3)
    axes[0].text(6.0, 2.4, "−", color=NEG, fontsize=15, fontweight="bold",
                 ha="center", va="center", zorder=3)
    # Panel 2: grounded — electrons flee to ground
    rod(axes[1]); sphere(axes[1])
    axes[1].text(4.4, 2.4, "+", color=POS, fontsize=15, fontweight="bold",
                 ha="center", va="center", zorder=3)
    axes[1].add_patch(FancyArrowPatch((6.3, 2.4), (7.4, 1.0), arrowstyle="-|>",
                      mutation_scale=14, linewidth=2.0, color=NEG, zorder=3))
    axes[1].text(7.4, 0.7, "ground", ha="center", fontsize=8, color=INK)
    # Panel 3: ground removed, rod still there: net +
    rod(axes[2]); sphere(axes[2])
    axes[2].text(4.6, 2.4, "+ +", color=POS, fontsize=14, fontweight="bold",
                 ha="center", va="center", zorder=3)
    # Panel 4: rod removed, + spreads over sphere
    sphere(axes[3], fc=POS)
    axes[3].text(5.2, 2.4, "+ +", color="white", fontsize=14, fontweight="bold",
                 ha="center", va="center", zorder=3)
    return _save(fig, path)


def polarization(path):
    """A neutral object (paper bits / atoms) polarized by a nearby charged rod,
    producing net attraction."""
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Polarization: a charged rod attracts a NEUTRAL object")
    # positive rod on the left
    ax.add_patch(Rectangle((0.3, 2.0), 2.0, 0.6, facecolor=POS,
                 edgecolor=INK, zorder=2))
    ax.text(1.3, 2.3, "+ + +", color="white", fontsize=12, ha="center",
            va="center", fontweight="bold", zorder=3)
    # neutral atom: drawn as small ovals, each with - shifted toward the rod
    for cx in (4.0, 5.4, 6.8):
        ax.add_patch(Circle((cx, 2.3), 0.55, facecolor="#ece9f2",
                     edgecolor=INK, zorder=2))
        ax.text(cx - 0.28, 2.3, "−", color=NEG, fontsize=12,
                fontweight="bold", ha="center", va="center", zorder=3)
        ax.text(cx + 0.28, 2.3, "+", color=POS, fontsize=12,
                fontweight="bold", ha="center", va="center", zorder=3)
    ax.add_patch(FancyArrowPatch((4.4, 1.1), (2.7, 1.1), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=ACCENT2, zorder=5))
    ax.text(3.6, 0.6, "net attraction", ha="center", color=ACCENT2,
            fontsize=10, fontweight="bold")
    ax.text(5.4, 3.4, "negative ends shift toward the + rod", ha="center",
            fontsize=9, color=INK)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L04 — Coulomb's Law
# ---------------------------------------------------------------------------
def two_charge_force_pair(path):
    """Two like charges with equal-length repulsive force arrows (Newton's
    third law for the electrostatic force)."""
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2.4, 3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Coulomb's law: equal & opposite forces on the two charges")
    _charge(ax, (2.0, 0.5), 1, r=0.7, fs=22)
    ax.text(2.0, 1.6, "q₁", ha="center", fontsize=12, fontweight="bold")
    _charge(ax, (8.0, 0.5), 1, r=0.7, fs=22)
    ax.text(8.0, 1.6, "q₂", ha="center", fontsize=12, fontweight="bold")
    # force on q1 points left (repelled away from q2)
    ax.add_patch(FancyArrowPatch((1.2, 0.5), (-0.6, 0.5), arrowstyle="-|>",
                 mutation_scale=20, linewidth=3.0, color=ACCENT2, zorder=5))
    ax.text(0.3, 1.0, "F on q₁", ha="center", color=ACCENT2,
            fontsize=11, fontweight="bold")
    # force on q2 points right, equal length
    ax.add_patch(FancyArrowPatch((8.8, 0.5), (10.6, 0.5), arrowstyle="-|>",
                 mutation_scale=20, linewidth=3.0, color=GREEN, zorder=5))
    ax.text(9.7, 1.0, "F on q₂", ha="center", color=GREEN,
            fontsize=11, fontweight="bold")
    ax.annotate("", xy=(8.0, -1.4), xytext=(2.0, -1.4),
                arrowprops=dict(arrowstyle="<->", color=INK, linewidth=1.2))
    ax.text(5.0, -1.9, "r (distance between centers)", ha="center",
            fontsize=10, color=INK)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L05 — Electric Fields
# ---------------------------------------------------------------------------
def field_around_point_charge(path, sign=1):
    """Radial field-vector arrows around a single point charge (out for +,
    in for -)."""
    fig, ax = plt.subplots(figsize=(5.0, 5.0))
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.2, 3.2)
    ax.set_aspect("equal")
    ax.axis("off")
    label = "positive" if sign > 0 else "negative"
    ax.set_title(f"Electric field around a {label} charge")
    _charge(ax, (0, 0), sign, r=0.5, fs=22)
    for ang in range(0, 360, 30):
        a = np.deg2rad(ang)
        if sign > 0:
            start = (0.6 * np.cos(a), 0.6 * np.sin(a))
            end = (2.4 * np.cos(a), 2.4 * np.sin(a))
        else:
            start = (2.4 * np.cos(a), 2.4 * np.sin(a))
            end = (0.65 * np.cos(a), 0.65 * np.sin(a))
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                     mutation_scale=12, linewidth=1.8, color=PURPLE))
    note = "field points AWAY from +" if sign > 0 else "field points TOWARD −"
    ax.text(0, -3.0, note, ha="center", fontsize=10, color=INK,
            fontweight="bold")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L06 — Electric Field Lines
# ---------------------------------------------------------------------------
def field_lines_single(path):
    """Continuous radial field lines leaving a single positive charge."""
    fig, ax = plt.subplots(figsize=(5.0, 5.0))
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.2, 3.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Field lines: single positive charge (lines start on +)")
    _charge(ax, (0, 0), 1, r=0.5, fs=22)
    for ang in range(0, 360, 30):
        a = np.deg2rad(ang)
        x0, y0 = 0.5 * np.cos(a), 0.5 * np.sin(a)
        x1, y1 = 3.0 * np.cos(a), 3.0 * np.sin(a)
        ax.plot([x0, x1], [y0, y1], color=PURPLE, linewidth=1.6, zorder=2)
        # arrowhead mid-line
        mx, my = 1.7 * np.cos(a), 1.7 * np.sin(a)
        ax.add_patch(FancyArrowPatch((mx - 0.01 * np.cos(a), my - 0.01 * np.sin(a)),
                     (mx + 0.2 * np.cos(a), my + 0.2 * np.sin(a)),
                     arrowstyle="-|>", mutation_scale=12, color=PURPLE,
                     linewidth=1.6, zorder=3))
    return _save(fig, path)


def field_lines_dipole(path):
    """Dipole field lines: curve from + to -, never crossing."""
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Dipole field lines: start on +, end on −, never cross")
    qpos, qneg = (-1.6, 0), (1.6, 0)
    _charge(ax, qpos, 1, r=0.45, fs=18)
    _charge(ax, qneg, -1, r=0.45, fs=18)

    def field(x, y):
        ex = ey = 0.0
        for (cx, cy), s in [(qpos, 1), (qneg, -1)]:
            dx, dy = x - cx, y - cy
            r2 = dx * dx + dy * dy
            r = np.sqrt(r2) + 1e-9
            ex += s * dx / (r2 * r)
            ey += s * dy / (r2 * r)
        return ex, ey

    for ang in range(20, 360, 40):
        a = np.deg2rad(ang)
        x, y = qpos[0] + 0.5 * np.cos(a), qpos[1] + 0.5 * np.sin(a)
        xs, ys = [x], [y]
        for _ in range(400):
            ex, ey = field(x, y)
            m = np.hypot(ex, ey) + 1e-12
            x += 0.04 * ex / m
            y += 0.04 * ey / m
            xs.append(x); ys.append(y)
            if np.hypot(x - qneg[0], y - qneg[1]) < 0.45:
                break
            if abs(x) > 4 or abs(y) > 3:
                break
        ax.plot(xs, ys, color=PURPLE, linewidth=1.3, zorder=1)
    return _save(fig, path)


def field_lines_parallel_plates(path):
    """Uniform field between two oppositely charged parallel plates."""
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Parallel plates: uniform field (evenly spaced lines)")
    ax.add_patch(Rectangle((1, 5.0), 6, 0.3, facecolor=POS, edgecolor=INK))
    ax.text(0.5, 5.15, "+", color=POS, fontsize=16, fontweight="bold",
            ha="center", va="center")
    ax.add_patch(Rectangle((1, 0.7), 6, 0.3, facecolor=NEG, edgecolor=INK))
    ax.text(0.5, 0.85, "−", color=NEG, fontsize=16, fontweight="bold",
            ha="center", va="center")
    for x in np.linspace(1.6, 6.4, 6):
        ax.add_patch(FancyArrowPatch((x, 4.9), (x, 1.1), arrowstyle="-|>",
                     mutation_scale=14, linewidth=1.8, color=PURPLE))
    ax.text(4, 0.1, "E is the same strength everywhere between the plates",
            ha="center", fontsize=9, color=INK)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Build all figures
# ---------------------------------------------------------------------------
def main():
    written = []

    # L01 — Electric Charge
    d = fig_dir("01_Electric_Charge")
    written.append(attract_repel(d / "attract_repel.png"))
    written.append(charged_balloon(d / "charged_balloon.png"))

    # L02 — Conductors / Insulators / Conduction
    d = fig_dir("02_Conductors_Insulators_and_Charging_by_Conduction")
    written.append(conductor_vs_insulator(d / "conductor_vs_insulator.png"))
    written.append(conduction_steps(d / "conduction_steps.png"))

    # L03 — Induction / Polarization
    d = fig_dir("03_Charging_by_Induction_and_Polarization")
    written.append(induction_steps(d / "induction_steps.png"))
    written.append(polarization(d / "polarization.png"))

    # L04 — Coulomb's Law
    d = fig_dir("04_Coulombs_Law")
    r = np.linspace(0.5, 5, 80)
    k = 8.99e9
    q = 1e-6
    Fe = k * q * q / (r ** 2)
    written.append(line_graph(
        d / "fe_vs_r_inverse_square.png",
        [("Fₑ vs r (q₁=q₂=1 µC)", list(r), list(Fe))],
        xlabel="distance r (m)", ylabel="electrostatic force Fₑ (N)",
        title="Coulomb's law: Fₑ ∝ 1 / r²"))
    written.append(two_charge_force_pair(d / "two_charge_force_pair.png"))

    # L05 — Electric Fields
    d = fig_dir("05_Electric_Fields")
    written.append(field_around_point_charge(d / "field_point_charge_pos.png", sign=1))
    r2 = np.linspace(0.3, 4, 80)
    E = k * q / (r2 ** 2)
    written.append(line_graph(
        d / "e_vs_r.png",
        [("E vs r (q = 1 µC)", list(r2), list(E))],
        xlabel="distance r (m)", ylabel="field strength E (N/C)",
        title="Field strength falls off as 1 / r²"))

    # L06 — Electric Field Lines
    d = fig_dir("06_Electric_Field_Lines")
    written.append(field_lines_single(d / "field_lines_single.png"))
    written.append(field_lines_dipole(d / "field_lines_dipole.png"))
    written.append(field_lines_parallel_plates(d / "field_lines_parallel_plates.png"))

    print(f"Wrote {len(written)} figures:")
    for w in written:
        print(" ", w)


if __name__ == "__main__":
    main()
