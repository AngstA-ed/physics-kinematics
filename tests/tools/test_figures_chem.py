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
