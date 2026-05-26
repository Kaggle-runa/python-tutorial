"""特徴量生成を担当するモジュール。

カリフォルニア住宅価格データに対して、既存列を組み合わせて
新しい特徴量を追加する。
"""

from __future__ import annotations

import pandas as pd


def add_household_features(df: pd.DataFrame) -> pd.DataFrame:
    """世帯数, 合計居室数, 合計寝室数を追加する。

    | 既存列 | 意味 |
    |-|-|
    | Population | ブロックの人口 |
    | AveOccup   | 平均世帯人口 |
    | AveRooms   | 1世帯あたりの平均居室数 |
    | AveBedrms  | 1世帯あたりの平均寝室数 |

    平均世帯人口 = 人口 / 世帯数 という関係から、

    | 追加列 | 計算式 |
    |-|-|
    | Household  | Population / AveOccup |
    | AllRooms   | Household * AveRooms  |
    | AllBedrms  | Household * AveBedrms |
    """
    df = df.copy()
    df["Household"] = df["Population"] / df["AveOccup"]
    df["AllRooms"] = df["Household"] * df["AveRooms"]
    df["AllBedrms"] = df["Household"] * df["AveBedrms"]
    return df


def split_features_target(
    df: pd.DataFrame,
    target_col: str = "Price",
) -> tuple[pd.DataFrame, pd.Series]:
    """目的変数列を分離して (X, y) を返す。"""
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y
