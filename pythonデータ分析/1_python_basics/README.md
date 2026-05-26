# Python 基礎教材 (データ分析入門)

データ分析に必要な Python の **基本文法** と **主要ライブラリ**, さらに実務的な
**データクレンジング** までを学ぶ教材集です。

## 全体構成

**15 章 + 練習問題集** で構成しています。

### 第 I 部: Python 基礎文法 (第 1〜9 章)

| # | ファイル | 学ぶ内容 |
|-|-|-|
| 01 | `01_変数とデータ型.ipynb` | 変数, int/float/str/bool, 型変換, 算術演算子 (`%` も丁寧に) |
| 02 | `02_文字列.ipynb` | インデックス, スライス, `.format()`, f-string, 文字列メソッド |
| 03 | `03_リスト.ipynb` | 作成, スライス, append/insert/pop, 2 次元リスト |
| 04 | `04_辞書とタプル.ipynb` | dict の追加/更新/削除, tuple, set, 4 型の使い分け |
| 05 | `05_条件分岐.ipynb` | if/elif/else, 論理演算子, 三項演算子, 連鎖比較 |
| 06 | `06_繰り返し処理.ipynb` | for, while, continue/break, enumerate/zip, ネストループ |
| 07 | `07_リスト内包表記.ipynb` | フィルタ, 三項式, dict/set 内包表記, ジェネレータ |
| 08 | `08_関数.ipynb` | def, 引数, 戻り値, スコープ, docstring, 型ヒント, lambda |
| 09 | `09_クラス.ipynb` | クラス定義, `__init__`/`self`, **継承, オーバーライド, `super()`** |

### 第 II 部: データ分析ライブラリ入門 (第 10〜14 章)

| # | ファイル | 学ぶ内容 |
|-|-|-|
| 10 | `10_pandas基礎.ipynb` | Series/DataFrame, **loc/iloc**, 条件抽出, **set_index**, **sort_values**, **drop_duplicates**, **value_counts**, **groupby**, **merge** (4 種), **concat**, **fillna** (ffill/bfill), **apply** |
| 11 | `11_numpy基礎.ipynb` | ndarray, ベクトル化, 集約関数, ブロードキャスト, スライス, reshape |
| 12 | `12_matplotlib基礎.ipynb` | 折れ線, 散布図, 棒グラフ, ヒストグラム, 円グラフ, subplot |
| 13 | `13_seaborn基礎.ipynb` | scatterplot, histplot, boxplot, violinplot, heatmap, pairplot |
| 14 | `14_scikit-learn基礎.ipynb` | 共通 API (`fit`/`transform`/`predict`), train_test_split, 線形回帰, 評価指標, Pipeline |

### 第 III 部: 実務編

| # | ファイル | 学ぶ内容 |
|-|-|-|
| 15 | `15_データクレンジング.ipynb` | 表記ゆれ統一, 全角⇔半角, 日付パース, Excel シリアル値, 価格列の正規化 |

### 練習問題

| ファイル | 内容 |
|-|-|
| `練習問題.ipynb` | **10 問の自主練習問題** (本番テスト前の腕試し用) |

---

## 学習の進め方

### 推奨ルート

1. **第 1 章 〜 第 9 章** で Python の基礎文法を順に身につける
2. **第 10 章 〜 第 14 章** でデータ分析ライブラリの使い方を学ぶ
3. **第 15 章** で実務でよく出会う「データの汚れ」と整え方を学ぶ
4. **`練習問題.ipynb`** で力試し
5. 終わったら `../data_analysis_project/` で実際のデータ分析プロジェクトに進む

### 1 章あたりの取り組み方

各章は次の流れで構成されています:

1. **学習目標** (この章でできるようになること)
2. **概念の説明** (図・表でやさしく)
3. **コード例** (実行して結果を確認)
4. **練習問題** (各章末で確認)
5. **まとめ**

**コードセルを実行する前に「結果を予想する」** ことが上達のコツです。
予想と違ったら何が起きたか考えてみましょう。

---

## 必要なライブラリ

最低限以下があれば動きます。

```bash
pip install jupyter numpy pandas scikit-learn matplotlib seaborn japanize-matplotlib jaconv
```

`jaconv` は第 15 章 (データクレンジング) の全角⇔半角変換でのみ使います。
入っていなくても他の章の動作には影響しません。

VSCode / JupyterLab / Google Colab のどれでも開けます。

---

## 練習問題集の使い方

`練習問題.ipynb` は 10 問構成で、本番テスト前の **自主トレ** 用です。

- 各問題のあとに **解答と詳しい解説** を載せています
- 解答セルを実行する前に、自分で頭の中で結果を予想してください
- 間違えたら、該当章を読み直してから再挑戦

> 本番テストには **数字や変数を変えた類題** が出ます。
> 教材内の例題と練習問題は本番テストとは別パターンになっています。
> 解き方の手順 (とくに while + continue + break, merge, fillna) を覚えるのが目標です。
