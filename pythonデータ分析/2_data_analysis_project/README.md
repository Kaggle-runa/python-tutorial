# California Housing — データ分析プロジェクト雛形

scikit-learn のカリフォルニア住宅価格データセットを題材に、
**1つの ipynb で完結していたコード** を「**ディレクトリ分割した実プロジェクト構成**」
に書き直したサンプルです。

実際のお仕事や Kaggle, インターンの現場で使われるレイアウトに近い形にしています。

---

## ディレクトリ構成

```
data_analysis_project/
├── README.md                   # このファイル (使い方)
├── requirements.txt            # 依存パッケージ
├── .gitignore                  # data/ や models/ の中身を Git 追跡しない設定
├── main.py                     # パイプラインを一括実行するエントリポイント
│
├── data/                       # データ (Git 管理しない方が一般的)
│   ├── raw/                    # 加工していない生データ
│   └── processed/              # 前処理・特徴量生成後のデータ
│
├── models/                     # 学習済みモデルの保存先 (pickle 形式)
│
├── notebooks/                  # 試行錯誤・分析の Jupyter Notebook
│   ├── 01_EDA.ipynb            # 探索的データ解析
│   ├── 02_preprocessing.ipynb  # 前処理と特徴量生成
│   ├── 03_modeling.ipynb       # モデル学習
│   └── 04_evaluation.ipynb     # 評価とチューニング
│
├── src/                        # 再利用可能なロジック (.py モジュール)
│   ├── __init__.py
│   ├── data_loader.py          # データの読み書き
│   ├── preprocessing.py        # 欠損値処理・スケーリング
│   ├── features.py             # 特徴量生成
│   ├── modeling.py             # 学習・保存・読み込み
│   └── evaluation.py           # 評価指標
│
└── docs/                       # 説明資料
    ├── project_structure.md    # ディレクトリ構成の意図と理由
    └── workflow.md             # データ分析の流れ
```

---

## セットアップ

```bash
# 1. 仮想環境の用意 (任意)
python3 -m venv .venv
source .venv/bin/activate

# 2. ライブラリのインストール
pip install -r requirements.txt
```

---

## 使い方

### A. ノートブックで対話的に進める

VSCode / JupyterLab で `notebooks/` 配下のノートブックを **番号順に** 開きます。

1. `01_EDA.ipynb` — どんなデータか把握する
2. `02_preprocessing.ipynb` — 前処理と特徴量生成
3. `03_modeling.ipynb` — モデルを学習
4. `04_evaluation.ipynb` — 評価とチューニング

各ノートブックの先頭セルで `src/` を import するパスを通しているので、
`from src import data_loader, ...` の形でロジックを呼び出せます。

### B. パイプラインを一括実行する

ターミナルからプロジェクトルートで:

```bash
# 線形回帰で実行
python main.py

# XGBoost で実行
python main.py --model xgboost
```

---

## なぜ分割するのか

| 1つの ipynb で完結 | ディレクトリ分割した本構成 |
|-|-|
| 上から下まで実行するだけで分かりやすい | **同じ前処理ロジックを別のノートブックでも再利用できる** |
| 規模が大きくなると重くて開けない | ロジックは .py に, 試行錯誤は ipynb に, と役割を分けられる |
| Git の差分が見にくい (JSON 全体が変わる) | `.py` ファイルは行単位で差分が出るのでレビューしやすい |
| 同僚との分業がしにくい | `src/` 配下のモジュールごとに担当を分けられる |

詳しい思想は [docs/project_structure.md](docs/project_structure.md) と
[docs/workflow.md](docs/workflow.md) を参照してください。

---

## ライセンス・備考

- データセットは scikit-learn 経由で取得します (初回のみネットワーク必要)
- 教材用途で再配布・改変自由です
