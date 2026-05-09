# Kinematics — Visual Prompts

Source prompts for any AI-generated images used in this unit. Re-runnable so visuals are reproducible. Note: the pilot Kinematics lessons rely entirely on **hand-authored inline SVG** — no AI-generated raster images were used. This file documents prompts for *future* AI-generated images that the unit could optionally include (e.g., printable cover art, additional storyboards, lab-station signage).

## Style / brand inputs (apply to every prompt)

- Two-color palette: **East Meadow purple `#662e80`** and **Valley Stream blue `#2ea3f2`**. Optional accent: **`#f37366`** (orange, for warnings or peak labels).
- Flat illustration style — no gradients, no photorealism, no glow effects. Inspired by educational textbook flat-art conventions.
- 16:9 aspect ratio for unit covers; 1:1 for individual lesson icons.
- No text in the AI-generated image itself unless explicitly requested. Text is layered on later in DOCX or HTML.

## Unit cover image

> "Stylized vector arrows arranged in a kinematics motif — a head-to-tail vector addition triangle, a parabolic projectile arc, and a simple x-t coordinate axis with a single straight line. Flat illustration, two-color palette: deep purple #662e80 and bright blue #2ea3f2. Subtle accent in #f37366 for the projectile peak. 16:9, no text. Background: pure white."

## Optional per-lesson icon prompts

These are *not* required by the pilot but can be generated as 64×64 lesson icons if a future redesign uses them.

### 01 Vectors

> "A single bold purple arrow and a single bold blue arrow, drawn head-to-tail, forming an L-shape. A dashed black resultant arrow goes from tail of first to head of second. Flat. White background. 1:1."

### 02 Distance and Displacement

> "A zigzag walking-path drawn as connected purple line segments on a faint grid, with a straight blue dashed arrow connecting the start and end points (the displacement). Flat. White background. 1:1."

### 03 Average Speed and Velocity

> "Two simple cars at the same starting line, one purple, one blue, with the purple car drawing a straight horizontal arrow forward and the blue car drawing a U-turn arrow forward-then-backward. Flat. White background. 1:1."

### 04 Acceleration

> "A purple dot with three trailing afterimages, each spaced wider than the last, on a horizontal line — visualizing accelerating motion. To the right, a small velocity-time axis with a straight blue line of positive slope. Flat. White background. 1:1."

### 05 Motion Graphs

> "Two side-by-side coordinate axes labeled subtly. Left axes show a curving purple line (parabolic position vs time). Right axes show a straight blue line (linear velocity vs time). A faint connecting arrow points from one to the other. Flat. White background. 1:1."

### 06 Freefall

> "A small purple ball at the top of the frame with three downward-trailing afterimages spaced increasingly far apart (under gravity). Beside it, a faint Earth gravity arrow pointing down. Flat. White background. 1:1."

### 07 Vertical Projectiles

> "A vertical parabolic trajectory drawn in purple — ball goes straight up, peaks, and comes back down. The peak is highlighted in orange (#f37366) with a subtle 'v=0' indicator (no text — just a dot at the peak). Flat. White background. 1:1."

### 08 Horizontal Projectile Motion

> "A small table with a marble rolling off the edge. Two trajectories: a vertical purple dashed line (dropped marble) and a parabolic blue trajectory (rolled marble). Both end at the same horizontal floor line at the same time. Flat. White background. 1:1."

### 09 Projectiles at an Angle

> "Three projectile arcs from the same launch point at different angles (low, optimal 45°, high). The 45° arc is in orange #f37366; the others are gray. All three arcs end on the same horizontal ground. Flat. White background. 1:1."

## Image-generation guidance

- Use Imagen-3 or DALL-E 3 (recent generations handle "flat illustration" better than older models).
- Iterate on **palette adherence** first — accept color drift only when the composition is otherwise correct.
- For lesson icons, generate at 1024×1024 and downscale; this preserves arrow-tip quality at smaller display sizes.
- Save outputs to `Visuals/<lesson-slug>_icon.png` and update this file with the date and prompt revision.

## Provenance log

| Date | Image file | Prompt | Notes |
|---|---|---|---|
| 2026-05-08 | (none generated) | — | Pilot relies on inline SVG; this file is a seed for future visual passes. |
