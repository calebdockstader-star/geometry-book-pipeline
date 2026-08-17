# Resume state — written 2026-08-17 08:40 MDT (pre-offline snapshot)

If the session died or agents were killed by a network outage, this file is
the recovery map. Any session can resume from here.

## Where the book stands

- `build/book.pdf` — 448 pp, compiles clean, visually swept end to end.
  FINAL for: frontmatter, ch01–ch06(text), ch08–ch14, ch16, appendix.
- Remaining work (was in-flight when this was written):
  1. **ch07 prose** — 147 `\VIItodo{...}` scaffold spans to transcribe
     (PDF pp.130–146). Agent was running (workflow `wf_c7c61517-6db`,
     task wsec5qygp, script `…/workflows/scripts/brumfiel-repairs3.js`).
     After transcription, its pipeline runs a fresh text review.
  2. **ch15 prose** — 53 `\XVtodo{...}` spans (PDF pp.265–279). Same
     workflow/pipeline as ch07.
  3. **ch06 figures** — finisher driving label collisions 48→0 REAL,
     scan-verifying ~45 blocks (workflow `wf_e2602e3b-d62`, task ws6nc42eb,
     script `…/workflows/scripts/ch06-figure-finish-wf_e2602e3b-d62.js`).
- Check `grep -oE "(pending|todo)\{" chapters/*.tex` — the integration gate
  is that this returns NOTHING (plus `\VIItodo`/`\XVtodo` macro defs deleted).

## How to resume a dead lane

- Check journals first (one JSON line per agent result):
  `~/.claude/projects/-Users-calebdockstader-Documents-Claude-Fun-geometry-book-pipeline/419dbb5f-0a2e-42b3-95f6-ea1625405529/subagents/workflows/<runid>/journal.jsonl`
- Relaunch with cache: `Workflow({scriptPath: <script>, resumeFromRunId: <runid>})`
  — completed calls replay from cache; only dead ones re-run.
- API 529 Overloaded plagued 07:15–08:00 this morning; spawns died instantly
  (0 tokens). Just retry after ~10 min.

## Integration checklist (after all three lanes are green)

1. Gate: placeholder grep empty; `python3 tools/verify_figures.py` all green;
   `python3 tools/check_labels.py chapters/figuresNN.tex NN` 0 COLLIDE for 06.
2. `python3 tools/assemble_book.py` (handles counter resets, raggedbottom,
   local-macro hoisting, TOC splice) then
   `tectonic -Z search-path=style -Z search-path=chapters --outdir build book.tex` ×2.
3. Visually inspect the re-flowed ch06/ch07/ch15 regions (rest already swept).
4. Consolidate all `chapters/*-UNCERTAIN.md` → `OPEN-QUESTIONS.md` by chapter;
   collapse copyright entries to one settled note citing
   `sources/copyright/renewal-search.md`.
5. Update STATUS.md; mark session tasks #5/#6 completed; SendUserFile
   `build/book.pdf` + `OPEN-QUESTIONS.md` to Caleb.

## Fixed this session (do not redo)

- Copyright basis verified & documented: `sources/copyright/renewal-search.md`.
- Assembler: per-chapter counter resets + `\raggedbottom` (tools/assemble_book.py).
- Hilbert plate dedup (frontmatter keeps it; ch01's removed).
- ch09 Figs 9-53/54/55 hoisted into figures09.tex + constraints (186/186, 0 collide).
- check_labels.py: tectonic driver, Bezier flattening, white-fill masks,
  notation-rule filter, prime/subscript merging, missing-file guard.

## Environment

- LaTeX = tectonic (brew), cache warm — compiles work OFFLINE.
- Agents/API need network. Session crons: recovery checks armed for
  10:45 and 12:45 MDT on 2026-08-17 (session-local — gone if the terminal
  closes; then start a fresh session and follow this file).
