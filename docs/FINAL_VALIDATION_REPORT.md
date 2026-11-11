# Final validation and release report

Date: November 10, 2026 (America/Los_Angeles). Baseline `d2ce4c2` (PR #17).
Repository: [Yug-More/MarketPulse](https://github.com/Yug-More/MarketPulse).
Branch: `codex/final-research-metrics-freeze`.

## Outcome and scope

The finalization adds a measured application-metrics freeze, adversarial integrity
tests, CI enforcement, contribution-qualified application wording, and a prioritized
audit. It preserves historical data, predictions, figures and manuscript outputs.
No new performance result or independent data is introduced. The central conclusion
remains that corrected point-forecast gains over simple baselines are not established
in the declared original or expanded families.

## Executed checks

The isolated environment used Python 3.13.2 on macOS 14.5 ARM64, NumPy 2.5.4,
pandas 3.1.1, scikit-learn 1.9.1 and PyTorch 2.15.0. Exact installed versions
are in `results/finalization/requirements.txt`; these are current verification
versions, not reconstructed historical training environments.

- **Tests:** 114 passed, zero skipped, in the final local run (`pytest.log`).
  This includes nine new freeze tests (parameter expansion included). Coverage
  percentage was not measured.
- **Lint and format:** Ruff check and format check pass (`lint.log`, `format.log`).
- **New verifier typing:** scoped mypy passes (`new_code_typecheck.log`).
- **Package-wide typing:** 40 errors in nine existing files (`typecheck.log`).
  This exploratory check is not a pass and is not a required existing CI job.
  No source-generation guard or type rule was weakened to hide it.
- **Package build:** sdist and wheel build successfully (`build.log`). Research
  artifacts remain repository assets; building the package alone does not bundle
  the stored study or enable complete experiment replay.
- **Neural integration:** the installed `marketpulse-walkforward` entry point
  completed two smoke folds using all five procedures and generated figures
  (`neural_smoke.log`). Smoke metrics are wiring evidence, excluded from claims.
- **Six cross-phase audits:** all passed, with historical tree unchanged
  (`verified_cross_phase_audit/manifest.json`). This verifies original fold
  records, robustness/calibration, four-block historical rehearsal, expanded
  seed results, adaptive intervals and failure diagnostics.
- **Independent arithmetic:** all 355,320 saved targets, 282 fold boundaries,
  30 pooled metric rows, and separate 18/30/60 comparison families agree with
  raw-price reconstruction and saved statistics (`independent_recalculation.json`).
  The audit also reconstructs 1,494/347,500 designated nesting failures.
- **Scientific verification:** passes its computational checks of 430,920
  point-forecast records and saved interval evidence (`scientific_verification.json`).
  The extra records are selected-seed sensitivity; they are not added to the
  canonical application count or treated as independent outcomes.
- **Claim registry:** 40 claims and six prior audit bindings pass; independent
  confirmation remains false (`check_1.log`).
- **Publication assets:** 12 tables and four figures pass (`check_2.log`).
- **Manuscript:** 37 quantitative bindings and 12 recorded verified references
  pass (`check_3.log`); the saved PDF build/hash check passes at 18 pages
  (`check_4.log`). No manuscript text, citation, figure, PDF or historical output
  was edited or rebuilt in this finalization. This is artifact verification,
  not new external peer review or a new reference-source retrieval.
- **Frozen metrics:** direct reconstruction passes (`check_7.log`); canonical
  counts are 355,320 records, 71,064 index/horizon origins, 23,726 index/date
  pairs, 21,475 calendar dates and 282 index/horizon folds. All remain dependent.

All paths in this section are relative to `results/finalization/`. Individual
verification return codes and measured command durations are in `checks.json`.
The saved study's numerical confidence intervals remain in the primary comparison
CSVs; they are marginal 95% block intervals, not simultaneous guarantees.

## Guard failure encountered and corrected

The first cross-phase attempt failed the historical source-identity check after
an additional OHLC validation condition was briefly placed in the frozen historical
validator. The edit and its test were removed; the historical validator is unchanged.
The failed log is retained in `cross_phase_audit/` and the successful complete
rerun is `verified_cross_phase_audit/`. No historical manifest, source hash, result,
or test was relaxed. The new freeze verifier is separate from the historical
pipeline and independently reconstructs target positions from raw price dates.

## Skeptical research review

The question, targets, chronology, baseline definitions, shared samples, paired
inference, negative findings and claim bindings are defensible within the saved
retrospective scope. Equal target samples do not remove different index histories,
correlation or researcher exposure. HAC/bootstrap conclusions remain conditional
on dependence choices; failure to reject is not equivalence. Seed sensitivity is
selected-fold only. No trading system or transaction-cost study was added.

Complete acquisition history, exact source versions, data rights, early S&P
construction, researcher blinding and 210 legacy execution contexts remain
unresolved. Historical weights are absent. Full-history training was not rerun.
Only the previous six-fold replay establishes exact reproduced fits for that
subset. Current smoke runtime is not a model efficiency benchmark. No inference
latency, memory, model-size, economic return or coverage percentage is invented.
These are claim restrictions and future evidence requirements, not claims fixed
by passing software checks.

## Release tracking

The feature branch uses `Yug-More <yugmore20@gmail.com>` for author and committer.
No history rewrite, force push, empty commit, or tool co-author attribution is used.
The finalization [pull request #18](https://github.com/Yug-More/MarketPulse/pull/18)
records hosted CI and merge state. The implementation commit is `174ee32` and the
research handoff/evidence commit is `0a8b911`; both author and committer identities
were verified. The PR is the release record for subsequent documentation commits,
the merge commit and post-merge CI, avoiding a self-referential commit hash here.
Post-merge state must be verified from remote main; a local test run alone is not
proof of merge or successful hosted CI.

## Application handoff

[FINAL_PROJECT_METRICS.md](FINAL_PROJECT_METRICS.md) is the authoritative human-readable
claim boundary, backed by `final_metrics.json`. [GRADUATE_APPLICATION_SUMMARY.md](GRADUATE_APPLICATION_SUMMARY.md)
contains exact whitespace-counted 75/100/150/200/250-word project/SOP/research variants,
three contribution-qualified résumé bullets, and interview answers. Source and
historical contribution limitations remain explicit. Existing methods documents
are reused; the finalization audit maps the requested documentation topics.
