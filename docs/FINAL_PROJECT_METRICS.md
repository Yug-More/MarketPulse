# Frozen MarketPulse project metrics

Freeze date: November 10, 2026 (America/Los_Angeles). Research baseline:
`d2ce4c25506a291b0c69254a8127419795a64123` (merged PR #17).
This is the authoritative application-claim boundary for the existing retrospective
study. The accompanying [machine-readable freeze](final_metrics.json) binds
measured denominators, all 30 pooled metric rows, and 17 evidence/configuration
hashes. It is not a new experiment, certification, or independent confirmation.
Release commits and CI are recorded in the finalization PR linked from the
[validation report](FINAL_VALIDATION_REPORT.md).

## Project and contribution boundaries

**Official name:** MarketPulse. **Description:** A reproducible retrospective
comparison of linear regression, random forest, and sequence LSTM financial
price-return forecasts against simple baselines. **Area:** empirical machine
learning, time-series evaluation, and statistical forecast comparison.

Git history attributes the NASDAQ notebooks and associated course-project work to
Yug More and the S&P dataset/notebooks to Srihan Cheemangunta (`srihanrc`); both
contributed README changes. Preserve this shared origin. Subsequent commits under
Yug-More record the research package, evidence audits, and finalization work.
Git attribution establishes recorded responsibility, not independent verification
of how much code was personally written without assistance. Application wording
must reflect the applicant's actual work and distinguish original team work from
later repository development. See [the original audit](REPOSITORY_AUDIT.md) and
[research contribution boundaries](RESEARCH_CONTRIBUTIONS.md).

## Data and counting units

- NASDAQ-100 (`^NDX`): 6,289 stored sessions, January 3, 2000–December 31, 2024.
- S&P 500 (`^GSPC`): 23,323 stored sessions, December 30, 1927–November 4, 2020.
- Total input rows: 29,612 index/session records, not independent observations.
- Forward log-close-return horizons: 1, 5, and 20 file sessions.
- Canonical prediction records: **355,320**, including both baselines.
- Distinct index/horizon forecast origins: **71,064**.
- Distinct index/date pairs across horizons: **23,726**.
- Distinct calendar dates across both indexes and all horizons: **21,475**.
- Index/horizon folds: **282**, comprising 13 per NASDAQ horizon and 81 per S&P horizon.
- Five procedures: three learned model families and two simple baselines.
- The forecast records, horizons, folds, dates, and indexes are dependent.
  **No independent-trial count is established.** Do not call these 355,320 experiments.

The NASDAQ notebook records a yfinance download; the S&P notebook describes a
Kaggle source without an exact dataset/version URL. Acquisition dates, exact
source revisions, full-file provenance, licensing, and past researcher exposure
are unresolved. Inputs are price-index closes, not dividend-reinvested total
returns or a point-in-time constituent panel. Corporate-action treatment and
historical membership are not reconstructed. The premodern S&P history, including
its first row before the provider's stated first-value date, remains unresolved.
No survivorship-bias-free or unseen-data claim is authorized.

## Experimental protocol

The forecast origin is after close t; the label is `log(C[t+h]/C[t])`.
Ten trailing features and 20-session sequence windows use information through t.
Expanding training uses at least 2,520 origins, followed by 252 validation origins
and 252 test origins per fold, stepping 252 eligible origins. Training labels
mature strictly before validation starts; validation labels mature strictly before
test starts. No test origin repeats within an index/horizon. Training and scalers
are fixed during the block; future mature outcomes may enter later folds.
This is retrospective walk-forward evaluation, not a permanently untouched test set.

Zero return and the frozen embargoed training-target mean are the baselines.
Linear regression uses training-only standardization. Random forest selects depth
4 or 8 using validation RMSE (200 trees, minimum leaf size 5). One-layer LSTM
selects hidden size 16 or 32 using validation RMSE, lookback 20, Adam 0.001,
batch size 256, maximum 25 epochs, patience 5, restored best validation weights.
The canonical seed is 171. Additional seeds 171/271/371/471/571 cover selected
folds, not every historical fold. No additional model family was added in this freeze.

## Pooled results and evaluation dates

RMSE below uses concatenated prediction errors in log-return units. These are
rounded presentation values; the JSON and source CSV retain full precision.
Each n counts origins per procedure, not the total across five procedures.

- **NASDAQ-100, h=1**: 13 folds; 3,276 origins, 2011-12-21–2024-12-30. RMSE: zero_return 0.01293108; historical_mean 0.01293151; linear_regression 0.01293854; random_forest 0.01278679; lstm 0.01336627.
- **NASDAQ-100, h=5**: 13 folds; 3,276 origins, 2011-12-15–2024-12-23. RMSE: zero_return 0.02654638; historical_mean 0.02654909; linear_regression 0.02656753; random_forest 0.02629975; lstm 0.02709838.
- **NASDAQ-100, h=20**: 13 folds; 3,276 origins, 2011-11-23–2024-12-02. RMSE: zero_return 0.05181378; historical_mean 0.05190190; linear_regression 0.05218904; random_forest 0.05320649; lstm 0.05444301.
- **S&P 500, h=1**: 81 folds; 20,412 origins, 1939-08-25–2020-11-03. RMSE: zero_return 0.00995053; historical_mean 0.00994824; linear_regression 0.00996843; random_forest 0.00988535; lstm 0.01032622.
- **S&P 500, h=5**: 81 folds; 20,412 origins, 1939-08-21–2020-10-28. RMSE: zero_return 0.02206745; historical_mean 0.02204244; linear_regression 0.02212451; random_forest 0.02210424; lstm 0.02264049.
- **S&P 500, h=20**: 81 folds; 20,412 origins, 1939-07-31–2020-10-07. RMSE: zero_return 0.04388101; historical_mean 0.04367350; linear_regression 0.04402313; random_forest 0.04441878; lstm 0.04555491.

MAE, forecast bias, direction accuracy, and relative MSE skill against both
baselines are retained for all 30 rows in `final_metrics.json` and
`results/walkforward/full/pooled_metrics.csv`. MSE equals squared RMSE.
Skill versus the fold-specific historical-mean forecast is an out-of-sample
baseline-relative MSE measure; it is not an in-sample regression R-squared.
Zero forecasts do not earn correct-direction credit for nonzero outcomes.
No economic return, latency, memory-use, or profitability metric is inferred.

## Statistics, uncertainty, and robustness

RF has the lowest native pooled RMSE in three of six cells; simple baselines win
the other three. LSTM has the highest pooled RMSE in all six. No RF improvement
over either simple baseline survives the original 18-test Holm family. No ML gain
over a simple baseline survives the separate expanded 30-test family. Original
S&P h20 RF losses are higher than both simple baselines after correction.
Nonsignificance does not establish equivalence or universal model inferiority.

Paired forecast losses use Bartlett HAC and session-preserving moving-block
bootstrap calculations. Confidence intervals are marginal 95% intervals, not
simultaneous Holm-inverted intervals. Full effects, standard errors, nominal and
adjusted p-values, and CI endpoints are in `paper/tables/original_primary.csv`,
`expanded_primary.csv`, and `adaptive_primary.csv`; the independent recalculation
checks all declared family sizes and numerical values. Do not pool the families.

The adaptive interval extension has 20 adjusted score improvements among 60
primary comparisons, limited to S&P h1/h5 versus trailing calibration. Long-horizon
undercoverage and 1,494 crossings among 347,500 eligible designated-method nominal
level pairs remain. No distribution-free guarantee follows. These intervals reuse
point forecasts and do not increase the independent outcome sample.

Selected-fold five-seed sensitivity, calendar matching, volatility regimes,
alternative losses and block-length sensitivities are documented in
[the robustness report](PHASE10_ROBUSTNESS.md). NASDAQ h20 LSTM seed ranks span
1–5 in the selected sample; this does not overturn its full-history last place.
Regime thresholds use training-only trailing volatility. Short stress samples and
unequal index histories constrain interpretation. The 60 Phase 10 extra stochastic
runs contain 30,240 forecasts and 13.76 summed training minutes in saved records;
this is not full-study runtime or a standardized hardware efficiency comparison.
Training weights are absent; 210 of 282 folds lack original execution metadata.
The earlier six-terminal-fold replay reproduced 7,560 saved values, not all fits.

## Engineering and reproducibility

See [the current validation report](FINAL_VALIDATION_REPORT.md) for test outcomes,
checks, measured environment, and package-wide typing limits. Coverage percentage
was not measured. Historical input and result trees are preserved.
The package separates data loading/validation, causal features/targets, temporal
partitions, fitted models, saved experiments, paired inference, and publication
artifacts. The freeze rejects duplicates, unpaired outcomes, incomplete model
samples, repeated fold origins, nonfinite records, target reconstruction errors,
and evidence hash drift. Freeze creation refuses to replace an existing file.

```bash
python -m marketpulse.frozen_metrics verify
python scripts/audit_all_research.py --output /tmp/marketpulse-fresh-audit
python scripts/audit_evidence_authenticity.py --output /tmp/marketpulse-recalculation.json
python scripts/final_synthesis.py verify
python scripts/publication_assets.py verify
python scripts/manuscript.py verify
python scripts/verify_manuscript_pdf.py
pytest -ra
ruff check .
ruff format --check .
```

Use a new audit output directory. Saved arithmetic and presentation assets can be
verified; complete source reacquisition and exact historical fit replay cannot.
Raw forecasts are `results/walkforward/full/predictions.csv.gz`; exact fold CSVs
are `fold_predictions.tar.gz`; fold boundaries and run identity are `fold_plan.json`
and `manifest.json`. Configurations are `configs/{datasets,forecasting,benchmark}.toml`.
The 40-claim registry is `results/phase12/claims.json`; new verification logs are
under `results/finalization/`. Environment versions are recorded there, separate
from historical training environments. The paper has 12 tables, four figures,
12 previously verified references, and an 18-page compiled PDF. Verification here
checks recorded citations/bindings and hashes; it is not a new external literature review.

## Application language and change policy

Use the [graduate application summary](GRADUATE_APPLICATION_SUMMARY.md) for the
requested 75/100/150/200/250-word variants, three résumé bullets, and interview
answers. Approved one-sentence description:

> Developed and audited a retrospective financial forecasting study comparing five
> procedures across 282 purged walk-forward folds and 355,320 saved forecasts,
> finding no corrected ML gain over simple baselines in the declared point-forecast families.

Use the contribution qualifications above when describing individual responsibility.
The freeze governs application claims, not future scientific updates. A genuine
correction requires preserving the old freeze in Git, explaining the changed evidence,
rerunning verification, and reviewing all application wording. Never silently add
sensitivity forecasts to the canonical count or remove inconvenient negative findings.
