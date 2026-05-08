"""Copy interactive Student_Exploration.html files to the gh-pages branch.

Run only if SharePoint Permissive mode is unavailable and HTML must be hosted on
GitHub Pages. The script writes a self-contained `gh_pages_out/` directory that
the user manually copies onto a `gh-pages` branch.
"""
from __future__ import annotations
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFACTOR = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(ROOT / "gh_pages_out"))
    args = p.parse_args()
    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    # Copy _assets
    shutil.copytree(REFACTOR / "_assets", out / "_assets")

    # Copy each lesson's Student_Exploration.html into a mirroring path
    for unit in sorted(REFACTOR.iterdir()):
        if not unit.is_dir() or unit.name.startswith("_"):
            continue
        for lesson in sorted(unit.iterdir()):
            if not lesson.is_dir():
                continue
            html = lesson / "Student_Exploration.html"
            if not html.is_file():
                continue
            target = out / unit.name / lesson.name / "Student_Exploration.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(html, target)

    print(f"Published interactives to {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
