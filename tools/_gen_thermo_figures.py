"""One-off generator: figures for Unit 05 Thermodynamics lessons.

Run from project root with the venv active:
    python tools/_gen_thermo_figures.py
"""
from __future__ import annotations
from pathlib import Path
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

from tools.figures import (
    line_graph, bar_chart,
    PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, _save,
)

UNIT = Path("Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/05_Thermodynamics")


def fig_dir(lesson: str) -> Path:
    d = UNIT / lesson / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------------------
# Custom diagrams (particles, heat-transfer modes) not in the helper library
# ---------------------------------------------------------------------------
def particle_speed_diagram(path):
    """Two boxes of particles: cool (slow, short arrows) vs hot (fast, long
    arrows). Average arrow length = average kinetic energy = temperature."""
    rng = np.random.default_rng(7)
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.6))
    titles = ["Cooler — slow particles\n(low average KE = low temperature)",
              "Hotter — fast particles\n(high average KE = high temperature)"]
    arrow_scale = [0.18, 0.42]
    colors = [BLUE, ACCENT2]
    for ax, title, scale, col in zip(axes, titles, arrow_scale, colors):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.set_aspect("equal"); ax.axis("off")
        ax.add_patch(plt.Rectangle((0.04, 0.04), 0.92, 0.84, fill=False,
                                   edgecolor=INK, linewidth=1.6))
        pts = rng.uniform(0.14, 0.78, size=(9, 2))
        angles = rng.uniform(0, 2 * np.pi, size=9)
        for (x, y), a in zip(pts, angles):
            ax.add_patch(Circle((x, y), 0.045, facecolor=col,
                                edgecolor=INK, zorder=3))
            dx, dy = scale * np.cos(a), scale * np.sin(a)
            ax.add_patch(FancyArrowPatch((x, y), (x + dx, y + dy),
                         arrowstyle="-|>", mutation_scale=11,
                         linewidth=1.8, color=INK, zorder=4))
        ax.set_title(title, fontsize=10)
    fig.suptitle("Temperature = average kinetic energy of the particles",
                 fontsize=12, fontweight="bold", y=1.02)
    fig.tight_layout()
    return _save(fig, path)


def heat_transfer_modes(path):
    """Three panels: conduction, convection, radiation."""
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 3.2))
    for ax in axes:
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.set_aspect("equal"); ax.axis("off")

    # Conduction — bar touching a flame; arrow of energy along it
    ax = axes[0]
    ax.add_patch(plt.Rectangle((0.1, 0.45), 0.8, 0.16, facecolor="#c9c9d6",
                               edgecolor=INK))
    ax.add_patch(plt.Rectangle((0.06, 0.30), 0.06, 0.45, facecolor=ACCENT2,
                               edgecolor=INK))  # heat source
    for x in (0.30, 0.50, 0.70):
        ax.add_patch(FancyArrowPatch((x, 0.53), (x + 0.12, 0.53),
                     arrowstyle="-|>", mutation_scale=12, linewidth=2.0,
                     color=PURPLE))
    ax.text(0.5, 0.10, "Conduction\n(contact, particle to particle)",
            ha="center", fontsize=9)
    ax.set_title("")

    # Convection — fluid loop arrows
    ax = axes[1]
    ax.add_patch(plt.Rectangle((0.18, 0.16), 0.64, 0.7, fill=False,
                               edgecolor=INK, linewidth=1.4))
    ax.add_patch(plt.Rectangle((0.30, 0.06), 0.4, 0.06, facecolor=ACCENT2,
                               edgecolor=INK))
    ax.add_patch(FancyArrowPatch((0.35, 0.22), (0.35, 0.78),
                 arrowstyle="-|>", mutation_scale=13, linewidth=2.2,
                 color=ACCENT2))
    ax.add_patch(FancyArrowPatch((0.65, 0.78), (0.65, 0.22),
                 arrowstyle="-|>", mutation_scale=13, linewidth=2.2,
                 color=BLUE))
    ax.text(0.5, 0.0, "Convection\n(moving fluid carries energy)",
            ha="center", fontsize=9)

    # Radiation — sun with wavy rays
    ax = axes[2]
    ax.add_patch(Circle((0.25, 0.7), 0.13, facecolor=ACCENT2, edgecolor=INK,
                        zorder=3))
    for k in range(4):
        y = 0.62 - k * 0.02
        xs = np.linspace(0.4, 0.9, 60)
        ys = y - 0.06 * k + 0.03 * np.sin((xs - 0.4) * 30)
        ax.plot(xs, ys, color=PURPLE, linewidth=1.8)
    ax.add_patch(FancyArrowPatch((0.82, 0.45), (0.92, 0.40),
                 arrowstyle="-|>", mutation_scale=12, linewidth=2.0,
                 color=PURPLE))
    ax.text(0.5, 0.05, "Radiation\n(electromagnetic waves, no medium)",
            ha="center", fontsize=9)

    fig.suptitle("Three ways thermal energy transfers", fontsize=12,
                 fontweight="bold")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Lesson 01 — Thermal Energy and Temperature
# ---------------------------------------------------------------------------
def cup_vs_pool(path):
    """Log-scale bar chart so the tiny cup bar is still visible next to the
    enormous pool bar — same temperature, hugely different thermal energy."""
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    cats = ["Cup of water\n(0.25 kg)", "Swimming pool\n(500,000 kg)"]
    vals = [3, 6_000_000]   # proportional to mass at equal temperature
    bars = ax.bar(cats, vals, 0.55, color=[BLUE, PURPLE])
    ax.set_yscale("log")
    ax.set_ylabel("total thermal energy (relative, log scale)")
    ax.set_title("Same temperature (20 °C), very different thermal energy")
    ax.grid(True, axis="y", color=GRID, linewidth=0.8)
    ax.bar_label(bars, labels=["small", "millions ×"], padding=4,
                 fontsize=10, fontweight="bold")
    return _save(fig, path)


def lesson01():
    d = fig_dir("01_Thermal_Energy_and_Temperature")
    particle_speed_diagram(d / "particle_speed.png")
    cup_vs_pool(d / "cup_vs_pool_energy.png")


# ---------------------------------------------------------------------------
# Lesson 02 — Heat Transfer and the Second Law
# ---------------------------------------------------------------------------
def lesson02():
    d = fig_dir("02_Heat_Transfer_and_the_Second_Law_of_Thermodynamics")
    t = np.linspace(0, 12, 60)
    hot = 30 + 50 * np.exp(-0.35 * t)   # starts 80, decays toward ~30
    cold = 30 - 20 * np.exp(-0.35 * t)  # starts 10, rises toward ~30
    line_graph(
        d / "approach_equilibrium.png",
        [("hot object", t, hot), ("cold object", t, cold)],
        xlabel="time (min)", ylabel="temperature (°C)",
        title="Temperatures converge to thermal equilibrium",
    )
    heat_transfer_modes(d / "heat_transfer_modes.png")


# ---------------------------------------------------------------------------
# Lesson 03 — Calorimetry / Thermal Tales
# ---------------------------------------------------------------------------
def lesson03():
    d = fig_dir("03_Calorimetry_Thermal_Tales")
    # Hot 0.20 kg @ 80C mixed with cold 0.20 kg @ 20C -> final 50C.
    t = np.linspace(0, 10, 60)
    hot = 50 + 30 * np.exp(-0.5 * t)    # 80 -> 50
    cold = 50 - 30 * np.exp(-0.5 * t)   # 20 -> 50
    line_graph(
        d / "mixing_temps.png",
        [("hot sample (starts 80 °C)", t, hot),
         ("cold sample (starts 20 °C)", t, cold)],
        xlabel="time (min)", ylabel="temperature (°C)",
        title="Mixing: both samples meet at the final temperature (50 °C)",
    )
    # Heat lost = heat gained (closed system). Equal magnitudes.
    bar_chart(
        d / "heat_lost_gained.png",
        ["Heat lost\nby hot water", "Heat gained\nby cold water"],
        [25_100, 25_100],
        ylabel="energy (J)",
        title="Closed system: heat lost = heat gained",
    )


if __name__ == "__main__":
    lesson01()
    lesson02()
    lesson03()
    print("Thermodynamics figures written.")
