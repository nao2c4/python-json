"""ランダムなユーザ情報を生成し、jsonファイルに保存する。"""

import argparse
import json
import random
from datetime import date, timedelta
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """コマンドライン引数をパースする。

    Returns:
        argparse.Namespace: パース結果。
    """
    parser = argparse.ArgumentParser(
        description="Create random user information and save it to a json file."
    )
    parser.add_argument("-n", type=int, default=20_000, help="The number of users.")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("data/sample.json"), help="The output file."
    )
    return parser.parse_args()


def create_users(n: int) -> list[dict[str, str]]:
    """ランダムなユーザ情報を生成する。

    Args:
        n (int): ユーザ数。

    Returns:
        list[dict[str, str]]: ユーザ情報のリスト。
    """
    users = [
        {"name": create_random_name(), "birthday": create_random_date().strftime("%Y-%m-%d")}
        for _ in range(n)
    ]
    # 名前の重複をチェックする。
    # 重複がある場合は、名前を再生成する。
    # 無限ループ対策はしていない。
    names = {user["name"] for user in users}
    if len(names) < n:
        users = create_users(n)
    return users


def create_json(n: int, output: Path) -> None:
    """ランダムなユーザ情報を生成し、jsonファイルに保存する。

    Args:
        n (int): ユーザ数。
        output (Path): 出力ファイル。
    """
    metadata = {"version": "1.0.0", "author": "nao2c4"}
    users = [
        {"name": create_random_name(), "birthday": create_random_date().strftime("%Y-%m-%d")}
        for _ in range(n)
    ]

    with output.open("w") as f:
        json.dump({"metadata": metadata, "users": users}, f, indent=4)


def create_random_name(n: int = 10) -> str:
    """ランダムな名前を生成する。

    Args:
        n (int): 名前の長さ。

    Returns:
        str: ランダムな名前。
    """
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=n))  # noqa: S311


def create_random_date(criterion: date = date(1900, 1, 1), days_range: int = 40_000) -> date:
    """ランダムな日付を生成する。

    Args:
        criterion (date, optional): 基準日。Defaults to date(1900, 1, 1).
        days_range (int, optional): ランダムに取る日数の範囲。Defaults to 40_000.

    Returns:
        date: ランダムな日付。
    """
    return criterion + timedelta(days=random.randint(0, days_range))  # noqa: S311


def main() -> None:
    """メイン関数。"""
    args = parse_args()
    create_json(args.n, args.output)


if __name__ == "__main__":
    main()
