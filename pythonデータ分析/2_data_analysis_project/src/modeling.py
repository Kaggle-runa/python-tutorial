"""モデルの学習と保存・読み込みを担当するモジュール。

- 学習: train_linear_regression / train_xgboost
- 保存: save_model (pickle ベース)
- 読込: load_model
"""

from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = PROJECT_ROOT / "models"


def split_train_test(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 0,
):
    """学習用/検証用にデータを分割する。"""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_linear_regression(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """線形回帰モデルを学習して返す。"""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def train_xgboost(X_train: pd.DataFrame, y_train: pd.Series):
    """XGBoost (勾配ブースティング) モデルを学習して返す。

    xgboost がインストールされていない場合、明示的にエラーを出す。
    """
    try:
        from xgboost import XGBRegressor
    except ImportError as e:
        raise ImportError(
            "xgboost が必要です。`pip install xgboost` を実行してください。"
        ) from e

    model = XGBRegressor(random_state=0)
    model.fit(X_train, y_train)
    return model


def predict_with_clipping(
    model,
    X: pd.DataFrame,
    lower: float = 0.0,
    upper: float = 5.00001,
) -> np.ndarray:
    """予測値を [lower, upper] の範囲にクリッピングする後処理つき推論。

    California housing データは Price が 5.00001 で上限処理されているため、
    予測値も同じ範囲に丸めることで指標がわずかに改善する。
    """
    pred = model.predict(X)
    return np.clip(pred, lower, upper)


def save_model(model, name: str) -> Path:
    """学習済みモデルを `models/<name>.pkl` に保存。"""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    path = MODELS_DIR / f"{name}.pkl"
    with open(path, "wb") as f:
        pickle.dump(model, f)
    return path


def load_model(name: str):
    """`models/<name>.pkl` から学習済みモデルを読み込む。"""
    path = MODELS_DIR / f"{name}.pkl"
    with open(path, "rb") as f:
        return pickle.load(f)
