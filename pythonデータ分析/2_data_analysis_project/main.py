"""データ分析パイプラインを一括実行するエントリポイント。

ターミナルから実行する例:

    python main.py
    python main.py --model xgboost

実行すると以下の順で処理が走る:

    1. 生データ取得   (data/raw/california_housing.csv)
    2. 特徴量生成     (Household / AllRooms / AllBedrms を追加)
    3. 学習/検証分割
    4. モデル学習     (LinearRegression もしくは XGBoost)
    5. クリッピング付き推論
    6. 評価指標の表示
    7. 学習済みモデルを models/ に保存
"""

from __future__ import annotations

import argparse

from src import data_loader, evaluation, features, modeling


def run(model_name: str = "linear", test_size: float = 0.2, random_state: int = 2) -> None:
    print("=" * 60)
    print(f"start pipeline: model={model_name}")
    print("=" * 60)

    print("\n[1/6] load raw data ...")
    df = data_loader.load_raw()
    print(f"  shape = {df.shape}")

    print("\n[2/6] feature engineering ...")
    df = features.add_household_features(df)
    data_loader.save_processed(df, "california_housing_fe")
    print(f"  columns = {df.columns.tolist()}")

    print("\n[3/6] train/test split ...")
    X, y = features.split_features_target(df, target_col="Price")
    X_train, X_test, y_train, y_test = modeling.split_train_test(
        X, y, test_size=test_size, random_state=random_state,
    )
    print(f"  train: {X_train.shape}, test: {X_test.shape}")

    print(f"\n[4/6] train model ({model_name}) ...")
    if model_name == "linear":
        model = modeling.train_linear_regression(X_train, y_train)
    elif model_name == "xgboost":
        model = modeling.train_xgboost(X_train, y_train)
    else:
        raise ValueError(f"unknown model: {model_name}")

    print("\n[5/6] predict with clipping ...")
    y_pred = modeling.predict_with_clipping(model, X_test)

    print("\n[6/6] evaluate ...")
    metrics = evaluation.regression_metrics(y_test, y_pred)
    evaluation.print_metrics(model_name, metrics)

    saved = modeling.save_model(model, model_name)
    print(f"\nmodel saved to: {saved}")
    print("done.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run California housing pipeline.")
    parser.add_argument(
        "--model",
        choices=["linear", "xgboost"],
        default="linear",
        help="使用するモデルの種類 (default: linear)",
    )
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--seed", type=int, default=2)
    args = parser.parse_args()
    run(model_name=args.model, test_size=args.test_size, random_state=args.seed)


if __name__ == "__main__":
    main()
