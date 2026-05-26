"""予測の評価指標計算を担当するモジュール。

回帰タスク向けに MAE / MSE / RMSE / 決定係数 (R^2) を計算する。
"""

from __future__ import annotations

from typing import Dict

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(y_true, y_pred) -> Dict[str, float]:
    """回帰タスクの代表的な評価指標をまとめて辞書で返す。

    Returns:
        {"MAE": ..., "MSE": ..., "RMSE": ..., "R2": ...}
    """
    mse = mean_squared_error(y_true, y_pred)
    return {
        "MAE": float(mean_absolute_error(y_true, y_pred)),
        "MSE": float(mse),
        "RMSE": float(np.sqrt(mse)),
        "R2": float(r2_score(y_true, y_pred)),
    }


def print_metrics(name: str, metrics: Dict[str, float]) -> None:
    """指標を見やすい形で標準出力に表示する。"""
    print(f"=== {name} ===")
    for key, value in metrics.items():
        print(f"  {key:>4}: {value:.4f}")
