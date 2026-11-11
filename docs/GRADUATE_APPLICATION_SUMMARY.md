# Graduate application summary

Frozen November 10, 2026. Use with [the authoritative metrics](FINAL_PROJECT_METRICS.md).
All summaries describe the project, not a certification of individual authorship.
First-person claims require the applicant to confirm that they accurately describe
work personally performed. The historical project was collaborative: Yug More's
NASDAQ work and Srihan Cheemangunta's S&P work remain attributed in Git.
No publication, peer review, independent validation, or profitable trading outcome
is claimed. Counts below are dependent forecasts, not independent experiments.

## 75-word project summary

MarketPulse compares financial return forecasts from linear regression, random forests, and sequence LSTMs with zero-return and historical-mean baselines. Its retrospective evaluation contains 355,320 forecasts across 282 purged walk-forward folds on NASDAQ-100 and S&P 500 price histories. Dependence-aware comparisons and multiple-testing correction do not establish consistent machine-learning improvements over simple baselines. The repository preserves negative findings, reproducible analyses, and explicit limitations concerning data provenance, historical execution metadata, and independent validation. Findings remain conditional on these histories.

## 100-word SOP description

MarketPulse investigates whether model complexity improves financial return forecasting under chronological evaluation. The retrospective study compares linear regression, random forests, and sequence LSTMs against zero-return and historical-mean baselines across two US price-index histories and three horizons. Its 355,320 stored forecasts represent 71,064 index/horizon origins across 282 purged walk-forward folds, not independent trials. Training-only preprocessing, validation-based model selection, paired losses, dependence-aware uncertainty, and separate multiple-testing families support an auditable evaluation. No corrected machine-learning gain over simple baselines is established in the declared point-forecast families. Missing source provenance and historical execution metadata constrain reproducibility and generalization. These findings remain conditional and retrospective.

## 150-word technical summary

MarketPulse evaluates whether increasingly complex models improve financial return forecasts relative to simple statistical baselines. The retrospective study compares standardized linear regression, random forests, and sequence LSTMs with zero-return and frozen historical-mean forecasts on stored NASDAQ-100 and S&P 500 price histories. Targets are forward log-close returns over one, five, and twenty sessions. Expanding-window evaluation uses purged training, chronological validation, and shared test origins. Scalers see training data only; validation selects forest depth and LSTM size and stopping epoch. The canonical outputs contain 355,320 forecasts across 282 index/horizon folds, representing 71,064 dependent origins. Paired-loss HAC calculations, moving-block confidence intervals, and separate Holm families distinguish point-estimate wins from supported improvements. No corrected machine-learning gain over either simple baseline is established in the declared point-forecast families. Saved evidence, configurations, figures, and manuscript claims remain traceable. Source acquisition gaps, missing legacy execution metadata, and unavailable independent validation limit stronger conclusions. No profitability is established.

## 200-word research description

MarketPulse studies whether financial forecasting gains justify model complexity under leakage-resistant retrospective evaluation. It compares linear regression, random forests, and sequence LSTMs with zero-return and historical-mean baselines on NASDAQ-100 and S&P 500 price-index histories. Forward log-return targets span one, five, and twenty sessions. Ten causal features and trailing sequence windows use information available through the forecast close. Expanding training, purged boundaries, chronological validation, and shared test origins constrain leakage; model selection and preprocessing exclude test outcomes.

The canonical study stores 355,320 forecasts across 282 index/horizon folds, representing 71,064 dependent forecast origins. Paired-loss inference combines HAC uncertainty, moving-block confidence intervals, and separate Holm corrections. Random forests achieve the lowest pooled RMSE in three of six cells, but no corrected machine-learning improvement over a simple baseline is established in the declared point-forecast families. LSTM has the highest native pooled RMSE in all six cells. Selected-fold seed, regime, and matched-calendar analyses expose sensitivity rather than universal rankings.

The repository binds research claims to saved outputs, configurations, figures, and manuscript artifacts. Missing acquisition records, unresolved source rights, absent historical weights, and incomplete execution metadata constrain complete replication. The study supports honest negative findings and careful empirical methodology, without establishing unseen-market performance or trading profitability.

## 250-word research summary

MarketPulse asks whether machine-learning models provide reliable improvements over simple financial return forecasts. The retrospective study uses two price-index histories, NASDAQ-100 and S&P 500, with forward log-close-return horizons of one, five, and twenty sessions. Standardized linear regression, random forests, and sequence LSTMs share evaluation origins with zero-return and frozen training-target-mean baselines.

Its expanding-window protocol separates training, validation, and testing chronologically. Horizon-dependent purges exclude labels whose outcomes reach later blocks. Causal features and sequence windows end at each forecast close; scalers fit training observations only. Validation chooses forest depth, LSTM hidden size, and stopping epoch, while test outcomes remain outside those choices. The canonical record contains 355,320 forecasts across 282 index/horizon folds, corresponding to 71,064 dependent forecast origins rather than independent experiments.

Random forests achieve the lowest native pooled RMSE in three of six cells, with simple baselines winning the remainder. No corrected machine-learning improvement over a simple baseline survives the declared original or expanded point-forecast families. LSTM ranks last in all six native pooled cells. Paired losses, HAC uncertainty, moving-block confidence intervals, and separate Holm families distinguish descriptive rankings from supported comparisons. Selected-fold seeds, matched dates, and volatility regimes reveal sensitivity.

A delayed-feedback interval study retains long-horizon undercoverage and nominal-level nesting failures alongside score improvements. Reproducible scripts connect stored predictions, configurations, tables, figures, and manuscript claims. Missing source acquisition records, incomplete historical execution metadata, absent weights, and unavailable independent validation remain explicit limitations. The contribution is an auditable framework and negative evidence, without claims of profitability or universal model inferiority.

## Three résumé bullet candidates

Use these only within the contribution boundary above; replace action verbs if they
overstate personal responsibility.

- Developed and audited a financial forecasting pipeline comparing five procedures
  across 282 purged walk-forward folds and 355,320 stored forecasts on two price indexes.
- Evaluated paired forecast losses with dependence-aware uncertainty and multiple-testing
  correction; found no supported ML improvement over simple baselines in the declared
  original and expanded point-forecast families.
- Built reproducible evidence checks linking forecast records, configurations, publication
  assets, and application metrics, with explicit provenance and generalization limitations.

## Verified metrics and methodological decisions

There are three learned model families, two simple baselines, three horizons,
71,064 index/horizon origins, 23,726 index/date pairs and 21,475 calendar dates.
The canonical 355,320 records exclude extra selected-seed predictions and interval
variants. Ten causal features and trailing 20-session sequences use information
through close t. Training has at least 2,520 origins, followed by 252 validation and
252 test origins, with horizon-dependent purges. The canonical seed is 171;
five-seed sensitivity covers selected folds only. The original 18-test, expanded
30-test, and adaptive 60-test families are separate. CIs are marginal 95% block
intervals and do not inherit simultaneous coverage from Holm p-value adjustment.

## Individual and team contribution summary

Repository history supports Yug More's NASDAQ notebooks, dataset inclusion, and
README work, and Srihan Cheemangunta's S&P dataset/notebooks and README work.
Later commits under Yug-More record package development and research validation.
These records do not independently prove unaided personal implementation of every
later module. Describe concrete decisions you understand and can defend; retain
team attribution. The research contribution is empirical comparison and an auditable
methodology, not a new forecasting theorem or demonstrated commercial strategy.

## Technical challenges and negative findings

The principal challenges were target/sequence alignment, training-only preprocessing,
maturing labels at temporal boundaries, paired sample denominators, dependence-aware
inference, preserving old outputs, and keeping claims synchronized with evidence.
Full historical fit replay remains limited by absent weights and 210 execution
contexts. Complete acquisition dates/source versions/rights remain unverified.
No finalization work can reconstruct those facts honestly from current hashes.

RF's point-estimate wins do not yield corrected baseline gains in the declared
point-forecast families; LSTM has the highest native pooled RMSE in all six cells.
Selected-fold seed ranks vary materially. Adaptive score gains coexist with
long-horizon undercoverage and 1,494 nesting violations among 347,500 eligible pairs.
Nonsignificance does not prove equivalence; conditional retrospective findings do
not establish future performance, independent replication, or economic value.

## Faculty interview questions and evidence-based answers

**What is your central result?** More complex models did not consistently beat
simple baselines under this saved protocol. RF wins some descriptive cells, but
corrected ML-over-baseline improvements are not established in the declared
point-forecast families. This is conditional negative evidence, not a universal claim.

**Why are 355,320 forecasts not 355,320 trials?** Each index/horizon origin is
repeated across five procedures; horizons overlap, indexes co-move, and folds share
expanding training histories. There are 71,064 index/horizon origins, not independent
replications. Paired losses and dependence-aware inference address part of that structure.

**How did you prevent leakage?** Features end at the origin, sequences align to
that origin's label, scalers fit training rows, and labels reaching later partitions
are purged. Validation chooses settings before test evaluation. This does not prove
historical researcher blinding or vendor point-in-time data provenance.

**Why might simpler models compete?** Weak predictable signal, sampling variation,
nonstationarity, and estimation variance are plausible explanations. The experiment
does not isolate a causal explanation or prove these mechanisms.

**What did you tune?** Forest depth in {4,8}; LSTM hidden size in {16,32} and
validation stopping epoch, using the saved budgets. Final test outcomes do not choose
those settings. The retrospective research process itself is not independently blinded.

**How strong are the statistical claims?** They use paired losses, HAC standard
errors, moving-block marginal intervals, and declared Holm families. Dependence and
block/bandwidth assumptions matter. A smaller adjusted p-value is not proof of practical
utility; failing to reject is not equivalence.

**What would you do next?** Resolve source lineage and usage rights, register a
frozen protocol before receiving genuinely unexposed observations, preserve weights
and execution environments, and evaluate after targets mature. Do not retroactively
label reused historical data independent validation.

**Did the uncertainty extension solve coverage?** No. Limited interval-score gains
coexist with long-horizon undercoverage and nonnested levels. The saved failure modes
are part of the result, not hidden exceptions.

**Was it profitable or published?** Neither is established. Forecast errors do not
specify executable trades, transaction costs, slippage, or economic returns. The
repository includes a manuscript, not a claim of publication or external peer review.

**What can someone reproduce?** Stored targets, metrics, inference families,
claim bindings and publication assets can be checked. Six terminal folds were
previously replayed exactly. Full independent source reacquisition and every original
fit cannot be reproduced with the available provenance. Current validation outcomes
are in [the final validation report](FINAL_VALIDATION_REPORT.md).
