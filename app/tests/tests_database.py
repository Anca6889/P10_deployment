"""Intergation test of the database generation process"""

from django.test import TestCase
from unittest.mock import patch
from app.management.commands.database import Command


class Databasetests(TestCase):
    """
    This class will fo a global integration tests with two mocks:
    The request method to OFF API and the handle method who is exacly the same
    as original but with adding a result string to check if everything worked.
    """

    def setUp(self):
        """Instance the class"""

        self.db = Command()

    def mock_handle(self):
        """Setup the handle mock"""

        self.launch_process()
        return "everything is running fine"

    def mock_request_api(self):
        """Setup the API request method mock with fake results"""

        mock_results = [
            [
                {
                    "product_name_fr": "testname",
                    "brands": "testbrand",
                    "nutriscore_grade": "e",
                    "stores": "teststore",
                    "url": "test/url.com",
                    "image_front_url": "testimage",
                    "categories": "cat1"
                },
                {
                    "product_name_fr": "testname2",
                    "brands": "testbrand2",
                    "nutriscore_grade": "a",
                    "stores": "teststore2",
                    "url": "test/url.com2",
                    "image_front_url": "testimage2",
                    "categories": "cat2"
                },
            ],
        ]

        self.delete_uncomplete_products(mock_results)

    @patch("app.management.commands.database.Command.handle", mock_handle)
    @patch("app.management.commands.database.Command.request_off_api",
           mock_request_api)
    def test_database_process(self):
        """Lauch the integration test with the two mocks"""

        response = self.db.handle()
        self.assertEqual(response, "everything is running fine")
