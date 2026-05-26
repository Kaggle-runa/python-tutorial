"""カリフォルニア住宅価格データ分析プロジェクト。

各モジュールの役割は以下のとおり。

- `data_loader` : データの取得と CSV 保存/読み込み
- `preprocessing` : 欠損値処理・スケーリングなどの前処理
- `features` : 特徴量生成
- `modeling` : モデルの学習・保存・読み込み
- `evaluation` : 予測の評価指標計算と可視化
"""

__all__ = [
    "data_loader",
    "preprocessing",
    "features",
    "modeling",
    "evaluation",
]
