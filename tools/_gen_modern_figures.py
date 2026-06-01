"""One-off generator: figures for Unit 09 Modern Physics lessons.

Run from project root with the venv active:
    python tools/_gen_modern_figures.py

Covers the diagrams the shared figure library does not: atomic-model
progression, gold-foil scattering, energy-level transitions, line spectra,
the Standard-Model particle chart, a proton = uud diagram, fission/fusion
side-by-side, and an alpha/beta/gamma decay diagram. Quantitative graphs
(photon energy vs frequency) use the shared `line_graph` helper.
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
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle, FancyBboxPatch

from tools.figures import (
    line_graph,
    PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, _save,
)

UNIT = Path("Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/09_Modern_Physics")


def fig_dir(lesson: str) -> Path:
    d = UNIT / lesson / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------------------
# L01 — Photoelectric effect
# ---------------------------------------------------------------------------
def photon_ejects_electron(path):
    """An incoming photon strikes a metal surface and an electron flies off."""
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.set_xlim(0, 11)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("A photon above threshold ejects an electron")
    # metal surface
    ax.add_patch(Rectangle((6.5, -0.6), 4.0, 2.6, facecolor="#b0b0b8",
                 edgecolor=INK, zorder=2))
    ax.text(8.5, 0.7, "metal surface", ha="center", va="center",
            color=INK, fontsize=10, fontweight="bold")
    # bound electrons in the metal
    for x in (7.2, 7.9, 8.6, 9.3, 10.0):
        ax.add_patch(Circle((x, 1.5), 0.16, facecolor=BLUE, edgecolor=INK, zorder=3))
    # incoming photon (wavy arrow) from upper left
    xs = np.linspace(0.6, 6.4, 100)
    ys = 4.0 - 0.45 * (xs - 0.6) + 0.18 * np.sin(xs * 6)
    ax.plot(xs, ys, color=ACCENT2, linewidth=2.4, zorder=4)
    ax.add_patch(FancyArrowPatch((6.0, ys[-6]), (6.55, 1.7), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=ACCENT2, zorder=4))
    ax.text(1.6, 4.2, "photon  E = h·f", color=ACCENT2, fontsize=11,
            fontweight="bold")
    # ejected electron flies up-right
    ax.add_patch(Circle((7.2, 1.5), 0.16, facecolor=GREEN, edgecolor=INK, zorder=5))
    ax.add_patch(FancyArrowPatch((7.4, 1.7), (9.6, 4.3), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=GREEN, zorder=5))
    ax.text(8.9, 4.4, "ejected electron", color=GREEN, fontsize=11,
            fontweight="bold")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L02 — Models of the atom
# ---------------------------------------------------------------------------
def atomic_model_progression(path):
    """Five-panel progression: Dalton, Thomson, Rutherford, Bohr, Quantum."""
    fig, axes = plt.subplots(1, 5, figsize=(13.5, 3.2))
    titles = ["Dalton (1803)\nsolid sphere",
              "Thomson (1904)\nplum pudding",
              "Rutherford (1911)\nnucleus + space",
              "Bohr (1913)\nfixed orbits",
              "Quantum (1926)\nelectron cloud"]
    for ax, t in zip(axes, titles):
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(t, fontsize=10)

    # Dalton: solid sphere
    axes[0].add_patch(Circle((0, 0), 0.9, facecolor=PURPLE, edgecolor=INK, alpha=0.9))

    # Thomson: positive blob with embedded electrons
    axes[1].add_patch(Circle((0, 0), 0.95, facecolor="#f2c6e0", edgecolor=INK))
    for (x, y) in [(-0.4, 0.3), (0.4, 0.35), (0.0, -0.4), (0.5, -0.2), (-0.45, -0.3), (0.1, 0.5)]:
        axes[1].add_patch(Circle((x, y), 0.11, facecolor=BLUE, edgecolor=INK))

    # Rutherford: tiny nucleus, mostly empty space, scattered electrons
    axes[2].add_patch(Circle((0, 0), 0.95, fill=False, edgecolor=GRID,
                      linewidth=1.2, linestyle=":"))
    axes[2].add_patch(Circle((0, 0), 0.13, facecolor=ACCENT2, edgecolor=INK))
    axes[2].text(0, -0.42, "nucleus", ha="center", fontsize=7, color=ACCENT2)
    for (x, y) in [(-0.6, 0.5), (0.65, 0.4), (-0.5, -0.6), (0.55, -0.5)]:
        axes[2].add_patch(Circle((x, y), 0.08, facecolor=BLUE, edgecolor=INK))

    # Bohr: nucleus + circular orbits with electrons
    axes[3].add_patch(Circle((0, 0), 0.13, facecolor=ACCENT2, edgecolor=INK))
    for r in (0.45, 0.8):
        axes[3].add_patch(Circle((0, 0), r, fill=False, edgecolor=PURPLE, linewidth=1.4))
    axes[3].add_patch(Circle((0.45, 0), 0.08, facecolor=BLUE, edgecolor=INK))
    axes[3].add_patch(Circle((0, 0.8), 0.08, facecolor=BLUE, edgecolor=INK))

    # Quantum: fuzzy probability cloud
    rng = np.random.default_rng(7)
    n = 1400
    rr = np.abs(rng.normal(0, 0.45, n))
    th = rng.uniform(0, 2 * np.pi, n)
    axes[4].scatter(rr * np.cos(th), rr * np.sin(th), s=2, color=BLUE, alpha=0.25)
    axes[4].add_patch(Circle((0, 0), 0.1, facecolor=ACCENT2, edgecolor=INK, zorder=5))

    fig.suptitle("The atomic model changed as new evidence appeared",
                 fontsize=13, fontweight="bold", y=1.02)
    return _save(fig, path)


def gold_foil_scattering(path):
    """Rutherford's gold-foil experiment: most alphas pass through, a few
    deflect sharply off the tiny dense nucleus."""
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(-1, 5)
    ax.axis("off")
    ax.set_title("Gold-foil scattering: most pass straight through; a few bounce back")
    # source
    ax.add_patch(Rectangle((0.2, 1.6), 1.2, 0.8, facecolor="#888", edgecolor=INK))
    ax.text(0.8, 2.0, "α\nsource", ha="center", va="center", color="white",
            fontsize=8, fontweight="bold")
    # foil
    ax.add_patch(Rectangle((6.0, -0.4), 0.25, 4.8, facecolor=ACCENT2,
                 edgecolor=INK, alpha=0.7))
    ax.text(6.1, 4.6, "gold foil", ha="center", fontsize=9, color=ACCENT2)
    # nucleus inside foil
    ax.add_patch(Circle((6.12, 2.0), 0.12, facecolor=PURPLE, edgecolor=INK, zorder=5))
    ax.text(6.12, 1.5, "nucleus", ha="center", fontsize=7, color=PURPLE)
    # straight-through paths
    for y in (0.6, 1.3, 2.7, 3.4):
        ax.add_patch(FancyArrowPatch((1.5, y), (11.2, y), arrowstyle="-|>",
                     mutation_scale=12, linewidth=1.6, color=GREEN, zorder=3))
    # one deflected path
    ax.add_patch(FancyArrowPatch((1.5, 2.0), (6.0, 2.0), arrowstyle="-",
                 mutation_scale=12, linewidth=1.8, color=BLUE, zorder=3))
    ax.add_patch(FancyArrowPatch((6.05, 2.0), (3.0, 4.3), arrowstyle="-|>",
                 mutation_scale=14, linewidth=2.2, color=BLUE, zorder=4))
    ax.text(9.0, 3.7, "most pass straight through", color=GREEN, fontsize=9,
            fontweight="bold")
    ax.text(1.8, 4.4, "a few bounce back sharply", color=BLUE, fontsize=9,
            fontweight="bold")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L03 — Energy levels & spectra
# ---------------------------------------------------------------------------
def energy_level_diagram(path):
    """Discrete energy levels with an absorption (up) and emission (down)
    transition; emitted photon carries the energy difference."""
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Energy levels: a photon = a jump between levels")
    levels = {"n = 1": 1.2, "n = 2": 4.6, "n = 3": 6.8, "n = 4": 8.2}
    for name, y in levels.items():
        ax.plot([1.5, 8.5], [y, y], color=INK, linewidth=2.2)
        ax.text(8.7, y, name, va="center", fontsize=10, color=INK)
    ax.text(0.2, 9.4, "energy", fontsize=10, color=INK, fontweight="bold", rotation=90)
    # absorption: n=1 -> n=3 (photon absorbed, electron jumps up)
    ax.add_patch(FancyArrowPatch((3.2, 1.2), (3.2, 6.8), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=BLUE))
    ax.text(2.0, 4.0, "absorb\nphoton", color=BLUE, fontsize=9, fontweight="bold",
            ha="center")
    # emission: n=3 -> n=1 (photon emitted)
    ax.add_patch(FancyArrowPatch((6.0, 6.8), (6.0, 1.2), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=ACCENT2))
    ax.text(7.0, 4.0, "emit\nphoton\nE = h·f", color=ACCENT2, fontsize=9,
            fontweight="bold", ha="center")
    return _save(fig, path)


def line_spectrum_strip(path):
    """A black strip with a few bright colored emission lines — an element
    'fingerprint' — compared with a continuous rainbow band."""
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.0, 2.8))
    # continuous spectrum (rainbow gradient)
    grad = np.linspace(0, 1, 256).reshape(1, -1)
    a1.imshow(grad, aspect="auto", cmap="rainbow", extent=[400, 700, 0, 1])
    a1.set_yticks([])
    a1.set_title("Continuous spectrum (hot solid / white light)", fontsize=10)
    a1.set_xlabel("wavelength (nm)")

    # emission line spectrum: black with a few bright lines (hydrogen-like)
    a2.set_facecolor("black")
    a2.set_xlim(400, 700)
    a2.set_ylim(0, 1)
    a2.set_yticks([])
    lines_nm = {410: "#8b00ff", 434: "#4b0fd6", 486: "#1fa3ff", 656: "#ff2b2b"}
    for nm, c in lines_nm.items():
        a2.axvline(nm, color=c, linewidth=3.0)
    a2.set_title("Emission line spectrum (hydrogen) — an element fingerprint",
                 fontsize=10)
    a2.set_xlabel("wavelength (nm)")
    fig.tight_layout()
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L04 — Standard Model
# ---------------------------------------------------------------------------
def standard_model_chart(path):
    """Simplified Standard-Model grid: quarks, leptons, force-carrier bosons."""
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 7)
    ax.axis("off")
    ax.set_title("The Standard Model: matter particles + force carriers")

    def tile(x, y, label, color):
        ax.add_patch(FancyBboxPatch((x, y), 1.4, 0.95,
                     boxstyle="round,pad=0.02,rounding_size=0.08",
                     facecolor=color, edgecolor=INK, alpha=0.9))
        ax.text(x + 0.7, y + 0.475, label, ha="center", va="center",
                color="white", fontsize=9, fontweight="bold")

    # Quarks block (top-left, 2 rows x 3 cols)
    ax.text(0.2, 6.55, "QUARKS (matter)", fontsize=11, fontweight="bold", color=PURPLE)
    quarks = ["up", "charm", "top", "down", "strange", "bottom"]
    for i, q in enumerate(quarks):
        col, row = i % 3, i // 3
        tile(0.2 + col * 1.55, 5.2 - row * 1.1, q, PURPLE)

    # Leptons block (lower-left, 2 rows x 3 cols)
    ax.text(0.2, 2.85, "LEPTONS (matter)", fontsize=11, fontweight="bold", color=BLUE)
    leptons = ["electron", "muon", "tau", "e neutrino", "mu neutrino", "tau neutrino"]
    for i, lp in enumerate(leptons):
        col, row = i % 3, i // 3
        tile(0.2 + col * 1.55, 1.5 - row * 1.1, lp, BLUE)

    # Bosons block (right column)
    ax.text(5.6, 6.55, "BOSONS (forces)", fontsize=11, fontweight="bold", color=GREEN)
    bosons = ["photon", "gluon", "W boson", "Z boson", "Higgs"]
    for i, b in enumerate(bosons):
        tile(5.9, 5.2 - i * 1.1, b, GREEN)
    return _save(fig, path)


def proton_quark_diagram(path):
    """A proton drawn as three quarks: up, up, down."""
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("A proton = two up quarks + one down quark (uud)")
    # proton boundary
    ax.add_patch(Circle((0, 0), 1.5, fill=False, edgecolor=GRID,
                 linewidth=2.0, linestyle="--"))
    quarks = [("u", -0.7, 0.55, PURPLE), ("u", 0.7, 0.55, PURPLE),
              ("d", 0.0, -0.7, ACCENT2)]
    # gluon "springs" connecting them
    pts = [(-0.7, 0.55), (0.7, 0.55), (0.0, -0.7)]
    for (x1, y1), (x2, y2) in [(pts[0], pts[1]), (pts[1], pts[2]), (pts[2], pts[0])]:
        ax.plot([x1, x2], [y1, y2], color=GREEN, linewidth=1.6, linestyle=":", zorder=1)
    for label, x, y, c in quarks:
        ax.add_patch(Circle((x, y), 0.45, facecolor=c, edgecolor=INK, zorder=3))
        ax.text(x, y, label, ha="center", va="center", color="white",
                fontsize=16, fontweight="bold", zorder=4)
    ax.text(0, -1.85, "charge: +⅔ +⅔ −⅓ = +1", ha="center", fontsize=10, color=INK)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L05 — Fission / fusion / decay
# ---------------------------------------------------------------------------
def fission_fusion_diagram(path):
    """Side-by-side: fission (heavy nucleus splits) and fusion (light nuclei
    combine). Both release energy."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.8))
    for ax in (a1, a2):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect("equal")
        ax.axis("off")

    # --- Fission ---
    a1.set_title("Fission: a heavy nucleus splits")
    a1.add_patch(Circle((1.6, 4), 0.25, facecolor=BLUE, edgecolor=INK, zorder=4))
    a1.add_patch(FancyArrowPatch((0.3, 4), (3.4, 4), arrowstyle="-|>",
                 mutation_scale=14, linewidth=2.0, color=BLUE, zorder=3))
    a1.text(0.2, 4.5, "neutron", color=BLUE, fontsize=9, fontweight="bold")
    a1.add_patch(Circle((4.4, 4), 1.0, facecolor=PURPLE, edgecolor=INK, alpha=0.9))
    a1.text(4.4, 4, "heavy\nnucleus", ha="center", va="center", color="white",
            fontsize=8, fontweight="bold")
    a1.add_patch(FancyArrowPatch((5.5, 4), (6.6, 4), arrowstyle="-|>",
                 mutation_scale=14, linewidth=2.0, color=INK))
    a1.add_patch(Circle((7.6, 5.4), 0.6, facecolor=ACCENT2, edgecolor=INK))
    a1.add_patch(Circle((7.6, 2.6), 0.6, facecolor=ACCENT2, edgecolor=INK))
    a1.text(8.8, 5.4, "two lighter\nnuclei", color=ACCENT2, fontsize=8, fontweight="bold")
    for dx, dy in [(1.0, 0.7), (1.0, -0.7), (0.6, 1.2)]:
        a1.add_patch(FancyArrowPatch((8.4, 4), (8.4 + dx, 4 + dy),
                     arrowstyle="-|>", mutation_scale=10, linewidth=1.4, color=BLUE))
    a1.text(5.0, 0.6, "+ energy (E = m c²)", ha="center", color=GREEN,
            fontsize=10, fontweight="bold")

    # --- Fusion ---
    a2.set_title("Fusion: light nuclei combine (powers stars)")
    a2.add_patch(Circle((1.6, 5.2), 0.55, facecolor=PURPLE, edgecolor=INK))
    a2.add_patch(Circle((1.6, 2.8), 0.55, facecolor=PURPLE, edgecolor=INK))
    a2.text(0.2, 5.2, "small\nnuclei", color=PURPLE, fontsize=8, fontweight="bold")
    a2.add_patch(FancyArrowPatch((2.3, 5.0), (3.6, 4.3), arrowstyle="-|>",
                 mutation_scale=12, linewidth=1.8, color=INK))
    a2.add_patch(FancyArrowPatch((2.3, 3.0), (3.6, 3.7), arrowstyle="-|>",
                 mutation_scale=12, linewidth=1.8, color=INK))
    a2.add_patch(Circle((5.0, 4), 0.95, facecolor=ACCENT2, edgecolor=INK, alpha=0.9))
    a2.text(5.0, 4, "heavier\nnucleus", ha="center", va="center", color="white",
            fontsize=8, fontweight="bold")
    for dx, dy in [(1.2, 0.9), (1.3, 0.0), (1.2, -0.9)]:
        a2.add_patch(FancyArrowPatch((5.9, 4), (5.9 + dx, 4 + dy),
                     arrowstyle="-|>", mutation_scale=10, linewidth=1.4, color=GREEN))
    a2.text(5.0, 0.6, "+ enormous energy", ha="center", color=GREEN,
            fontsize=10, fontweight="bold")
    return _save(fig, path)


def decay_diagram(path):
    """Alpha, beta, and gamma decay shown as three rows."""
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.set_title("Three kinds of radioactive decay")

    def nucleus(x, y, r, label, color):
        ax.add_patch(Circle((x, y), r, facecolor=color, edgecolor=INK, alpha=0.9))
        ax.text(x, y, label, ha="center", va="center", color="white",
                fontsize=8, fontweight="bold")

    # Alpha (top)
    ax.text(0.2, 8.4, "Alpha (α): emits a helium nucleus (2 p + 2 n)",
            fontsize=10, color=PURPLE, fontweight="bold")
    nucleus(2.0, 7.2, 0.8, "parent", PURPLE)
    ax.add_patch(FancyArrowPatch((2.9, 7.2), (4.2, 7.2), arrowstyle="-|>",
                 mutation_scale=14, linewidth=2.0, color=INK))
    nucleus(5.2, 7.2, 0.7, "daughter", BLUE)
    ax.add_patch(Circle((7.4, 7.2), 0.35, facecolor=ACCENT2, edgecolor=INK))
    ax.text(7.4, 7.2, "α", ha="center", va="center", color="white",
            fontsize=10, fontweight="bold")
    ax.add_patch(FancyArrowPatch((7.8, 7.2), (9.2, 7.8), arrowstyle="-|>",
                 mutation_scale=12, linewidth=1.6, color=ACCENT2))

    # Beta (middle)
    ax.text(0.2, 5.4, "Beta (β): a neutron becomes a proton + emits an electron",
            fontsize=10, color=BLUE, fontweight="bold")
    nucleus(2.0, 4.2, 0.8, "parent", PURPLE)
    ax.add_patch(FancyArrowPatch((2.9, 4.2), (4.2, 4.2), arrowstyle="-|>",
                 mutation_scale=14, linewidth=2.0, color=INK))
    nucleus(5.2, 4.2, 0.8, "daughter", BLUE)
    ax.add_patch(Circle((7.4, 4.2), 0.22, facecolor=GREEN, edgecolor=INK))
    ax.text(7.9, 4.2, "β⁻ (electron)", color=GREEN, fontsize=9, fontweight="bold")
    ax.add_patch(FancyArrowPatch((7.6, 4.2), (9.0, 4.8), arrowstyle="-|>",
                 mutation_scale=12, linewidth=1.6, color=GREEN))

    # Gamma (bottom)
    ax.text(0.2, 2.4, "Gamma (γ): an excited nucleus releases a high-energy photon",
            fontsize=10, color=ACCENT2, fontweight="bold")
    nucleus(2.0, 1.2, 0.8, "excited", PURPLE)
    ax.add_patch(FancyArrowPatch((2.9, 1.2), (4.2, 1.2), arrowstyle="-|>",
                 mutation_scale=14, linewidth=2.0, color=INK))
    nucleus(5.2, 1.2, 0.8, "stable", BLUE)
    xs = np.linspace(6.2, 9.6, 80)
    ys = 1.2 + 0.22 * np.sin(xs * 7)
    ax.plot(xs, ys, color=ACCENT2, linewidth=2.2)
    ax.text(8.0, 2.0, "γ photon", color=ACCENT2, fontsize=9, fontweight="bold")
    return _save(fig, path)


# ---------------------------------------------------------------------------
def main():
    written = []

    # L01 — Photoelectric Effect
    d = fig_dir("01_The_Photoelectric_Effect")
    # Ejected-electron (max kinetic) energy vs frequency: zero below threshold,
    # linear above it. f in units of 1e14 Hz; threshold at f0 = 5.0e14.
    f0 = 5.0
    f = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # ×10^14 Hz
    ke = np.clip((f - f0) * 0.41, 0, None)          # eV, slope ~ h
    written.append(line_graph(
        d / "ke_vs_frequency.png",
        [("max electron energy", list(f), list(ke))],
        xlabel="light frequency (×10¹⁴ Hz)",
        ylabel="max electron energy (eV)",
        title="No electrons below threshold f₀; energy rises linearly above it",
        markers=True))
    written.append(photon_ejects_electron(d / "photon_ejects_electron.png"))

    # L02 — Models of the Atom
    d = fig_dir("02_Models_of_the_Atom")
    written.append(atomic_model_progression(d / "atomic_model_progression.png"))
    written.append(gold_foil_scattering(d / "gold_foil_scattering.png"))

    # L03 — Energy levels & spectra
    d = fig_dir("03_Energy_Level_Diagrams_and_Spectra")
    written.append(energy_level_diagram(d / "energy_level_diagram.png"))
    written.append(line_spectrum_strip(d / "line_spectrum_strip.png"))

    # L04 — Standard Model
    d = fig_dir("04_The_Standard_Model")
    written.append(standard_model_chart(d / "standard_model_chart.png"))
    written.append(proton_quark_diagram(d / "proton_quark_diagram.png"))

    # L05 — Fusion / fission / decay
    d = fig_dir("05_Fusion_Fission_and_Radioactive_Decay")
    written.append(fission_fusion_diagram(d / "fission_fusion_diagram.png"))
    written.append(decay_diagram(d / "decay_diagram.png"))

    print(f"Wrote {len(written)} figures:")
    for w in written:
        print(" ", w)


if __name__ == "__main__":
    main()
