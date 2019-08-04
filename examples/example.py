import logging
from azuretablelogging import AzureTableStorageHandler

# setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# setup handler and add to logger
handler = AzureTableStorageHandler(
    account_key="your_account_key",
    account_name="your_account_name",
    table_name="table_name"
)
logger.addHandler(handler)

# write logs
logger.debug("デバッグ")
logger.info("情報レベル")
logger.warn("警告レベル")
logger.error("エラーレベル")
logger.critical("致命的レベル")
