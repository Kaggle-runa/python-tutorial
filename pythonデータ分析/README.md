# Python データ分析 入門教材

データ分析を学ぶための **2 部構成** の教材です。

```
pythonデータ分析/
├── python_basics/                   ← Part 1: Python と主要ライブラリの基礎
│   ├── 01_変数とデータ型.ipynb      ── 第 I 部 (基礎文法)
│   ├── 02_文字列.ipynb
│   ├── 03_リスト.ipynb
│   ├── 04_辞書とタプル.ipynb
│   ├── 05_条件分岐.ipynb
│   ├── 06_繰り返し処理.ipynb
│   ├── 07_リスト内包表記.ipynb
│   ├── 08_関数.ipynb
│   ├── 09_クラス.ipynb              ── (継承 / super() / オーバーライドを含む)
│   ├── 10_pandas基礎.ipynb         ── 第 II 部 (主要ライブラリ)
│   ├── 11_numpy基礎.ipynb
│   ├── 12_matplotlib基礎.ipynb
│   ├── 13_seaborn基礎.ipynb
│   ├── 14_scikit-learn基礎.ipynb
│   ├── 15_データクレンジング.ipynb  ── 第 III 部 (実務編: 表記ゆれ/全角半角/日付)
│   └── 練習問題.ipynb               ── 10 問の自主トレ問題集
│
├── data_analysis_project/          ← Part 2: ディレクトリ分割した実プロジェクト
│   ├── README.md
│   ├── main.py
│   ├── data/   (raw/, processed/)
│   ├── models/
│   ├── notebooks/                  ── EDA → 前処理 → 学習 → 評価の 4 ノート
│   │   ├── 01_EDA.ipynb
│   │   ├── 02_preprocessing.ipynb
│   │   ├── 03_modeling.ipynb
│   │   └── 04_evaluation.ipynb
│   ├── src/                        ── 再利用ロジック (.py)
│   │   ├── data_loader.py
│   │   ├── preprocessing.py
│   │   ├── features.py
│   │   ├── modeling.py
│   │   └── evaluation.py
│   └── docs/                       ── 説明資料
│       ├── project_structure.md
│       └── workflow.md
│
├── image/                          ← テスト問題のスクリーンショット (参考)
└── データ分析の事始め.ipynb         ← 元の単一ノートブック (参考用)
```

---

## Part 1: `python_basics/` — Python と主要ライブラリの基礎

データ分析を始めるにあたって必要な **Python の文法**、**主要ライブラリ**、**実務的なデータクレンジング** を学ぶ 15 章 + 練習問題集。

### 第 I 部: Python 基礎文法 (第 1〜9 章)

| 章 | テーマ |
|-|-|
| 01 | 変数とデータ型 |
| 02 | 文字列 |
| 03 | リスト |
| 04 | 辞書とタプル |
| 05 | 条件分岐 |
| 06 | 繰り返し処理 |
| 07 | リスト内包表記 |
| 08 | 関数 |
| 09 | クラス (継承 / super() / オーバーライドまで) |

### 第 II 部: データ分析ライブラリ入門 (第 10〜14 章)

| 章 | テーマ |
|-|-|
| 10 | pandas (loc/iloc, set_index, sort_values, groupby, **merge**, concat, **fillna**, apply など) |
| 11 | numpy (ndarray, ベクトル化, 集約) |
| 12 | matplotlib (折れ線, 散布図, ヒスト, 棒グラフ) |
| 13 | seaborn (heatmap, pairplot, boxplot) |
| 14 | scikit-learn (共通 API, 線形回帰, 評価指標) |

### 第 III 部: 実務編 (第 15 章)

| 章 | テーマ |
|-|-|
| 15 | データクレンジング (表記ゆれ統一, 全角⇔半角, 日付パース, Excel シリアル値) |

### 練習問題

10 問の自主トレ問題集 (`練習問題.ipynb`)。本番テスト前のウォームアップ用。

詳細は [python_basics/README.md](python_basics/README.md) を参照。

---

## Part 2: `data_analysis_project/` — データ分析プロジェクトの作り方

元の `データ分析の事始め.ipynb` (1 つのノートで完結している) を、
**実プロジェクトで使われるディレクトリ構成** に分割し直したサンプルです。
内容も「データ分析の事始め.ipynb」を踏まえつつ、各工程をさらに丁寧に説明しています。

### ノートブック構成 (順番に読む)

| # | ファイル | 内容 |
|-|-|-|
| 01 | `01_EDA.ipynb` | 探索的データ解析: 統計量・相関・分布の解釈、散布図、地理プロット、外れ値検出 |
| 02 | `02_preprocessing.ipynb` | 前処理: 欠損値 3 手法 (drop/dropna/fillna)、エンコーディング 2 手法 (One-hot/Label)、スケーリング 2 手法 (正規化/標準化)、特徴量生成 |
| 03 | `03_modeling.ipynb` | モデル学習: ホールドアウト法 / k-fold CV、線形回帰・Ridge・Lasso・決定木・Random Forest の比較 |
| 04 | `04_evaluation.ipynb` | 評価とチューニング: 回帰指標 (MAE/MSE/RMSE/R²)、分類指標 (混同行列/Precision/Recall/F1)、クリッピング後処理、アンサンブル学習、XGBoost との比較、残差プロット |

### サクッと試す

```bash
cd data_analysis_project
pip install -r requirements.txt

python main.py                  # 線形回帰で一括実行
python main.py --model xgboost  # XGBoost で一括実行
```

ノートブックで対話的に進めたい場合は `data_analysis_project/notebooks/` を開いてください。

### ディレクトリ構成の意図

- `data/raw/` `data/processed/` でデータの加工状態を分離
- `src/` に **再利用可能なロジック** を配置
- `notebooks/` は **試行錯誤** に専念
- `models/` に学習済みモデルを保存

詳細:
- [data_analysis_project/docs/project_structure.md](data_analysis_project/docs/project_structure.md): ディレクトリ構成の意図
- [data_analysis_project/docs/workflow.md](data_analysis_project/docs/workflow.md): データ分析の流れ
- [data_analysis_project/README.md](data_analysis_project/README.md): 使い方

---

## どちらから始めるべきか

| あなたは… | 始めるべき場所 |
|-|-|
| Python そのものに慣れていない | Part 1 の第 1 章から順に |
| Python は書けるがライブラリは初めて | Part 1 の第 10 章から |
| データ分析プロジェクトの構成を知りたい | Part 2 から |
| 本番テスト前に腕試ししたい | `python_basics/練習問題.ipynb` |

両方やると、

> 「Python の文法 → 主要ライブラリ → データ分析の型 → 実プロジェクト構成」

の一連の流れを体験できます。
