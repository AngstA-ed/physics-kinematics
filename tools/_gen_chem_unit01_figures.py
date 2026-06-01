"""One-off generator: figures for Chemistry Unit 1 (Safety & Measurement).

Run from project root with the venv active:
    python tools/_gen_chem_unit01_figures.py
"""
from __future__ import annotations
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
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


def SERIES_SAFE(i):
    return [PURPLE, BLUE, ACCENT2, GREEN, "#c0392b"][i % 5]


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


def accuracy_precision_targets(path):
    """Three dartboard targets: accurate+precise, precise-not-accurate, neither."""
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
    fig.subplots_adjust(top=0.82)
    for ax, (title, openness) in zip(axes, [("ice (solid)", 0.34), ("water (liquid)", 0.22)]):
        ax.set_xlim(0, 1.15); ax.set_ylim(0, 1); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=11, fontweight="bold")
        ys = np.arange(0.15, 0.95, openness)
        xs = np.arange(0.15, 0.95, openness)
        for j, y in enumerate(ys):
            for x in xs:
                ox = (openness / 2) if j % 2 else 0
                ax.add_patch(Circle((x + ox, y), 0.05, facecolor=BLUE, edgecolor=INK))
    fig.suptitle("Ice is LESS dense than water (open lattice)", fontsize=11, fontweight="bold",
                 y=1.04)
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
