"""One-off generator: figures for Unit 02 Forces lessons.

Run from project root with the venv active:
    python tools/_gen_forces_figures.py
"""
from __future__ import annotations
from pathlib import Path
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

from tools.figures import (
    line_graph, free_body_diagram, vector_diagram,
    PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, _prep, _save,
)

UNIT = Path("Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/02_Forces")


def fig_dir(lesson: str) -> Path:
    d = UNIT / lesson / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------------------
# Custom diagrams (not covered by the helper library)
# ---------------------------------------------------------------------------
def action_reaction_pair(path):
    """Two bodies (A and B) touching, with equal & opposite force arrows on
    DIFFERENT bodies — the hallmark of a Newton's-third-law pair."""
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.set_xlim(-2.2, 9.6)
    ax.set_ylim(-2, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Action–Reaction Pair (forces on two different objects)")
    # Body A (left) and Body B (right)
    ax.add_patch(plt.Rectangle((1.0, 0.0), 2.4, 2.0, facecolor=PURPLE,
                 edgecolor=INK, alpha=0.85, zorder=3))
    ax.text(2.2, 1.0, "A", ha="center", va="center", color="white",
            fontsize=14, fontweight="bold", zorder=4)
    ax.add_patch(plt.Rectangle((4.0, 0.0), 2.4, 2.0, facecolor=BLUE,
                 edgecolor=INK, alpha=0.85, zorder=3))
    ax.text(5.2, 1.0, "B", ha="center", va="center", color="white",
            fontsize=14, fontweight="bold", zorder=4)
    # Force A-on-B: points right, drawn on B
    ax.add_patch(FancyArrowPatch((6.5, 1.0), (9.0, 1.0), arrowstyle="-|>",
                 mutation_scale=20, linewidth=3.0, color=ACCENT2, zorder=5))
    ax.text(7.75, 1.45, "F (A on B)", ha="center", color=ACCENT2,
            fontsize=11, fontweight="bold")
    # Force B-on-A: points left, drawn on A, EQUAL length
    ax.add_patch(FancyArrowPatch((0.9, 1.0), (-1.6, 1.0), arrowstyle="-|>",
                 mutation_scale=20, linewidth=3.0, color=GREEN, zorder=5,
                 clip_on=False))
    ax.text(-0.35, 1.45, "F (B on A)", ha="center", color=GREEN,
            fontsize=11, fontweight="bold")
    ax.text(5.0, -1.4, "Equal in size, opposite in direction, one on each body.",
            ha="center", fontsize=10, color=INK)
    return _save(fig, path)


def equal_opposite_pair(path):
    """Two equal-length arrows pointing opposite ways, drawn on separate rows
    so the labels never collide — abstract view of a Newton's-third-law pair."""
    fig, ax = plt.subplots(figsize=(5.4, 2.6))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.4, 1.4)
    ax.axis("off")
    ax.set_title("Equal in size, opposite in direction")
    ax.add_patch(FancyArrowPatch((0, 0.55), (3, 0.55), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.8, color=PURPLE))
    ax.text(0, 0.95, "action:  F (A on B)", color=PURPLE, fontsize=11,
            fontweight="bold")
    ax.add_patch(FancyArrowPatch((0, -0.55), (-3, -0.55), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.8, color=BLUE))
    ax.text(-3.0, -1.05, "reaction:  F (B on A)", color=BLUE, fontsize=11,
            fontweight="bold")
    ax.axvline(0, color=GRID, linewidth=1.0)
    return _save(fig, path)


def circular_motion_diagram(path):
    """Object on a circular path with a tangent velocity arrow and a
    centripetal force arrow pointing to the center."""
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    R = 1.6
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-2.6, 2.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Centripetal force points to the center")
    # circular path
    ax.add_patch(Circle((0, 0), R, fill=False, edgecolor=GRID, linewidth=2.0,
                 linestyle="--"))
    ax.plot(0, 0, marker="+", color=INK, markersize=12, markeredgewidth=2)
    ax.text(0.12, 0.18, "center", fontsize=9, color=INK)
    # object on the right of the circle
    obj = (R, 0)
    ax.add_patch(Circle(obj, 0.18, facecolor=PURPLE, edgecolor=INK, zorder=4))
    # velocity: tangent (upward at this point)
    ax.add_patch(FancyArrowPatch(obj, (R, 1.4), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.6, color=BLUE, zorder=5))
    ax.text(R + 0.1, 1.1, "v (velocity, tangent)", color=BLUE, fontsize=10,
            fontweight="bold")
    # centripetal force: toward center (to the left)
    ax.add_patch(FancyArrowPatch(obj, (0.15, 0), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.6, color=ACCENT2, zorder=5))
    ax.text(0.55, -0.32, "F_c (toward center)", color=ACCENT2, fontsize=10,
            fontweight="bold")
    return _save(fig, path)


def two_mass_gravity(path):
    """Two masses with equal-length attractive force arrows pointing toward
    each other (Newton's third law for gravity)."""
    fig, ax = plt.subplots(figsize=(6.0, 3.0))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-2, 3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Gravity: equal attractive forces on both masses")
    ax.add_patch(Circle((1.5, 0.5), 0.9, facecolor=PURPLE, edgecolor=INK,
                 alpha=0.85, zorder=3))
    ax.text(1.5, 0.5, "m₁", ha="center", va="center", color="white",
            fontsize=13, fontweight="bold", zorder=4)
    ax.add_patch(Circle((8.5, 0.5), 1.3, facecolor=BLUE, edgecolor=INK,
                 alpha=0.85, zorder=3))
    ax.text(8.5, 0.5, "m₂", ha="center", va="center", color="white",
            fontsize=13, fontweight="bold", zorder=4)
    # force on m1 (points right, toward m2)
    ax.add_patch(FancyArrowPatch((2.6, 0.5), (4.6, 0.5), arrowstyle="-|>",
                 mutation_scale=20, linewidth=3.0, color=ACCENT2, zorder=5))
    ax.text(3.6, 1.0, "F on m₁", ha="center", color=ACCENT2,
            fontsize=11, fontweight="bold")
    # force on m2 (points left, toward m1) EQUAL length
    ax.add_patch(FancyArrowPatch((7.1, 0.5), (5.1, 0.5), arrowstyle="-|>",
                 mutation_scale=20, linewidth=3.0, color=GREEN, zorder=5))
    ax.text(6.1, 1.0, "F on m₂", ha="center", color=GREEN,
            fontsize=11, fontweight="bold")
    # distance label
    ax.annotate("", xy=(8.5, -1.2), xytext=(1.5, -1.2),
                arrowprops=dict(arrowstyle="<->", color=INK, linewidth=1.2))
    ax.text(5.0, -1.6, "r (distance between centers)", ha="center",
            fontsize=10, color=INK)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Build all figures
# ---------------------------------------------------------------------------
def main():
    written = []

    # L01 — Inertia
    d = fig_dir("01_Newtons_First_Law_and_Inertia")
    written.append(free_body_diagram(
        d / "fbd_book_on_table.png",
        [("F_normal", 0, 1), ("F_gravity", 0, -1)],
        body_label="book", title="Book at rest: balanced forces (net = 0)"))
    written.append(line_graph(
        d / "vt_constant_velocity.png",
        [("velocity", [0, 1, 2, 3, 4, 5], [6, 6, 6, 6, 6, 6])],
        xlabel="time (s)", ylabel="velocity (m/s)",
        title="Zero net force → constant velocity", markers=True))

    # L02 — Second Law / Net Force
    d = fig_dir("02_Newtons_Second_Law_and_Net_Force")
    F = [0, 2, 4, 6, 8, 10]
    a = [0, 1, 2, 3, 4, 5]   # a = F/m with m = 2 kg
    written.append(line_graph(
        d / "accel_vs_net_force.png",
        [("a vs F (m = 2 kg)", F, a)],
        xlabel="net force (N)", ylabel="acceleration (m/s²)",
        title="a is proportional to net force (a = Fₙₑₜ / m)",
        markers=True))
    written.append(free_body_diagram(
        d / "fbd_unbalanced.png",
        [("F_normal", 0, 1), ("F_gravity", 0, -1),
         ("F_applied", 1.4, 0), ("friction", -0.6, 0)],
        body_label="cart",
        title="Unbalanced forces → net force → acceleration"))

    # L03 — Third Law
    d = fig_dir("03_Newtons_Third_Law_Action_and_Reaction")
    written.append(action_reaction_pair(d / "action_reaction_pair.png"))
    written.append(equal_opposite_pair(d / "equal_opposite_vectors.png"))

    # L04 — Friction
    d = fig_dir("04_Friction")
    written.append(free_body_diagram(
        d / "fbd_friction.png",
        [("F_normal", 0, 1), ("F_gravity", 0, -1),
         ("F_applied", 1.4, 0), ("f_friction", -1.0, 0)],
        body_label="box",
        title="Friction opposes the applied force"))
    # static rises to a peak, then kinetic plateau (slightly lower)
    fa = [0, 1, 2, 3, 4, 5, 5, 6, 7, 8]
    fr = [0, 1, 2, 3, 4, 5, 4.2, 4.2, 4.2, 4.2]
    written.append(line_graph(
        d / "friction_vs_applied.png",
        [("friction force", fa, fr)],
        xlabel="applied force (N)", ylabel="friction force (N)",
        title="Static peak, then kinetic plateau", markers=True))

    # L05 — Centripetal
    d = fig_dir("05_Centripetal_Force_and_Circular_Motion")
    written.append(circular_motion_diagram(d / "circular_motion.png"))
    v = np.array([2, 4, 6, 8, 10])
    v2 = (v ** 2)
    Fc = 0.5 / 1.0 * v2  # Fc = m v^2 / r, with m=0.5 kg, r=1 m -> 0.5 v^2
    written.append(line_graph(
        d / "fc_vs_vsquared.png",
        [("F_c vs v²", list(v2), list(Fc))],
        xlabel="v² (m²/s²)", ylabel="centripetal force (N)",
        title="F_c is proportional to v² (F_c = m v² / r)",
        markers=True))

    # L06 — Universal Gravitation
    d = fig_dir("06_Universal_Gravitation")
    r = np.linspace(1, 6, 60)
    Fg = 100.0 / (r ** 2)   # inverse-square, arbitrary constant
    written.append(line_graph(
        d / "fg_vs_r_inverse_square.png",
        [("F_g vs r", list(r), list(Fg))],
        xlabel="distance r (arbitrary units)", ylabel="gravitational force (N)",
        title="Inverse-square law: F_g ∝ 1 / r²", markers=False))
    written.append(two_mass_gravity(d / "two_mass_gravity.png"))

    print(f"Wrote {len(written)} figures:")
    for w in written:
        print(" ", w)


if __name__ == "__main__":
    main()
