# Finalization technical and research audit

Date: November 10, 2026, America/Los_Angeles. Baseline: `d2ce4c2`, PR #17.
The verified repository is `https://github.com/Yug-More/MarketPulse`; fetched main
matched local main. There were no open PRs at inspection. Historical audit reports
remain dated evidence; this report does not rewrite them.

## Implemented, executed, and reproducible

The repository already implements data schemas/validation, ten causal features,
forward log-return targets, purged expanding windows, two baselines, standardized
OLS, validation-selected RF and sequence LSTM, delayed-feedback calibration,
paired HAC/bootstrap inference, Holm families, seed/regime/matched-population
analyses, result persistence, claim registries, figures, manuscript, and CI.
Original notebooks, two raw files, historical outputs, and contributor history
are preserved. The full canonical evidence comprises 282 folds and 355,320 stored
forecasts. Selected-seed and calibration extensions reuse the historical data.
They are not new independent market samples.

Saved target reconstruction, pooled arithmetic, common samples, fold chronology,
and the three declared statistical families are independently recomputable from
committed records. Six current-code terminal folds were replayed by the previous
audit with exact saved-value agreement. This finalization reruns arithmetic audits
and neural smoke checks, not a fresh refit of every historical model. Original
weights and 210 historical execution contexts cannot be recovered from the repository.

## Prioritized findings and disposition

1. **High, unresolved: acquisition/rights and prior exposure.** Exact S&P source
   URL/version, acquisition timestamps, complete license records and historical
   source authentication remain unavailable. The early S&P row/date discrepancy
   remains. Fix requires genuine source evidence, not filling metadata by inference.
   Current public claims explicitly restrict the study to stored retrospective data.
2. **High for stronger claims, unresolved: independent generalization.** No genuinely
   unseen prospective dataset or outcomes exist. The Phase 9 rehearsal is infrastructure
   evidence only. Do not relabel it independent validation or tune to final results.
3. **High for exact historical replay, unresolved: 210 legacy executions.** Preserve
   provenance gaps and absent weights. Current environment records cannot establish
   historical execution facts. No fresh full-history refit is claimed.
4. **Medium, resolved: application denominator freeze.** Added a read-only verifier
   that reconstructs endpoints/labels and measures records, origins, index/dates,
   calendar dates and folds directly. Evidence/configuration hashes and all native
   metrics are frozen; CI detects drift. Exclusive creation prevents accidental
   replacement. Tests challenge pairing, repeated origins, nonfinite values,
   incomplete models, overwrite, and drift.
5. **Medium, resolved: stale seed-method wording.** The walk-forward methodology
   still said multiseed sensitivity had not run. It now distinguishes the canonical
   single seed from later selected-fold five-seed analyses.
6. **Medium, measured limitation: package typing.** Exploratory package-wide mypy
   reports 40 errors in nine existing files. These are not hidden by disabling checks
   or changing the historical pipeline. The new freeze module passes scoped mypy.
   Existing runtime tests and CI remain mandatory; package-wide typing is not a
   historical CI requirement. No claim of a fully typed package is made.
7. **Medium, retained: statistical interpretation.** Overlapping horizons, shared
   histories and regimes invalidate independent-trial interpretations. HAC/block
   assumptions, marginal CIs, and separate Holm families remain explicit. No corrected
   ML-over-baseline gain is established; equivalence is not demonstrated either.
8. **Medium, retained: adaptive failure modes.** Long-horizon undercoverage and
   nonnested intervals remain part of the results; no post-hoc repair or coverage
   guarantee is introduced for presentation.
9. **Low, resolved: release handoff.** Added application wording, frozen metrics,
   verification evidence, README navigation and an explicit contribution/rights boundary.
   Existing methods documents are reused rather than duplicated under new names.

## Leakage and fairness review

Features end at close t. Labels use t+h and are purged at train/validation and
validation/test boundaries with strict maturity before the next block. Training
scalers and validation selection exclude test outcomes. LSTM sequences end at the
origin; best-validation weights are restored in memory. Models share test origins;
pooled metrics concatenate errors rather than averaging RMSEs. New outcomes may
enter later folds after maturity. This protocol is chronology-resistant to the
identified code-level leakage paths but cannot establish historical researcher
blinding or unchanged vendor data. No additional tuning, model family, trading
subsystem, data download, or favorable period selection was introduced.

## Architecture and documentation map

`data/` and `configs/datasets.toml` retain source files and declared schema;
`src/marketpulse/data` parses without sorting/filling rows. `features.py`,
`targets.py`, and `sequences.py` construct aligned causal samples. `evaluation/`
implements partitions, preprocessing, metrics, paired reliability and regimes.
`models/` holds baselines/classical/LSTM; `experiments/` persists fold-level outputs,
identities, budgets and analyses. `publication.py` and `publication_assets.py`
bind claims/tables/figures to evidence. `frozen_metrics.py` adds the release boundary.

Dataset documentation remains `data/README.md`; design is in
`docs/WALKFORWARD_METHODOLOGY.md` and `FORECASTING_PIPELINE.md`; statistics are in
`STATISTICAL_RELIABILITY.md`; reproduction is in `REPRODUCIBILITY_GUIDE.md`.
These satisfy the requested architecture/dataset/design/statistics/reproduction
coverage without redundant alias documents. The existing manuscript and four
publication figures are retained and verified; no new chart or result is fabricated.

## Acceptance scope

This release freezes a defensible retrospective application artifact. It does not
close source-rights questions, reconstruct legacy provenance, pass package-wide
mypy, establish prospective performance, or justify a publication/peer-review claim.
Those limits prohibit stronger claims; they do not contradict the existing
qualified findings. Verification outcomes and release state belong in
[FINAL_VALIDATION_REPORT.md](FINAL_VALIDATION_REPORT.md).
