"""Reconstruct application denominators and detect drift in frozen evidence.

Reads the compressed canonical records directly; never extracts archives or
changes historical outputs. Counts describe dependent forecasts, not trials.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from marketpulse.data.catalog import load_catalog
from marketpulse.data.loader import load_market_csv


def summarize_predictions(frame: pd.DataFrame) -> dict:
    """Require complete paired samples and report distinct counting units."""
    key = ["dataset", "horizon", "fold", "origin_position"]
    required = {*key, "date", "target_date", "model", "y_true", "y_pred"}
    if not required.issubset(frame.columns) or frame.empty:
        raise ValueError("predictions must contain nonempty canonical records")
    if frame[list(required)].isna().any().any():
        raise ValueError("prediction records contain missing values")
    if frame.duplicated([*key, "model"]).any():
        raise ValueError("duplicate forecast key")
    if not np.isfinite(frame[["y_true", "y_pred"]].to_numpy(dtype=float)).all():
        raise ValueError("nonfinite forecast or outcome")
    models = sorted(frame.model.unique().tolist())
    grouped = frame.groupby(key, sort=False)
    if not grouped.size().eq(len(models)).all():
        raise ValueError("models do not share the complete origin sample")
    if not grouped[["date", "target_date", "y_true"]].nunique().eq(1).all().all():
        raise ValueError("paired labels or timestamps differ")
    origins = frame.drop_duplicates(key)
    if origins.duplicated(["dataset", "horizon", "origin_position"]).any():
        raise ValueError("test origin repeated across folds")
    dates = pd.to_datetime(origins.date, errors="raise")
    endpoints = pd.to_datetime(origins.target_date, errors="raise")
    if not (endpoints > dates).all():
        raise ValueError("target endpoint must follow forecast origin")
    cells = []
    for (dataset, horizon), part in origins.groupby(["dataset", "horizon"], sort=True):
        cells.append(
            {
                "dataset": dataset,
                "horizon": int(horizon),
                "folds": int(part.fold.nunique()),
                "origins": len(part),
                "first_origin": str(part.date.min()),
                "last_origin": str(part.date.max()),
            }
        )
    return {
        "forecast_records": len(frame),
        "dataset_horizon_origins": len(origins),
        "dataset_dates": len(origins.drop_duplicates(["dataset", "date"])),
        "calendar_dates": int(origins.date.nunique()),
        "dataset_horizon_folds": len(origins.drop_duplicates(["dataset", "horizon", "fold"])),
        "models": models,
        "cells": cells,
        "independent_trials": None,
    }


def snapshot(root: Path) -> dict:
    """Bind measured denominators and all published metrics to source hashes."""
    prediction_path = root / "results/walkforward/full/predictions.csv.gz"
    frame = pd.read_csv(prediction_path)
    pieces = []
    for entry in load_catalog(root):
        prices = load_market_csv(root / entry.path)
        dates = prices.date.dt.strftime("%Y-%m-%d")
        positions = pd.Series(np.arange(len(dates)), index=dates)
        part = frame.loc[frame.dataset == entry.name].copy()
        part["origin_position"] = part.date.map(positions)
        if part.origin_position.isna().any():
            raise ValueError("forecast date absent from raw prices")
        origins = part.origin_position.to_numpy(dtype=int)
        endpoints = origins + part.horizon.to_numpy(dtype=int)
        if (endpoints >= len(prices)).any():
            raise ValueError("target endpoint absent from raw prices")
        part["target_date"] = dates.iloc[endpoints].to_numpy()
        close = prices.close.to_numpy()
        actual = np.log(close[endpoints] / close[origins])
        if not np.allclose(actual, part.y_true, rtol=0, atol=1e-12):
            raise ValueError("saved labels differ from raw-price targets")
        pieces.append(part)
    if sum(len(part) for part in pieces) != len(frame):
        raise ValueError("unknown dataset in canonical predictions")
    summary = summarize_predictions(pd.concat(pieces, ignore_index=True))
    paths = [
        "data/nasdaq100.csv",
        "data/SPX.csv",
        "configs/datasets.toml",
        "configs/forecasting.toml",
        "configs/benchmark.toml",
        "results/walkforward/full/predictions.csv.gz",
        "results/walkforward/full/fold_predictions.tar.gz",
        "results/walkforward/full/manifest.json",
        "results/walkforward/full/fold_plan.json",
        "results/walkforward/full/pooled_metrics.csv",
        "results/statistical_reliability/comparisons.csv",
        "results/phase10/comparisons.csv",
        "results/phase11/score_comparisons.csv",
        "results/final_evidence_authenticity_audit/independent_recalculation.json",
        "results/phase12/claims.json",
        "paper/evidence/assets_manifest.json",
        "paper/evidence/manuscript_manifest.json",
    ]
    return {
        "schema_version": 1,
        "scope": (
            "Retrospective dependent forecasts; not independent trials or prospective evidence"
        ),
        "counts": summary,
        "pooled_metrics": pd.read_csv(root / "results/walkforward/full/pooled_metrics.csv").to_dict(
            "records"
        ),
        "sha256": {path: hashlib.sha256((root / path).read_bytes()).hexdigest() for path in paths},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("freeze", "verify"))
    parser.add_argument("--output", type=Path, default=Path("docs/final_metrics.json"))
    args = parser.parse_args()
    current = snapshot(Path(__file__).resolve().parents[2])
    if args.action == "freeze":
        # Exclusive creation forces an explicit review before replacing a freeze.
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(json.dumps(current, indent=2, allow_nan=False) + "\n")
    elif json.loads(args.output.read_text(encoding="utf-8")) != current:
        raise ValueError("frozen metrics or evidence changed; review claims before a new freeze")
    print(json.dumps({"status": "passed", "action": args.action, "counts": current["counts"]}))


if __name__ == "__main__":
    main()
