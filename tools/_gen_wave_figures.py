"""Reusable generator: figures for Unit 08 Waves & Sound lessons.

Run from project root with the venv active:
    python tools/_gen_wave_figures.py

Produces wave snapshots, transverse/longitudinal diagrams, standing-wave
harmonics, interference (constructive/destructive), Doppler wavefronts, the
EM spectrum band chart, refraction/optics ray diagrams, and analog-vs-digital
sampling figures. Also calls the shared helpers (line_graph) where a clean
plot is the right tool.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, Circle, Arc

from tools.figures import (
    line_graph,
    PURPLE, BLUE, INK, GRID, ACCENT2, GREEN, SERIES, _prep, _save,
)

UNIT = Path("Publisher_Ready_Curriculum/01_Physics_East_Meadow_Refactor/08_Waves")


def fig_dir(lesson: str) -> Path:
    d = UNIT / lesson / "figures"
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------------------
# L01 — Wave anatomy
# ---------------------------------------------------------------------------
def labeled_sine_wave(path):
    """A sine wave with amplitude, wavelength, crest, trough, and rest line
    annotated."""
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    x = np.linspace(0, 4 * np.pi, 800)
    A = 1.0
    y = A * np.sin(x)
    ax.plot(x, y, color=PURPLE, linewidth=2.6)
    ax.axhline(0, color=INK, linewidth=1.0, linestyle="--")
    ax.text(4 * np.pi, 0.06, " rest position", fontsize=10, color=INK, va="bottom", ha="right")

    # Crest and trough markers
    crest_x = np.pi / 2
    trough_x = 3 * np.pi / 2
    ax.plot(crest_x, A, marker="o", color=ACCENT2, markersize=8, zorder=5)
    ax.text(crest_x, A + 0.12, "crest", color=ACCENT2, fontsize=11,
            fontweight="bold", ha="center")
    ax.plot(trough_x, -A, marker="o", color=GREEN, markersize=8, zorder=5)
    ax.text(trough_x, -A - 0.2, "trough", color=GREEN, fontsize=11,
            fontweight="bold", ha="center")

    # Amplitude arrow (rest to crest)
    ax.add_patch(FancyArrowPatch((crest_x + 0.55, 0), (crest_x + 0.55, A),
                 arrowstyle="<->", mutation_scale=14, linewidth=2.0, color=BLUE))
    ax.text(crest_x + 0.75, A / 2, "amplitude", color=BLUE, fontsize=11,
            fontweight="bold", va="center")

    # Wavelength arrow (crest to crest)
    next_crest = crest_x + 2 * np.pi
    ax.add_patch(FancyArrowPatch((crest_x, A + 0.45), (next_crest, A + 0.45),
                 arrowstyle="<->", mutation_scale=14, linewidth=2.0, color=INK))
    ax.text((crest_x + next_crest) / 2, A + 0.58, "wavelength  λ",
            color=INK, fontsize=11, fontweight="bold", ha="center")

    ax.set_xlim(-0.2, 4 * np.pi + 0.2)
    ax.set_ylim(-1.5, 1.9)
    ax.set_xlabel("distance along the wave →")
    ax.set_yticks([])
    ax.set_title("Anatomy of a wave")
    return _save(fig, path)


def frequency_period_illustration(path):
    """Two waves: low frequency (long period) vs high frequency (short period),
    same amplitude, over the same time window."""
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    t = np.linspace(0, 2.0, 800)
    low = np.sin(2 * np.pi * 1.0 * t)   # 1 Hz
    high = np.sin(2 * np.pi * 3.0 * t)  # 3 Hz
    ax.plot(t, low + 1.4, color=BLUE, linewidth=2.4, label="low frequency (1 Hz)")
    ax.plot(t, high - 1.4, color=ACCENT2, linewidth=2.4, label="high frequency (3 Hz)")
    ax.axhline(1.4, color=GRID, linewidth=0.8)
    ax.axhline(-1.4, color=GRID, linewidth=0.8)

    # period bracket on the low wave (1 full cycle = 1 s)
    ax.add_patch(FancyArrowPatch((0.0, 2.7), (1.0, 2.7), arrowstyle="<->",
                 mutation_scale=12, linewidth=1.8, color=BLUE))
    ax.text(0.5, 2.9, "T = 1 s (one cycle)", color=BLUE, fontsize=10,
            fontweight="bold", ha="center")
    # period bracket on the high wave (1 full cycle = 0.333 s)
    ax.add_patch(FancyArrowPatch((0.0, -2.7), (1 / 3, -2.7), arrowstyle="<->",
                 mutation_scale=12, linewidth=1.8, color=ACCENT2))
    ax.text(1 / 3 + 0.02, -3.0, "T = 0.33 s", color=ACCENT2, fontsize=10,
            fontweight="bold", ha="left")

    ax.set_xlim(0, 2.0)
    ax.set_ylim(-3.5, 3.4)
    ax.set_xlabel("time (s)")
    ax.set_yticks([])
    ax.set_title("More cycles per second = higher frequency = shorter period")
    ax.legend(frameon=False, fontsize=9, loc="center right")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L02 — Transverse vs longitudinal
# ---------------------------------------------------------------------------
def transverse_vs_longitudinal(path):
    """Side-by-side: transverse sine (oscillation perpendicular to travel) vs
    longitudinal compressions/rarefactions (oscillation parallel to travel)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 5.4))

    # --- Transverse ---
    x = np.linspace(0, 4 * np.pi, 600)
    ax1.plot(x, np.sin(x), color=PURPLE, linewidth=2.6)
    ax1.axhline(0, color=GRID, linewidth=0.8)
    # travel direction (horizontal)
    ax1.add_patch(FancyArrowPatch((0.5, -1.7), (4, -1.7), arrowstyle="-|>",
                  mutation_scale=16, linewidth=2.2, color=INK))
    ax1.text(2.2, -2.1, "wave travels →", color=INK, fontsize=10, ha="center")
    # oscillation direction (vertical)
    ax1.add_patch(FancyArrowPatch((np.pi / 2, -0.1), (np.pi / 2, 1.0),
                  arrowstyle="<->", mutation_scale=14, linewidth=2.2, color=ACCENT2))
    ax1.text(np.pi / 2 + 0.2, 0.5, "particles move (perpendicular)", color=ACCENT2,
             fontsize=10, fontweight="bold")
    ax1.set_title("Transverse wave (e.g. light, a string)")
    ax1.set_xlim(0, 4 * np.pi)
    ax1.set_ylim(-2.5, 1.6)
    ax1.set_xticks([]); ax1.set_yticks([])

    # --- Longitudinal ---
    # draw vertical lines whose density varies sinusoidally (compressions/rarefactions)
    xs = np.linspace(0, 12, 60)
    density = 0.45 * np.sin(2 * np.pi * xs / 4.0)
    positions = xs + density
    for px in positions:
        ax2.plot([px, px], [0, 1], color=BLUE, linewidth=1.6)
    # mark a compression and a rarefaction
    ax2.add_patch(FancyArrowPatch((0.5, 1.6), (12, 1.6), arrowstyle="-|>",
                  mutation_scale=16, linewidth=2.2, color=INK))
    ax2.text(6, 1.85, "wave travels →", color=INK, fontsize=10, ha="center")
    # compression near where lines bunch (where density positive slope crowds)
    ax2.annotate("compression", xy=(3.0, -0.25), xytext=(2.4, -0.9),
                 fontsize=10, color=ACCENT2, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=ACCENT2))
    ax2.annotate("rarefaction", xy=(5.2, -0.25), xytext=(6.0, -0.9),
                 fontsize=10, color=GREEN, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=GREEN))
    ax2.add_patch(FancyArrowPatch((9.0, 1.15), (10.2, 1.15), arrowstyle="<->",
                  mutation_scale=14, linewidth=2.2, color=ACCENT2))
    ax2.text(9.6, 1.3, "particles move (parallel)", color=ACCENT2, fontsize=10,
             fontweight="bold", ha="center")
    ax2.set_title("Longitudinal wave (e.g. sound)")
    ax2.set_xlim(-0.5, 12.5)
    ax2.set_ylim(-1.3, 2.2)
    ax2.set_xticks([]); ax2.set_yticks([])

    fig.tight_layout()
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L03 — v = f·λ
# ---------------------------------------------------------------------------
def vflambda_worked_diagram(path):
    """A single wave annotated with v = fλ and worked numbers."""
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    x = np.linspace(0, 4 * np.pi, 600)
    ax.plot(x, np.sin(x), color=PURPLE, linewidth=2.6)
    ax.axhline(0, color=GRID, linewidth=0.8)
    # one wavelength bracket
    ax.add_patch(FancyArrowPatch((np.pi / 2, 1.25), (np.pi / 2 + 2 * np.pi, 1.25),
                 arrowstyle="<->", mutation_scale=14, linewidth=2.0, color=INK))
    ax.text(np.pi / 2 + np.pi, 1.45, "λ = 2 m", color=INK, fontsize=12,
            fontweight="bold", ha="center")
    ax.add_patch(FancyArrowPatch((0.4, -1.7), (4, -1.7), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.2, color=BLUE))
    ax.text(2.2, -2.1, "v = f·λ = (3 Hz)(2 m) = 6 m/s", color=BLUE,
            fontsize=12, fontweight="bold", ha="center")
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(-2.5, 1.9)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Wave speed from frequency and wavelength")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L04 — Standing waves and harmonics
# ---------------------------------------------------------------------------
def standing_wave_harmonics(path):
    """Fundamental + 2nd + 3rd harmonics on a fixed-end string, with nodes and
    antinodes labeled on the fundamental."""
    fig, axes = plt.subplots(3, 1, figsize=(7.2, 6.0))
    L = 1.0
    x = np.linspace(0, L, 400)
    titles = ["Fundamental (1st harmonic): 1 antinode",
              "2nd harmonic: 2 antinodes, 1 interior node",
              "3rd harmonic: 3 antinodes, 2 interior nodes"]
    for n, ax in zip([1, 2, 3], axes):
        env = np.sin(n * np.pi * x / L)
        ax.plot(x, env, color=PURPLE, linewidth=2.4)
        ax.plot(x, -env, color=PURPLE, linewidth=2.4)
        ax.fill_between(x, env, -env, color=BLUE, alpha=0.12)
        ax.axhline(0, color=GRID, linewidth=0.8)
        # nodes (where sin = 0)
        node_x = [k * L / n for k in range(n + 1)]
        ax.plot(node_x, [0] * len(node_x), marker="o", color=INK,
                markersize=7, linestyle="none", zorder=5)
        # antinodes
        anti_x = [(k + 0.5) * L / n for k in range(n)]
        ax.plot(anti_x, [0] * len(anti_x), marker="^", color=ACCENT2,
                markersize=9, linestyle="none", zorder=5)
        ax.set_title(titles[n - 1], fontsize=11)
        ax.set_xlim(-0.03, L + 0.03)
        ax.set_ylim(-1.3, 1.3)
        ax.set_xticks([]); ax.set_yticks([])
    axes[0].text(0.0, 1.05, "● node", color=INK, fontsize=9)
    axes[0].text(0.18, 1.05, "▲ antinode", color=ACCENT2, fontsize=9)
    fig.tight_layout()
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L05 — Interference
# ---------------------------------------------------------------------------
def interference_constructive(path):
    """Two in-phase waves add to a larger wave."""
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    x = np.linspace(0, 4 * np.pi, 600)
    w1 = np.sin(x)
    w2 = np.sin(x)
    ax.plot(x, w1, color=BLUE, linewidth=2.0, linestyle="--", label="wave 1")
    ax.plot(x, w2 + 0.0, color=ACCENT2, linewidth=2.0, linestyle=":", label="wave 2 (in phase)")
    ax.plot(x, w1 + w2, color=PURPLE, linewidth=2.8, label="sum (constructive)")
    ax.axhline(0, color=GRID, linewidth=0.8)
    ax.set_title("Constructive interference: in phase → amplitudes add")
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(-2.4, 2.4)
    ax.set_xticks([]); ax.set_yticks([])
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    return _save(fig, path)


def interference_destructive(path):
    """Two out-of-phase waves cancel."""
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    x = np.linspace(0, 4 * np.pi, 600)
    w1 = np.sin(x)
    w2 = -np.sin(x)
    ax.plot(x, w1, color=BLUE, linewidth=2.0, linestyle="--", label="wave 1")
    ax.plot(x, w2, color=ACCENT2, linewidth=2.0, linestyle=":", label="wave 2 (out of phase)")
    ax.plot(x, w1 + w2, color=PURPLE, linewidth=2.8, label="sum (destructive = 0)")
    ax.axhline(0, color=GRID, linewidth=0.8)
    ax.set_title("Destructive interference: out of phase → amplitudes cancel")
    ax.set_xlim(0, 4 * np.pi)
    ax.set_ylim(-2.4, 2.4)
    ax.set_xticks([]); ax.set_yticks([])
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L06 — Doppler effect
# ---------------------------------------------------------------------------
def doppler_wavefronts(path):
    """Concentric wavefronts from a source moving to the right: bunched
    (higher f) ahead, stretched (lower f) behind."""
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.set_aspect("equal")
    ax.axis("off")
    # source emits at times t = 0,1,2,3,4 from positions moving right
    emit_x = [0, 0.9, 1.8, 2.7, 3.6]
    radii = [4.0, 3.0, 2.0, 1.0, 0.2]
    for ex, r in zip(emit_x, radii):
        ax.add_patch(Circle((ex, 0), r, fill=False, edgecolor=PURPLE,
                     linewidth=1.8))
    # current source position
    ax.plot(emit_x[-1], 0, marker=">", color=ACCENT2, markersize=16, zorder=6)
    ax.add_patch(FancyArrowPatch((emit_x[-1], 0), (emit_x[-1] + 1.0, 0),
                 arrowstyle="-|>", mutation_scale=16, linewidth=2.2,
                 color=ACCENT2, zorder=6))
    ax.text(emit_x[-1] + 1.1, 0, " source motion", color=ACCENT2,
            fontsize=10, fontweight="bold", va="center")
    # observers
    ax.text(5.0, 1.6, "AHEAD: waves bunched →\nhigher frequency (higher pitch / blueshift)",
            color=BLUE, fontsize=10, fontweight="bold", ha="left")
    ax.text(-5.0, 1.6, "BEHIND: waves stretched →\nlower frequency (lower pitch / redshift)",
            color=GREEN, fontsize=10, fontweight="bold", ha="left")
    ax.set_xlim(-5.2, 8.2)
    ax.set_ylim(-4.4, 3.2)
    ax.set_title("Doppler effect: a moving source compresses waves ahead, stretches them behind")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L07 — EM spectrum
# ---------------------------------------------------------------------------
def em_spectrum_bands(path):
    """Horizontal band chart of the EM spectrum: radio → gamma, increasing
    frequency / decreasing wavelength."""
    fig, ax = plt.subplots(figsize=(8.4, 3.2))
    bands = [
        ("Radio", "#7b1fa2"),
        ("Microwave", "#3949ab"),
        ("Infrared", "#c62828"),
        ("Visible", "#f9a825"),
        ("Ultraviolet", "#6a1b9a"),
        ("X-ray", "#00838f"),
        ("Gamma", "#212121"),
    ]
    width = 1.0
    for i, (name, color) in enumerate(bands):
        ax.add_patch(Rectangle((i * width, 0), width, 1.0, facecolor=color,
                     edgecolor="white", alpha=0.85))
        ax.text(i * width + width / 2, 0.5, name, ha="center", va="center",
                color="white", fontsize=9, fontweight="bold", rotation=0)
    n = len(bands)
    # wavelength decreases →; frequency increases →
    ax.add_patch(FancyArrowPatch((0, 1.35), (n, 1.35), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.2, color=INK))
    ax.text(n / 2, 1.5, "increasing frequency  (f) →", ha="center",
            fontsize=11, fontweight="bold", color=INK)
    ax.add_patch(FancyArrowPatch((n, -0.35), (0, -0.35), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.2, color=INK))
    ax.text(n / 2, -0.62, "increasing wavelength  (λ) →", ha="center",
            fontsize=11, fontweight="bold", color=INK)
    ax.text(0.05, -0.95, "~10³ m", fontsize=8, color=INK)
    ax.text(n - 0.6, -0.95, "~10⁻¹² m", fontsize=8, color=INK)
    ax.set_xlim(-0.2, n + 0.2)
    ax.set_ylim(-1.1, 1.8)
    ax.axis("off")
    ax.set_title("The electromagnetic spectrum (all travel at c = 3.0 × 10⁸ m/s in vacuum)")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L08 — Refraction / Snell's law
# ---------------------------------------------------------------------------
def refraction_ray_diagram(path):
    """Incident ray bending toward the normal as it enters a denser medium,
    with the normal, incident, refracted, and a partial reflected ray."""
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    ax.set_aspect("equal")
    ax.axis("off")
    # interface (horizontal line at y=0), top = air, bottom = water
    ax.axhline(0, color=INK, linewidth=2.0)
    ax.add_patch(Rectangle((-4, -4), 8, 4, facecolor=BLUE, alpha=0.12))
    ax.text(-3.6, 2.6, "Air  (n₁ = 1.00)", fontsize=11, color=INK)
    ax.text(-3.6, -3.4, "Water  (n₂ = 1.33)", fontsize=11, color=INK)
    # normal (dashed vertical through origin)
    ax.plot([0, 0], [-4, 4], color=INK, linestyle="--", linewidth=1.3)
    ax.text(0.1, 3.6, "normal", fontsize=9, color=INK)
    # incident ray (from upper left to origin), angle from normal ~ 45 deg
    ax.add_patch(FancyArrowPatch((-3, 3), (0, 0), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=PURPLE))
    ax.text(-2.6, 2.1, "incident ray", color=PURPLE, fontsize=10, fontweight="bold")
    # refracted ray (bends toward normal, steeper) into water
    ax.add_patch(FancyArrowPatch((0, 0), (1.6, -3.0), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.4, color=ACCENT2))
    ax.text(1.0, -2.4, "refracted ray\n(bends toward normal)", color=ACCENT2,
            fontsize=10, fontweight="bold")
    # partial reflected ray (faint)
    ax.add_patch(FancyArrowPatch((0, 0), (3, 3), arrowstyle="-|>",
                 mutation_scale=12, linewidth=1.6, color=GRID))
    ax.text(2.4, 2.7, "reflected", color="#999999", fontsize=9)
    # angle arcs
    ax.add_patch(Arc((0, 0), 2.0, 2.0, angle=0, theta1=90, theta2=135,
                 color=PURPLE, linewidth=1.6))
    ax.text(-0.85, 1.0, "θ₁", color=PURPLE, fontsize=12, fontweight="bold")
    ax.add_patch(Arc((0, 0), 2.4, 2.4, angle=0, theta1=242, theta2=270,
                 color=ACCENT2, linewidth=1.6))
    ax.text(0.35, -1.25, "θ₂", color=ACCENT2, fontsize=12, fontweight="bold")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title("Refraction: n₁ sin θ₁ = n₂ sin θ₂")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L09 — Lenses and mirrors
# ---------------------------------------------------------------------------
def converging_lens_ray_diagram(path):
    """Object outside f of a converging lens → real, inverted image, with the
    three principal rays."""
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.axhline(0, color=INK, linewidth=1.0)  # principal axis
    # lens at x=0
    ax.plot([0, 0], [-2.5, 2.5], color=BLUE, linewidth=3.0)
    ax.annotate("", xy=(0, 2.7), xytext=(0, 2.5),
                arrowprops=dict(arrowstyle="-|>", color=BLUE))
    ax.annotate("", xy=(0, -2.7), xytext=(0, -2.5),
                arrowprops=dict(arrowstyle="-|>", color=BLUE))
    ax.text(0.1, 2.8, "converging lens", color=BLUE, fontsize=9)
    f = 2.0
    do = 4.0
    # focal points
    for fx in (-f, f):
        ax.plot(fx, 0, marker="o", color=INK, markersize=5)
    ax.text(f, -0.35, "F", fontsize=10)
    ax.text(-f, -0.35, "F", fontsize=10)
    # object (upright arrow) at x = -do, height 1.5
    ho = 1.5
    ax.add_patch(FancyArrowPatch((-do, 0), (-do, ho), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.6, color=PURPLE))
    ax.text(-do, ho + 0.15, "object", color=PURPLE, fontsize=10,
            fontweight="bold", ha="center")
    # image distance from 1/f = 1/do + 1/di  -> di = 1/(1/f - 1/do)
    di = 1 / (1 / f - 1 / do)   # = 4.0
    hi = -ho * di / do          # inverted
    # ray 1: parallel to axis then through far focus
    ax.plot([-do, 0], [ho, ho], color=ACCENT2, linewidth=1.6)
    ax.plot([0, di], [ho, hi], color=ACCENT2, linewidth=1.6)
    # ray 2: through center, straight
    ax.plot([-do, di], [ho, hi], color=GREEN, linewidth=1.6)
    # ray 3: through near focus then parallel
    ax.plot([-do, 0], [ho, -hi if False else 0], color="#c0392b", linewidth=0.0)
    # image arrow
    ax.add_patch(FancyArrowPatch((di, 0), (di, hi), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.6, color=INK))
    ax.text(di, hi - 0.25, "image\n(real, inverted)", color=INK, fontsize=10,
            fontweight="bold", ha="center", va="top")
    ax.set_xlim(-do - 1, di + 1.5)
    ax.set_ylim(-3.2, 3.4)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Converging lens:  1/f = 1/dₒ + 1/dᵢ")
    return _save(fig, path)


def concave_mirror_ray_diagram(path):
    """Object outside C of a concave mirror → real, inverted image."""
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.axhline(0, color=INK, linewidth=1.0)
    # mirror arc at right (concave, opening left)
    R = 4.0
    arc = Arc((R, 0), 2 * R, 2 * R, angle=0, theta1=150, theta2=210,
              color=BLUE, linewidth=3.0)
    ax.add_patch(arc)
    ax.text(R - 0.2, 2.4, "concave mirror", color=BLUE, fontsize=9, ha="right")
    f = R / 2
    ax.plot(f, 0, marker="o", color=INK, markersize=5)
    ax.text(f, -0.35, "F", fontsize=10)
    ax.plot(R, 0, marker="o", color=INK, markersize=5)
    ax.text(R, -0.35, "C", fontsize=10)
    do = 6.0   # outside C (which is at 4)
    ho = 1.5
    ax.add_patch(FancyArrowPatch((-do + R, 0), (-do + R, ho), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.6, color=PURPLE))
    # use object position on axis: place object at x = R - do? keep simple coords
    # Reframe: vertex at x=0 for clarity instead.
    ax.clear()
    ax.axhline(0, color=INK, linewidth=1.0)
    # vertex at x=0, mirror curving to the left side (opening right toward object)
    arc = Arc((-R, 0), 2 * R, 2 * R, angle=0, theta1=-30, theta2=30,
              color=BLUE, linewidth=3.0)
    ax.add_patch(arc)
    ax.text(0.1, 2.4, "concave\nmirror", color=BLUE, fontsize=9)
    f = R / 2
    ax.plot(-f, 0, marker="o", color=INK, markersize=5)
    ax.text(-f, -0.35, "F", fontsize=10)
    ax.plot(-R, 0, marker="o", color=INK, markersize=5)
    ax.text(-R, -0.35, "C", fontsize=10)
    do = 6.0
    ho = 1.5
    # object to the left, beyond C
    ax.add_patch(FancyArrowPatch((-do, 0), (-do, ho), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.6, color=PURPLE))
    ax.text(-do, ho + 0.15, "object", color=PURPLE, fontsize=10,
            fontweight="bold", ha="center")
    di = 1 / (1 / f - 1 / do)
    hi = -ho * di / do
    # ray parallel → reflects through F
    ax.plot([-do, 0], [ho, ho], color=ACCENT2, linewidth=1.6)
    ax.plot([0, -do], [ho, hi if (-do) != 0 else 0], color=ACCENT2, linewidth=0.0)
    ax.plot([0, -f], [ho, 0], color=ACCENT2, linewidth=1.6)
    ax.plot([-f, -di], [0, hi], color=ACCENT2, linewidth=1.6)
    # ray through C reflects back on itself
    ax.plot([-do, -di], [ho, hi], color=GREEN, linewidth=1.6)
    ax.add_patch(FancyArrowPatch((-di, 0), (-di, hi), arrowstyle="-|>",
                 mutation_scale=16, linewidth=2.6, color=INK))
    ax.text(-di, hi - 0.25, "image\n(real, inverted)", color=INK, fontsize=10,
            fontweight="bold", ha="center", va="top")
    ax.set_xlim(-do - 1, 1.5)
    ax.set_ylim(-3.2, 3.4)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("Concave mirror:  1/f = 1/dₒ + 1/dᵢ")
    return _save(fig, path)


# ---------------------------------------------------------------------------
# L10 — Analog vs digital
# ---------------------------------------------------------------------------
def analog_vs_digital(path):
    """A smooth analog sine overlaid with its stair-step digital (sampled +
    quantized) version."""
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    t = np.linspace(0, 2, 800)
    analog = np.sin(2 * np.pi * t) * 1.0
    ax.plot(t, analog, color=PURPLE, linewidth=2.6, label="analog (continuous)")
    # sample at intervals, quantize to discrete levels
    n_samples = 16
    ts = np.linspace(0, 2, n_samples, endpoint=False)
    raw = np.sin(2 * np.pi * ts)
    levels = 8
    quant = np.round((raw + 1) / 2 * (levels - 1)) / (levels - 1) * 2 - 1
    # stair-step
    step_t = np.repeat(ts, 2)[1:]
    step_t = np.append(step_t, 2.0)
    step_v = np.repeat(quant, 2)
    ax.plot(step_t, step_v, color=BLUE, linewidth=2.2, drawstyle="steps-post",
            label="digital (sampled + quantized)")
    ax.plot(ts, quant, marker="o", color=ACCENT2, linestyle="none",
            markersize=5, label="samples")
    ax.axhline(0, color=GRID, linewidth=0.8)
    ax.set_title("Analog signal vs its digital approximation")
    ax.set_xlabel("time")
    ax.set_yticks([])
    ax.set_xlim(0, 2)
    ax.set_ylim(-1.6, 1.6)
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    return _save(fig, path)


def sampling_diagram(path):
    """A sampling diagram: continuous curve with vertical sample lines and a
    bit-depth ladder on the side."""
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    t = np.linspace(0, 2, 800)
    analog = np.sin(2 * np.pi * t)
    ax.plot(t, analog, color=PURPLE, linewidth=2.4)
    n_samples = 12
    ts = np.linspace(0, 2, n_samples, endpoint=False) + (1 / n_samples)
    vs = np.sin(2 * np.pi * ts)
    levels = 8
    quant = np.round((vs + 1) / 2 * (levels - 1)) / (levels - 1) * 2 - 1
    for x, y in zip(ts, quant):
        ax.plot([x, x], [0, y], color=BLUE, linewidth=1.4, linestyle="--")
        ax.plot(x, y, marker="o", color=ACCENT2, markersize=6)
    # quantization grid lines
    for lvl in np.linspace(-1, 1, levels):
        ax.axhline(lvl, color=GRID, linewidth=0.6)
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.text(0.02, 1.15, "8 levels = 3 bits per sample", fontsize=9, color=INK)
    ax.set_title("Sampling: measure the signal at regular intervals, store each as bits")
    ax.set_xlabel("time")
    ax.set_yticks([])
    ax.set_xlim(0, 2)
    ax.set_ylim(-1.4, 1.4)
    return _save(fig, path)


# ---------------------------------------------------------------------------
# Secondary figures (one extra per lesson that started with a single figure)
# ---------------------------------------------------------------------------
def particle_motion_compare(path):
    """Two small panels: a single particle's path in a transverse wave (up/down)
    vs. a longitudinal wave (back/forth), beside the travel direction."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.2))
    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        # wave travel direction (to the right)
        ax.add_patch(FancyArrowPatch((-1.6, -1.6), (1.6, -1.6), arrowstyle="-|>",
                     mutation_scale=14, linewidth=1.8, color=INK))
        ax.text(0, -1.95, "wave travels →", ha="center", fontsize=9, color=INK)
        ax.add_patch(Circle((0, 0), 0.22, facecolor=PURPLE, edgecolor=INK, zorder=4))
    # transverse: particle moves up/down (perpendicular)
    ax1.add_patch(FancyArrowPatch((0, -0.9), (0, 0.9), arrowstyle="<->",
                  mutation_scale=16, linewidth=2.6, color=ACCENT2))
    ax1.text(0.25, 0.7, "up/down", color=ACCENT2, fontsize=10, fontweight="bold")
    ax1.set_title("Transverse: particle perpendicular to travel", fontsize=10)
    # longitudinal: particle moves left/right (parallel)
    ax2.add_patch(FancyArrowPatch((-0.9, 0), (0.9, 0), arrowstyle="<->",
                  mutation_scale=16, linewidth=2.6, color=GREEN))
    ax2.text(-0.7, 0.35, "back/forth", color=GREEN, fontsize=10, fontweight="bold")
    ax2.set_title("Longitudinal: particle parallel to travel", fontsize=10)
    fig.tight_layout()
    return _save(fig, path)


def resonance_curve(path):
    """A resonance response curve: amplitude peaks sharply at the natural
    frequency."""
    f = np.linspace(0.2, 3.0, 400)
    f0 = 1.5  # natural frequency
    gamma = 0.15
    amp = 1.0 / np.sqrt((f0**2 - f**2) ** 2 + (gamma * f) ** 2)
    amp = amp / amp.max()
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.plot(f, amp, color=PURPLE, linewidth=2.6)
    ax.axvline(f0, color=ACCENT2, linewidth=1.6, linestyle="--")
    ax.text(f0 + 0.05, 0.5, "natural\nfrequency", color=ACCENT2, fontsize=10,
            fontweight="bold")
    ax.set_xlabel("driving frequency (Hz)")
    ax.set_ylabel("response amplitude")
    ax.set_title("Resonance: huge response when driven at the natural frequency")
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.set_ylim(0, 1.15)
    return _save(fig, path)


def doppler_observed_frequency(path):
    """A bar chart of observed frequency: source frequency vs. approaching vs.
    receding."""
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    cats = ["Receding\n(behind)", "Source\n(at rest)", "Approaching\n(ahead)"]
    vals = [600, 700, 820]
    colors = [GREEN, INK, BLUE]
    bars = ax.bar(cats, vals, 0.6, color=colors)
    ax.axhline(700, color=INK, linewidth=1.0, linestyle="--")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 8, f"{v} Hz", ha="center",
                fontsize=10, fontweight="bold")
    ax.set_ylabel("observed frequency (Hz)")
    ax.set_title("Doppler effect: observed frequency vs. relative motion")
    ax.set_ylim(0, 900)
    ax.grid(True, axis="y", color=GRID, linewidth=0.8)
    return _save(fig, path)


def em_speed_constant(path):
    """A bar chart showing all EM bands share c, while their wavelengths differ
    enormously (log scale)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 3.4))
    bands = ["Radio", "Micro", "IR", "Vis", "UV", "X-ray", "Gamma"]
    # all speeds equal c
    c = 3.0e8
    ax1.bar(bands, [c] * len(bands), 0.6, color=PURPLE)
    ax1.set_ylabel("speed in vacuum (m/s)")
    ax1.set_title("Same speed: c for all", fontsize=11)
    ax1.set_ylim(0, 3.6e8)
    ax1.tick_params(axis="x", labelrotation=45, labelsize=8)
    ax1.grid(True, axis="y", color=GRID, linewidth=0.8)
    # wavelengths differ (log)
    wl = [1e3, 1e-2, 1e-5, 5e-7, 1e-8, 1e-10, 1e-12]
    ax2.bar(bands, wl, 0.6, color=BLUE)
    ax2.set_yscale("log")
    ax2.set_ylabel("wavelength (m, log scale)")
    ax2.set_title("Different wavelengths", fontsize=11)
    ax2.tick_params(axis="x", labelrotation=45, labelsize=8)
    ax2.grid(True, axis="y", color=GRID, linewidth=0.8)
    fig.tight_layout()
    return _save(fig, path)


def index_of_refraction_chart(path):
    """A bar chart of the index of refraction for common media, with a note on
    how light slows as n rises."""
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    media = ["Vacuum", "Air", "Water", "Glass", "Diamond"]
    n = [1.00, 1.00, 1.33, 1.50, 2.42]
    bars = ax.bar(media, n, 0.6, color=SERIES[:len(media)])
    for b, v in zip(bars, n):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.04, f"{v:.2f}", ha="center",
                fontsize=10, fontweight="bold")
    ax.set_ylabel("index of refraction  n = c / v")
    ax.set_title("Higher n → light travels slower → bends more")
    ax.set_ylim(0, 2.9)
    ax.grid(True, axis="y", color=GRID, linewidth=0.8)
    return _save(fig, path)


# ---------------------------------------------------------------------------
def main():
    written = []

    d = fig_dir("01_Wave_Anatomy_and_Characteristics")
    written.append(labeled_sine_wave(d / "wave_anatomy.png"))
    written.append(frequency_period_illustration(d / "frequency_period.png"))

    d = fig_dir("02_Transverse_and_Longitudinal_Waves")
    written.append(transverse_vs_longitudinal(d / "transverse_vs_longitudinal.png"))
    written.append(particle_motion_compare(d / "particle_motion.png"))

    d = fig_dir("03_Wave_Speed_Frequency_and_Wavelength")
    f = [1, 2, 3, 4, 6, 12]
    lam = [12.0 / fi for fi in f]   # constant v = 12 m/s
    written.append(line_graph(
        d / "wavelength_vs_frequency.png",
        [("λ vs f (v = 12 m/s)", f, lam)],
        xlabel="frequency f (Hz)", ylabel="wavelength λ (m)",
        title="At constant speed, λ and f are inversely related", markers=True))
    written.append(vflambda_worked_diagram(d / "vflambda_worked.png"))

    d = fig_dir("04_Standing_Waves_and_Resonance")
    written.append(standing_wave_harmonics(d / "standing_wave_harmonics.png"))
    written.append(resonance_curve(d / "resonance_curve.png"))

    d = fig_dir("05_Interference_Constructive_and_Destructive")
    written.append(interference_constructive(d / "interference_constructive.png"))
    written.append(interference_destructive(d / "interference_destructive.png"))

    d = fig_dir("06_The_Doppler_Effect")
    written.append(doppler_wavefronts(d / "doppler_wavefronts.png"))
    written.append(doppler_observed_frequency(d / "doppler_observed_frequency.png"))

    d = fig_dir("07_The_Electromagnetic_Spectrum")
    written.append(em_spectrum_bands(d / "em_spectrum.png"))
    written.append(em_speed_constant(d / "em_speed_constant.png"))

    d = fig_dir("08_Refraction_and_Snells_Law")
    written.append(refraction_ray_diagram(d / "refraction_ray.png"))
    written.append(index_of_refraction_chart(d / "index_of_refraction.png"))

    d = fig_dir("09_Optics_Lenses_and_Mirrors")
    written.append(converging_lens_ray_diagram(d / "converging_lens.png"))
    written.append(concave_mirror_ray_diagram(d / "concave_mirror.png"))

    d = fig_dir("10_Digital_Technologies_and_Information")
    written.append(analog_vs_digital(d / "analog_vs_digital.png"))
    written.append(sampling_diagram(d / "sampling.png"))

    print(f"Wrote {len(written)} figures:")
    for w in written:
        print(" ", w)


if __name__ == "__main__":
    main()
