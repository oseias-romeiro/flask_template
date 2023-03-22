import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self) -> None:
        # set app as flask instance
        app.testing = True
        self.app = app.test_client()

        return super().setUp()

    def test_index(self):
        """
        Test index route
        """

        index = self.app.get('/')

        self.assertEqual(
            index._status_code, 200,
            "Error in response code of index route"
        )
