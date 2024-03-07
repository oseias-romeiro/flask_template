import unittest
from app import app

routes = ['/', '/account/signin', '/account/create']

class TestApp(unittest.TestCase):

    def setUp(self) -> None:
        # set app as flask instance
        app.testing = True
        self.app = app.test_client()

        return super().setUp()
    
    def test_codes(self):
        for route in self.app.application.url_map.iter_rules():
            
            # route.methods
            if not route.rule.startswith('/static') and not route.rule.startswith('/bootstrap'):
                print(route.rule)
                response = self.app.get(route.rule)
                self.assertNotEqual(response._status_code, 404)

    def test_content_length(self):
        for route in routes:
            response = self.app.get(route)
            self.assertNotEqual(response.calculate_content_length(), 0)

    def test_index(self):
        response = self.app.get(routes[0])
        self.assertIn(b'Flask template', response.data)

    def test_signin(self):
        response = self.app.get(routes[1])
        self.assertIn(b'Sign in', response.data)

    def test_create(self):
        response = self.app.get(routes[2])
        self.assertIn(b'Sign up', response.data)