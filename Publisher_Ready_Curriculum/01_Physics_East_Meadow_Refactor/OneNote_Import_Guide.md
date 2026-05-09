# OneNote Class Notebook — Import Guide (one page)

Use this for every lesson once you have built it. The whole curriculum can be distributed to students via OneNote Class Notebook with no JavaScript and no external link dependencies.

## You'll need

- Microsoft 365 OneNote (web, desktop, or iPad)
- A Class Notebook for the course (one-time setup via the OneNote Class Notebook app — your district IT can enable this)
- The two `.onenote.html` files for the lesson:
  - `Student_Exploration.onenote.html`
  - `Teacher_Guide.onenote.html`

## Steps (per lesson)

### 1. Create the page

In your Class Notebook → **Content Library** → **Unit: Kinematics** → **New Page**. Title it `Lesson NN — Topic` (e.g., `Lesson 01 — Vectors`).

### 2. Open the static student page

In a browser, open `Student_Exploration.onenote.html` (double-click it on disk, or open from your SharePoint document library).

### 3. Copy

Cmd+A (or Ctrl+A) to **Select All** → Cmd+C (or Ctrl+C) to **Copy**.

### 4. Paste into OneNote

Click into the page body of the Content Library page → Cmd+V (or Ctrl+V). The page renders the co-branded header, all sections, and the storyboard SVGs. **Tables, lists, headings, and SVG diagrams all paste with full fidelity.**

### 5. Embed videos

The OneNote-paste version includes "Insert → Online Video" callouts wherever the original interactive HTML had a video iframe. For each callout:

1. Click the URL in the callout
2. Copy the URL
3. In OneNote, place the cursor where the video should appear → **Insert** → **Online Video** → paste
4. Delete the callout text once the video is embedded

### 6. Distribute

Use **Class Notebook** → **Distribute Page** to push it to all student sections at once. Each student gets their own copy in their OneNote — they can write, draw, and annotate on top of the lesson content.

### 7. Teacher section

Repeat steps 2–4 for `Teacher_Guide.onenote.html`, pasting into your *teacher-only* section (not the Content Library and not student sections). This keeps answer keys and lesson plans private.

## Tips and known limitations

### Cross-client paste fidelity

- **OneNote desktop (Mac and Windows)** has the highest paste fidelity. Use this when you can.
- **OneNote for iPad** preserves layout well but occasionally drops the SVG storyboard frames; the surrounding text remains intact, and the link to the SharePoint-hosted interactive `.html` (if you've set up that fallback) lets students still see the simulator.
- **OneNote on the web** sometimes downgrades complex tables. If the page looks off, open the same notebook in OneNote desktop or iPad and re-paste.

### Distribution is one-shot

OneNote Class Notebook **copies** pages once at distribution time. Subsequent edits to the Content Library page do *not* propagate to already-distributed student copies. If you need to push an update mid-unit, distribute the page again to a fresh student section folder (e.g., "Lesson 01 — Vectors v2"), or ask students to manually copy the new content into their existing page.

### Student-writing surfaces

Lessons include `<textarea>` boxes for Notice & Wonder and Initial Model. In OneNote, those textareas render as gray placeholder boxes. **OneNote ink and typing on top of them work normally** — students can write in the box just by clicking on it. Their writing is saved automatically and is theirs, not the teacher's.

### Interactive widget fallback

Inside the OneNote-pasted page, the live JavaScript interactive (sliders, animated trajectory, etc.) is replaced with a **3-frame static SVG storyboard**. The storyboard captures the key states of the interactive in pictures — students who paste the page see the diagrams without needing JavaScript to run.

If you want students to use the *live* interactive (sliders, real-time graphs), have them open the `Student_Exploration.html` from your SharePoint library or GitHub Pages link in a browser tab — alongside their OneNote page.

## Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Pasted page is mostly blank | Browser blocked file-system access during the copy | Open the `.onenote.html` from a SharePoint URL instead of a `file://` path |
| SVG diagrams missing on iPad | Known iPad OneNote limitation | Re-paste from OneNote desktop, or include a SharePoint link to the interactive HTML |
| Layout is broken (overlapping text) | Pasted from a non-OneNote browser into the web client | Try OneNote desktop; re-paste |
| "Insert Online Video" doesn't recognize the URL | The link is for a video site OneNote doesn't natively support | Embed the page URL as a hyperlink instead, or use the **Web Clipper** OneNote extension |

## Summary

The OneNote workflow is: build the lesson → open the `.onenote.html` → Select All → Copy → Paste into OneNote → embed videos via Insert Online Video → distribute. Per-lesson elapsed time: about 5 minutes after the first lesson (faster once you have the muscle memory).
