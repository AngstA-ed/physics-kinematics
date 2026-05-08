"""Generate Pandoc reference DOCX with co-branded styles.

Run once whenever brand tokens change:
    source .venv/bin/activate && python tools/make_reference_docx.py
"""
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Inches

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Publisher_Ready_Curriculum" / "01_Physics_East_Meadow_Refactor" / "_assets" / "brand" / "reference.docx"

EM_PURPLE = RGBColor(0x66, 0x2E, 0x80)
VS_BLUE = RGBColor(0x2E, 0xA3, 0xF2)
INK = RGBColor(0x1A, 0x1A, 0x1A)


def main() -> None:
    doc = Document()

    # Body / Normal
    normal = doc.styles["Normal"]
    normal.font.name = "Inter"
    normal.font.size = Pt(11)
    normal.font.color.rgb = INK

    # Headings
    for level, size in [(1, 22), (2, 16), (3, 13)]:
        style = doc.styles[f"Heading {level}"]
        style.font.name = "Inter"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = EM_PURPLE

    # Hyperlink color via Body Text approximation: most teachers won't see it,
    # but Pandoc respects the Hyperlink character style if present.
    if "Hyperlink" in [s.name for s in doc.styles]:
        doc.styles["Hyperlink"].font.color.rgb = VS_BLUE

    # Page margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

    # Insert a styled paragraph so Pandoc has a sample of every style applied
    doc.add_heading("Co-branded reference", level=1)
    doc.add_heading("Subheading", level=2)
    doc.add_paragraph("Body text sample.").style = normal

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
