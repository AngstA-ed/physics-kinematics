# Chemistry — East Meadow Refactor

Phenomenon-based 5E rebuild of the Valley Stream / East Meadow Chemistry
curriculum, parallel to `01_Physics_East_Meadow_Refactor/`. Markdown sources are
built to brand-styled DOCX.

## Sources of truth
- Sequence & content: `../02_Chemistry/Valley_Stream_Chemistry_Scope_Sequence.docx`
- Instructional framework: `../02_Chemistry/Copy of 1. East Meadow Valley Stream Chem 5_6_26.pptx`
  (NYSSLS Lesson Observation Checklist, ABCs = Activity Before Content, ≤3 vocab
  in the 2nd half, OPTIC/CER literacy, Regents 60/40).

## Build
    source .venv/bin/activate
    python tools/_gen_chem_unit01_figures.py            # render figures
    python tools/build_lessons.py --root Publisher_Ready_Curriculum/02_Chemistry_East_Meadow_Refactor 01_Safety_and_Measurement

Output: `Teacher_Guide.docx`, `Student_Worksheet.docx`, `Student_Notes.docx`,
`Answer_Key.docx` per lesson + `Unit_Plan.docx`. Build must report 0 failures.

## Status
- [x] Unit 1 — Safety & Measurement (pilot)
- [ ] Units 2–11 (future cycles)
