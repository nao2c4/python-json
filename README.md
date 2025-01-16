# Python で json ファイルを開こう

Python で json ファイルを扱う方法を紹介します。

## How to use

### 読み込む json ファイルを作成

`create_json.py` を実行し、 `data/sample.json` を作成します。

```bash
$ python create_json.py
``` 

作成された `data/sample.json` は以下のようになります。 `users` には 20,000 人分のデータが含まれています。

```json
{
    "metadata": {
        "version": 1.0,
        "author": "nao2c4"
    },
    "users": [
        {
            "name": "Alice",
            "birthday": "2000-01-01"
        },
        {
            "name": "Bob",
            "birthday": "2000-02-02"
        }
    ]
}
```

### 基本的な使い方

[json ファイルの基本的な扱い方](notebooks/sample_01_basic.ipynb) を参照してください。

### pandas との連携

[pandas との連携](notebooks/sample_02_pandas.ipynb) を参照してください。

### Pydantic を使ってみる

[Pydantic を使ってみる](notebooks/sample_03_pydantic.ipynb) を参照してください。
