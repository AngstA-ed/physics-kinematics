"""Walk the web edition and validate every HTML page.

Run before deploying to GitHub Pages so the live site never reveals an
answer key. Currently checks every *.html file under
Publisher_Ready_Curriculum/01_Physics_East_Meadow_Web/ for emphasis tags
inside multiple-choice option lists.

Exit code 0 on clean, 1 on any violation. Prints a per-file summary.

Usage:
    python tools/validate_web.py
"""
from __future__ import annotations
import sys
from pathlib import Path

# Add project root to sys.path so `from tools.validators import ...` works
# whether this script is run via `python tools/validate_web.py` or via
# `python -m tools.validate_web`.
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators import validate_web_assessment_html, ValidationError  # noqa: E402

WEB_ROOT = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Web"
SCHEMA = ROOT / "tools" / "lesson_schema.yaml"


def main() -> int:
    if not WEB_ROOT.exists():
        print(f"Web root not found at {WEB_ROOT}", file=sys.stderr)
        return 1
    html_files = sorted(WEB_ROOT.rglob("*.html"))
    errors: list[str] = []
    for html in html_files:
        try:
            validate_web_assessment_html(html, SCHEMA)
        except ValidationError as e:
            errors.append(str(e))
    if errors:
        print("Web assessment validation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  • {e}", file=sys.stderr)
        return 1
    print(f"OK — checked {len(html_files)} HTML files; no answer-revealing emphasis in any MC option.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
