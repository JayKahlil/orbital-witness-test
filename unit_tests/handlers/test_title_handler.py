import unittest
from unittest.mock import patch

from fastapi import HTTPException

from app.handlers.title_handler import list_titles, get_title_by_id


def get_mocked_data():
    return [
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


class TestTitleHandler(unittest.TestCase):

    @patch('app.handlers.title_handler.get_title_data')
    def test_list_titles(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()
        expected = [
            {
                "id": "0",
                "title_number": "MYBKZ10625",
                "title_class": "Freehold",
            },
            {
                "id": "1",
                "title_number": "GP51",
                "title_class": "Leasehold",
            }
        ]

        titles, total = list_titles(1, 5, "id", "asc")

        self.assertListEqual(titles, expected)
        self.assertEqual(total, 2)

    @patch('app.handlers.title_handler.get_title_data')
    def test_list_titles_filter_title_class(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()
        expected = [
            {
                "id": "1",
                "title_number": "GP51",
                "title_class": "Leasehold",
            }
        ]

        titles, total = list_titles(1, 5, "id", "asc", "Leasehold")

        self.assertListEqual(titles, expected)
        self.assertEqual(total, 1)

    @patch('app.handlers.title_handler.get_title_data')
    def test_list_titles_second_page(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()
        expected = [
            {
                "id": "1",
                "title_number": "GP51",
                "title_class": "Leasehold",
            }
        ]

        titles, total = list_titles(2, 1, "id", "asc")

        self.assertListEqual(titles, expected)
        self.assertEqual(total, 2)

    @patch('app.handlers.title_handler.get_title_data')
    def test_list_titles_second_page_empty(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()
        expected = []

        titles, total = list_titles(2, 5, "id", "asc")

        self.assertListEqual(titles, expected)
        self.assertEqual(total, 2)

    @patch('app.handlers.title_handler.get_title_data')
    def test_list_titles_reverse_title_number_order(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()
        expected = [
            {
                "id": "1",
                "title_number": "GP51",
                "title_class": "Leasehold",
            },
            {
                "id": "0",
                "title_number": "MYBKZ10625",
                "title_class": "Freehold",
            }
        ]

        titles, total = list_titles(1, 5, "title_number", "asc")

        self.assertListEqual(titles, expected)
        self.assertEqual(total, 2)

    @patch('app.handlers.title_handler.get_title_data')
    def test_list_titles_mismatch_sort_and_order_count(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()

        with self.assertRaises(HTTPException) as context:
            list_titles(1, 5, "title_number", "asc,desc")

        self.assertEqual(context.exception.detail, "Number of sort and order values must match")
        self.assertEqual(context.exception.status_code, 400)

    @patch('app.handlers.title_handler.get_title_data')
    def test_list_titles_invalid_sort_type(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()

        with self.assertRaises(HTTPException) as context:
            list_titles(1, 5, "title_class", "asc")

        self.assertEqual(context.exception.detail, "Sort type must be 'id' or 'title_number'")
        self.assertEqual(context.exception.status_code, 400)

    @patch('app.handlers.title_handler.get_title_data')
    def test_get_title_by_id(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()
        expected = {
            "id": "1",
            "title_number": "GP51",
            "title_class": "Leasehold",
            "content": "more test content"
        }

        title = get_title_by_id("1")

        self.assertEqual(title, expected)

    @patch('app.handlers.title_handler.get_title_data')
    def test_get_title_by_id_not_found(self, mock_get_title_data):
        mock_get_title_data.return_value = get_mocked_data()

        with self.assertRaises(HTTPException) as context:
            get_title_by_id("3")

        self.assertEqual(context.exception.detail, "Title with ID 3 not found")
        self.assertEqual(context.exception.status_code, 404)
