"""データの前処理を担当するモジュール。

- 欠損値処理 (fill_missing)
- スケーリング (scale_features)
"""

from __future__ import annotations

from typing import Iterable, Literal

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def fill_missing(
    df: pd.DataFrame,
    strategy: Literal["mean", "median", "ffill", "drop"] = "mean",
) -> pd.DataFrame:
    """数値列の欠損値を指定の戦略で埋める/取り除く。

    Args:
        df: 入力 DataFrame
        strategy:
            - "mean"   : 列ごとの平均で埋める
            - "median" : 列ごとの中央値で埋める
            - "ffill"  : 直前の値で埋める (時系列で有用)
            - "drop"   : 欠損を含む行を削除

    Returns:
        欠損値処理後の DataFrame (元の df は変更しない)。
    """
    df = df.copy()

    if strategy == "drop":
        return df.dropna(axis=0)

    if strategy == "ffill":
        return df.fillna(method="ffill")

    numeric_cols = df.select_dtypes(include="number").columns
    if strategy == "mean":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    elif strategy == "median":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    else:
        raise ValueError(f"unknown strategy: {strategy}")

    return df


def scale_features(
    df: pd.DataFrame,
    columns: Iterable[str],
    method: Literal["standard", "minmax"] = "standard",
) -> tuple[pd.DataFrame, object]:
    """指定列にスケーリングを適用する。

    Args:
        df: 入力 DataFrame
        columns: スケーリング対象の列名
        method: "standard" (平均0/分散1) または "minmax" (0-1)

    Returns:
        (スケーリング後の DataFrame, 学習済み Scaler) のタプル。
        Scaler は学習用データで fit したものを保存し、テスト用には
        transform だけ使う想定。
    """
    df = df.copy()
    columns = list(columns)

    if method == "standard":
        scaler = StandardScaler()
    elif method == "minmax":
        scaler = MinMaxScaler()
    else:
        raise ValueError(f"unknown method: {method}")

    df[columns] = scaler.fit_transform(df[columns])
    return df, scaler


def apply_scaler(df: pd.DataFrame, columns: Iterable[str], scaler) -> pd.DataFrame:
    """学習済み scaler を適用する (テストデータ用)。"""
    df = df.copy()
    df[list(columns)] = scaler.transform(df[list(columns)])
    return df
