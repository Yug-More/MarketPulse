"""Adversarial denominator checks use labelled synthetic fixtures only."""

import pandas as pd
import pytest

from marketpulse.frozen_metrics import summarize_predictions


def records():
    return pd.DataFrame(
        [
            {
                "dataset": "fixture",
                "horizon": horizon,
                "fold": 0,
                "origin_position": 10,
                "date": "2020-01-02",
                "target_date": "2020-01-10",
                "model": model,
                "y_true": 0.1,
                "y_pred": 0.0,
            }
            for horizon in (1, 5)
            for model in ("zero_return", "linear_regression")
        ]
    )


def test_distinguishes_records_horizons_and_dates():
    counts = summarize_predictions(records())
    assert counts["forecast_records"] == 4
    assert counts["dataset_horizon_origins"] == 2
    assert counts["dataset_dates"] == 1
    assert counts["calendar_dates"] == 1
    assert counts["dataset_horizon_folds"] == 2
    assert counts["independent_trials"] is None


def test_rejects_duplicate_forecasts():
    frame = records()
    with pytest.raises(ValueError, match="duplicate forecast"):
        summarize_predictions(pd.concat([frame, frame.iloc[:1]]))


def test_rejects_missing_model_origin():
    with pytest.raises(ValueError, match="complete origin"):
        summarize_predictions(records().iloc[:-1])


def test_rejects_unpaired_outcome():
    frame = records()
    frame.loc[0, "y_true"] = 0.2
    with pytest.raises(ValueError, match="paired labels"):
        summarize_predictions(frame)


def test_rejects_repeated_origin_across_folds():
    frame = records()
    other = frame.copy()
    other["fold"] = 1
    with pytest.raises(ValueError, match="repeated across folds"):
        summarize_predictions(pd.concat([frame, other]))


@pytest.mark.parametrize("value", [float("inf"), float("nan")])
def test_rejects_nonfinite_predictions(value):
    frame = records()
    frame.loc[0, "y_pred"] = value
    with pytest.raises(ValueError, match="nonfinite|missing"):
        summarize_predictions(frame)


def test_rejects_nonfuture_endpoint():
    frame = records()
    frame["target_date"] = frame["date"]
    with pytest.raises(ValueError, match="endpoint"):
        summarize_predictions(frame)


def test_freeze_refuses_overwrite_and_verify_detects_drift(tmp_path, monkeypatch):
    from marketpulse import frozen_metrics

    output = tmp_path / "freeze.json"
    payload = {"counts": {"forecast_records": 4}, "sha256": {"input": "original"}}
    monkeypatch.setattr(frozen_metrics, "snapshot", lambda root: payload)
    monkeypatch.setattr("sys.argv", ["freeze", "freeze", "--output", str(output)])
    frozen_metrics.main()
    with pytest.raises(FileExistsError):
        frozen_metrics.main()
    monkeypatch.setattr("sys.argv", ["freeze", "verify", "--output", str(output)])
    frozen_metrics.main()
    payload["sha256"]["input"] = "changed"
    with pytest.raises(ValueError, match="evidence changed"):
        frozen_metrics.main()
