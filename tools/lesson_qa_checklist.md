# Manual QA checklist (per lesson, pilot only)

Run after `python tools/build_lessons.py 01_Kinematics/NN_Topic` succeeds.

1. Open `Student_Exploration.html` via `file://` URL in Chrome — verify it renders
   and interacts correctly with no server.
2. Print preview — verify the print stylesheet hides interactive controls and
   shows the static fallback.
3. Disable JavaScript (DevTools → Settings → Disable JavaScript) — verify the
   storyboard fallback and curated MD links remain usable.
4. Open `Student_Exploration.onenote.html` in a browser — verify no JS warnings,
   no broken images, no external requests in the Network tab.
5. Select All → Copy → Paste into a OneNote page (test on web, desktop, and
   iPad clients) — verify layout, images, and links survive the paste.
6. Open `Teacher_Guide.docx` in Word — verify cover lockup, fonts, and tinted
   Curated Resources box render correctly.
7. Re-run `python tools/build_lessons.py 01_Kinematics/NN_Topic` and confirm
   zero hard-fails.
