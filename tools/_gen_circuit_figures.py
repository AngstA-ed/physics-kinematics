"""Reusable circuit-schematic generator + figures for Unit 07 Current Electricity.

Run from project root with the venv active:
    python tools/_gen_circuit_figures.py

Provides small matplotlib helpers for drawing battery/resistor/wire schematics
(series, parallel) plus electromagnetism diagrams (coil field, induction), and a
main() that renders every PNG into each lesson's figures/ folder. It also reuses
line_graph / bar_chart from tools.figures for the quantitative plots.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Arc

from tools.figures import (
    line_graph, bar_chart,
    PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, _save,
)

UNIT = Path("Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/07_Current_Electricity")


def fig_dir(lesson: str) -> Path:
    d = UNIT / lesson / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------------------
# Low-level schematic primitives (coordinates in data units)
# ---------------------------------------------------------------------------
def _wire(ax, x0, y0, x1, y1, color=INK, lw=2.4):
    ax.plot([x0, x1], [y0, y1], color=color, linewidth=lw, solid_capstyle="round",
            zorder=2)


def _battery(ax, x, y, label="battery", color=PURPLE):
    """Draw a battery symbol (long + short plate) centered horizontally at (x, y),
    with the gap oriented vertically so it sits on a horizontal wire."""
    # long plate (+) on the left, short plate (-) on the right
    ax.plot([x - 0.12, x - 0.12], [y - 0.42, y + 0.42], color=color, linewidth=3.0,
            zorder=3)
    ax.plot([x + 0.12, x + 0.12], [y - 0.24, y + 0.24], color=color, linewidth=5.0,
            zorder=3)
    ax.text(x - 0.32, y + 0.5, "+", color=color, fontsize=14, fontweight="bold")
    ax.text(x + 0.22, y + 0.5, "−", color=color, fontsize=14, fontweight="bold")
    if label:
        ax.text(x, y - 0.7, label, ha="center", va="top", color=color, fontsize=10,
                fontweight="bold")


def _resistor(ax, x, y, label="R", horizontal=True, color=ACCENT2, length=1.2):
    """Draw a zig-zag resistor centered at (x, y). Returns the two terminal
    points so callers can attach wires."""
    n = 6
    half = length / 2.0
    if horizontal:
        xs = np.linspace(x - half, x + half, n + 1)
        ys = y + 0.18 * np.array([0, 1, -1, 1, -1, 1, 0])
        term0 = (x - half, y)
        term1 = (x + half, y)
        ax.text(x, y + 0.42, label, ha="center", color=color, fontsize=11,
                fontweight="bold")
    else:
        ys = np.linspace(y - half, y + half, n + 1)
        xs = x + 0.18 * np.array([0, 1, -1, 1, -1, 1, 0])
        term0 = (x, y - half)
        term1 = (x, y + half)
        ax.text(x + 0.42, y, label, va="center", color=color, fontsize=11,
                fontweight="bold")
    ax.plot(xs, ys, color=color, linewidth=2.6, zorder=3)
    return term0, term1


def _current_arrow(ax, x, y, dx, dy, label="I", color=BLUE):
    ax.add_patch(FancyArrowPatch((x, y), (x + dx, y + dy), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.2, color=color, zorder=4))
    ax.text(x + dx / 2, y + dy / 2 + 0.22, label, ha="center", color=color,
            fontsize=10, fontweight="bold")


# ---------------------------------------------------------------------------
# Lesson 01 — simple series loop: battery + one resistor
# ---------------------------------------------------------------------------
def simple_circuit(path, vlabel="V = 6 V", rlabel="R = 3 Ω", ilabel="I = 2 A"):
    fig, ax = plt.subplots(figsize=(4.8, 3.6))
    ax.set_xlim(-0.5, 5.0)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Simple circuit: one battery, one resistor")
    L, R, B, T = 0.4, 4.4, 0.4, 3.0
    # wires around the loop
    _wire(ax, L, B, L, T)          # left side
    _wire(ax, L, T, R, T)          # top
    _wire(ax, R, T, R, B)          # right side
    _wire(ax, L, B, 1.8, B)        # bottom-left to resistor
    _wire(ax, 3.0, B, R, B)        # resistor to bottom-right
    # battery on the left wire
    _battery(ax, L, (B + T) / 2, label=vlabel)
    # resistor on the bottom wire
    _resistor(ax, 2.4, B, label=rlabel)
    # current arrow (conventional, +terminal out the top): top wire, pointing right
    _current_arrow(ax, 2.0, T, 0.9, 0, label=ilabel)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Lesson 02 — a wire with length L and cross-sectional area A
# ---------------------------------------------------------------------------
def wire_dimensions(path):
    fig, ax = plt.subplots(figsize=(6.2, 2.8))
    ax.set_xlim(-0.5, 8.0)
    ax.set_ylim(-1.4, 1.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Resistance of a wire depends on length L and area A")
    # the wire (a long thin cylinder shown as a rectangle)
    ax.add_patch(Rectangle((1.0, -0.35), 5.0, 0.7, facecolor=ACCENT2,
                 edgecolor=INK, alpha=0.85, zorder=3))
    # end cap to suggest cross-sectional area
    ax.add_patch(Circle((6.0, 0.0), 0.35, facecolor=BLUE, edgecolor=INK,
                 alpha=0.9, zorder=4))
    ax.text(6.0, 0.0, "A", ha="center", va="center", color="white",
            fontsize=11, fontweight="bold", zorder=5)
    # length dimension
    ax.annotate("", xy=(6.0, -0.95), xytext=(1.0, -0.95),
                arrowprops=dict(arrowstyle="<->", color=INK, linewidth=1.4))
    ax.text(3.5, -1.25, "length L", ha="center", color=INK, fontsize=11)
    ax.text(6.9, 0.0, "cross-sectional\narea A", va="center", color=BLUE,
            fontsize=10, fontweight="bold")
    ax.text(3.5, 0.95, "material: resistivity ρ", ha="center", color=ACCENT2,
            fontsize=11, fontweight="bold")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Lesson 03 — three resistors in series
# ---------------------------------------------------------------------------
def series_circuit(path, labels=("R₁ = 2 Ω", "R₂ = 3 Ω", "R₃ = 5 Ω"),
                   vlabel="V = 20 V"):
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Series circuit: one path, resistors in a row")
    L, R, B, T = 0.4, 6.0, 0.4, 3.0
    _wire(ax, L, B, L, T)          # left side (battery)
    _wire(ax, L, T, R, T)          # top wire holds the three resistors
    _wire(ax, R, T, R, B)          # right side
    _wire(ax, L, B, R, B)          # bottom return
    _battery(ax, L, (B + T) / 2, label=vlabel)
    # three resistors along the top
    xs = [1.6, 3.2, 4.8]
    for x, lbl in zip(xs, labels):
        _resistor(ax, x, T, label=lbl)
    # current is the SAME everywhere — one arrow on the bottom return
    _current_arrow(ax, 3.6, B, -1.0, 0, label="I (same everywhere)")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Lesson 04 — three resistors in parallel
# ---------------------------------------------------------------------------
def parallel_circuit(path, labels=("R₁ = 6 Ω", "R₂ = 3 Ω", "R₃ = 2 Ω"),
                     vlabel="V = 12 V"):
    fig, ax = plt.subplots(figsize=(5.8, 4.0))
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.8, 4.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Parallel circuit: branches share the same voltage")
    L, B, T = 0.4, 0.2, 3.4
    # battery on the left
    _battery(ax, L, (B + T) / 2, label=vlabel)
    _wire(ax, L, B, L, T)
    # top and bottom rails
    railR = 6.0
    _wire(ax, L, T, railR, T)
    _wire(ax, L, B, railR, B)
    # three vertical branches
    xs = [2.2, 3.6, 5.0]
    for x, lbl in zip(xs, labels):
        _resistor(ax, x, (B + T) / 2, label=lbl, horizontal=False, length=1.3)
        _wire(ax, x, T, x, (B + T) / 2 + 0.65)
        _wire(ax, x, (B + T) / 2 - 0.65, x, B)
    # total current splits into branch currents (arrows down each branch)
    _current_arrow(ax, L + 0.4, T, 0.9, 0, label="I_total")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Lesson 05 — coil with magnetic field; magnet-through-coil induction
# ---------------------------------------------------------------------------
def coil_field(path):
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.set_xlim(-1.0, 7.0)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Current in a coil creates a magnetic field (electromagnet)")
    # coil: several loops drawn as ellipses along an axis
    for i, x in enumerate([1.2, 1.9, 2.6, 3.3, 4.0]):
        ax.add_patch(Arc((x, 0), 0.5, 2.0, theta1=0, theta2=360,
                     edgecolor=ACCENT2, linewidth=2.4))
    # wires to a battery on the left
    _wire(ax, -0.6, -1.6, -0.6, 1.0)
    _wire(ax, -0.6, 1.0, 1.0, 0.9)
    _wire(ax, -0.6, -1.6, 4.2, -1.6)
    _wire(ax, 4.2, -1.6, 4.2, -0.9)
    _battery(ax, -0.6, -0.3, label="")
    ax.text(-0.95, -1.2, "battery", color=PURPLE, fontsize=9, rotation=90,
            va="center")
    # field lines through the coil (axis arrows = like a bar magnet N/S)
    ax.add_patch(FancyArrowPatch((4.4, 0), (6.4, 0), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.6, color=BLUE, zorder=5))
    ax.add_patch(FancyArrowPatch((0.8, 0), (-0.0, 0), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.6, color=BLUE, zorder=5))
    ax.text(5.6, 0.35, "B (field)", color=BLUE, fontsize=11, fontweight="bold")
    ax.text(6.0, -0.45, "N", color=INK, fontsize=12, fontweight="bold")
    ax.text(-0.4, -0.45, "S", color=INK, fontsize=12, fontweight="bold")
    return _save(fig, path)


def induction_diagram(path):
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    ax.set_xlim(-1.0, 7.0)
    ax.set_ylim(-2.2, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Moving a magnet through a coil induces a current")
    # coil on the right, connected to a galvanometer / LED loop
    for x in [3.6, 4.3, 5.0]:
        ax.add_patch(Arc((x, 0), 0.5, 1.9, theta1=0, theta2=360,
                     edgecolor=ACCENT2, linewidth=2.4))
    # leads down to an LED loop
    _wire(ax, 3.4, -0.95, 3.4, -1.7)
    _wire(ax, 5.2, -0.95, 5.2, -1.7)
    _wire(ax, 3.4, -1.7, 5.2, -1.7)
    ax.add_patch(Circle((4.3, -1.7), 0.22, facecolor=GREEN, edgecolor=INK, zorder=4))
    ax.text(4.3, -1.7, "LED", ha="center", va="center", color="white",
            fontsize=7, fontweight="bold", zorder=5)
    # bar magnet moving toward the coil
    ax.add_patch(Rectangle((0.2, -0.35), 1.6, 0.7, facecolor=PURPLE,
                 edgecolor=INK, alpha=0.85, zorder=3))
    ax.text(0.55, 0.0, "N", ha="center", va="center", color="white",
            fontsize=12, fontweight="bold", zorder=4)
    ax.text(1.45, 0.0, "S", ha="center", va="center", color="white",
            fontsize=12, fontweight="bold", zorder=4)
    # motion arrow
    ax.add_patch(FancyArrowPatch((2.0, 0.0), (3.0, 0.0), arrowstyle="-|>",
                 mutation_scale=18, linewidth=2.6, color=BLUE, zorder=5))
    ax.text(2.5, 0.4, "move", ha="center", color=BLUE, fontsize=10,
            fontweight="bold")
    ax.text(4.3, 1.4, "changing field → induced current",
            ha="center", color=INK, fontsize=10)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Build all figures
# ---------------------------------------------------------------------------
def main():
    written = []

    # ---- L01: Electric Current and Ohm's Law ----
    d = fig_dir("01_Electric_Current_and_Ohms_Law")
    # V vs I: linear, slope = R = 3 ohm
    I = [0, 1, 2, 3, 4]
    V = [3 * i for i in I]
    written.append(line_graph(
        d / "v_vs_i.png",
        [("V vs I (slope = R = 3 Ω)", I, V)],
        xlabel="current I (A)", ylabel="potential difference V (V)",
        title="Ohm's Law: V is proportional to I (slope = R)", markers=True))
    written.append(simple_circuit(d / "simple_circuit.png"))

    # ---- L02: Resistance in a Wire ----
    d = fig_dir("02_Resistance_in_a_Wire")
    # R vs length (linear, increasing)
    Lx = [1, 2, 3, 4, 5]
    Rl = [2 * x for x in Lx]
    written.append(line_graph(
        d / "r_vs_length.png",
        [("R vs length", Lx, Rl)],
        xlabel="length L (m)", ylabel="resistance R (Ω)",
        title="Longer wire → more resistance (R ∝ L)", markers=True))
    # R vs area (bar chart: thicker wire -> lower R)
    written.append(bar_chart(
        d / "r_vs_area.png",
        ["A", "2A", "3A", "4A"], [12, 6, 4, 3],
        ylabel="resistance R (Ω)",
        title="Bigger cross-section → less resistance (R ∝ 1/A)"))
    written.append(wire_dimensions(d / "wire_dimensions.png"))

    # ---- L03: Series Circuits ----
    d = fig_dir("03_Series_Circuits")
    written.append(series_circuit(d / "series_circuit.png"))
    # voltage drops add to source: 4 V + 6 V + 10 V = 20 V
    written.append(bar_chart(
        d / "series_voltage_drops.png",
        ["R₁ (2Ω)", "R₂ (3Ω)", "R₃ (5Ω)", "Source"],
        [4, 6, 10, 20],
        ylabel="voltage (V)",
        title="Series: voltage drops add up to the source (4+6+10 = 20 V)"))

    # ---- L04: Parallel Circuits ----
    d = fig_dir("04_Parallel_Circuits")
    written.append(parallel_circuit(d / "parallel_circuit.png"))
    # branch currents add to total: 2 A + 4 A + 6 A = 12 A
    written.append(bar_chart(
        d / "parallel_branch_currents.png",
        ["R₁ (6Ω)", "R₂ (3Ω)", "R₃ (2Ω)", "Total"],
        [2, 4, 6, 12],
        ylabel="current (A)",
        title="Parallel: branch currents add up to the total (2+4+6 = 12 A)"))

    # ---- L05: Electromagnetism / Induction ----
    d = fig_dir("05_Electromagnetism_Induction_Junction")
    written.append(coil_field(d / "coil_field.png"))
    written.append(induction_diagram(d / "induction_diagram.png"))

    print(f"Wrote {len(written)} figures:")
    for w in written:
        print(" ", w)


if __name__ == "__main__":
    main()
