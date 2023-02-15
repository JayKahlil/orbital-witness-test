import unittest
from unittest.mock import patch

from app.dependencies.data_store import get_title_data


class TestDataStore(unittest.TestCase):

    @patch('app.dependencies.data_store.DATA_FILE_PATH', 'unit_tests/test_data.json')
    def test_get_data(self):
        result = get_title_data()

        expected = [
            {
                "id": "0",
                "title_number": "MYBKZ10625",
                "title_class": "Freehold",
                "content": "test content"
            },
            {
                "id": "1",
                "title_number": "GP51",
                "title_class": "Leasehold",
                "content": "more test content"
            }
        ]

        self.assertListEqual(result, expected)
