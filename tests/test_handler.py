import sys
import os
sys.path.append(os.pardir)
import unittest
import logging
from uuid import uuid4
from azure.cosmosdb.table import TableService
from azuretablelogging import AzureTableStorageHandler

# configure
account_name = "your_account_name"
account_key = "your_account_key"
table_name = "table_name_for_this_session"


class TestAutomata(unittest.TestCase):
    def test_logging(self):
        # key to identify this session
        test_id = str(uuid4())

        # setup logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # setup handler and add to logger
        handler = AzureTableStorageHandler(
            account_name=account_name,
            account_key=account_key,
            table_name=table_name
        )
        logger.addHandler(handler)

        # write logs
        logger.debug(f"DEBUG: {test_id}")
        logger.info(f"INFO: {test_id}")
        logger.warning(f"WARNING: {test_id}")
        logger.error(f"ERROR: {test_id}")
        logger.critical(f"CRITICAL: {test_id}")

        # get log messages
        ts = TableService(account_name=account_name, account_key=account_key)
        for ent in ts.query_entities(table_name=table_name, filter="PartitionKey eq '__main__'"):
            self.assertEqual(ent["LevelName"] + ": " + test_id, ent["Message"])

if __name__ == "__main__":
    unittest.main()
