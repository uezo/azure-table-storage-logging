# azure-table-storage-logging

Azure Table Storageにログを出力するloggingのハンドラー。`logging.Handler`の拡張クラスなので従来のハンドラーと同じ手続きかつ併用できます。

# インストール

```bash
$ pip install azure-table-logging
```

# 使い方

```python:yourapp.py
import logging
from azuretablelogging import AzureTableStorageHandler

# ロガーの取得
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ハンドラーの生成。Azure Storageのアカウント名とキー、ログを記録するテーブル名を指定
handler = AzureTableStorageHandler(
    account_name="your_account_name",
    account_key="your_account_key",
    table_name="table_name"
)

# 生成したハンドラーをロガーに追加
logger.addHandler(handler)

# あとはいつも通りログ出力
logger.debug("デバッグ")
logger.info("情報レベル")
logger.warn("警告レベル")
logger.error("エラーレベル")
logger.critical("致命的レベル")
```

実行すると、`table_name`に指定したテーブルに5レコード追加されます。

PartitionKey|RowKey|Timestamp|LocalTimestamp|LevelName|Level|Message
---|---|---|---|---|---|---
main|251837309460.3795|2019-08-05T07:49:01.574Z|"2019-08-05 16:48:59,220"|CRITICAL|50|致命的レベル
main|251837309460.44092|2019-08-05T07:49:01.504Z|"2019-08-05 16:48:45,687"|ERROR|40|エラーレベル
main|251837309460.51297|2019-08-05T07:49:01.444Z|"2019-08-05 16:48:43,586"|WARNING|30|警告レベル
main|251837309460.77405|2019-08-05T07:49:01.374Z|"2019-08-05 16:48:21,398"|INFO|20|情報レベル
main|251837309498.6117|2019-08-05T07:48:47.676Z|"2019-08-05 16:48:05,928"|DEBUG|10|デバッグ

# 出力項目

カラム名|loggingとの対応|説明
---|---|---
PartitionKey|%(name)s|ロガーの名前
RowKey|n/a|ソートキー。新しいものほど値が小さい。9999年12月31日のEpochからAzure Storageに書き込む直前のEpochを引いたもの
Timestamp|n/a|Azure Storageに書き込まれた時間
LocalTimestamp|%(asctime)s|アプリケーションでログを出力した時点の時間
LevelName|%(levelname)s|ログ出力レベル
Level|%(level)s|ログ出力レベルの数値表現
Message|formatterで指定した値|ログメッセージ。Formatterでフォーマット可能


# その他のポイント

- Azureへの書き込みは別スレッドで処理しており、アプリケーションのパフォーマンスにはほとんど影響を与えません。
- 書き込みはハンドラーインスタンス毎に単一スレッドで行われるため、書き込み順序は保証されます。
- 大量のログを出力した際のパフォーマンスや問題は検証できていません。
- 指定したテーブル名が存在しないときは新規作成します。
