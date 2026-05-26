"""データの取得と入出力を担当するモジュール。

- 元データは sklearn の California housing dataset
- 取得した DataFrame は `data/raw/california_housing.csv` に保存して
  次回以降はキャッシュから読み込む
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.datasets import fetch_california_housing

# プロジェクトルートから見た data/ 配下のパス
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
RAW_CSV = RAW_DIR / "california_housing.csv"


def load_raw(use_cache: bool = True) -> pd.DataFrame:
    """カリフォルニア住宅価格データセットを DataFrame として取得する。

    Args:
        use_cache: True なら `data/raw/california_housing.csv` がある場合は
            そちらから読み込む (sklearn のダウンロードを回避)。

    Returns:
        説明変数と目的変数 (`Price`) を含む DataFrame。
    """
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if use_cache and RAW_CSV.exists():
        return pd.read_csv(RAW_CSV)

    dataset = fetch_california_housing()
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    df["Price"] = dataset.target

    df.to_csv(RAW_CSV, index=False)
    return df


def save_processed(df: pd.DataFrame, name: str) -> Path:
    """前処理済みデータを `data/processed/<name>.csv` に保存する。"""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    path = PROCESSED_DIR / f"{name}.csv"
    df.to_csv(path, index=False)
    return path


def load_processed(name: str) -> pd.DataFrame:
    """前処理済みデータを読み込む。"""
    path = PROCESSED_DIR / f"{name}.csv"
    return pd.read_csv(path)
