import unittest

from app import app
from tests.mockUsers import getSimpleUser, getAdminUser
from tests.describe_routes import routes

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.app.application.config['WTF_CSRF_ENABLED'] = False # disable CSRF protection

        # mock users
        self.simpleUser = getSimpleUser()
        self.adminUser = getAdminUser()

        # persist users
        self.signup(self.simpleUser.username, self.simpleUser.email, self.simpleUser.password)
        self.signup(self.adminUser.username, self.adminUser.email, self.adminUser.password)
        

    def tearDown(self):
        pass

    def login(self, username, password):
        return self.app.post('/account/signin', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)
    
    def logout(self):
        return self.app.get('/account/signout', follow_redirects=True)

    def signup(self, username, email, password):
        return self.app.post('/account/create', data=dict(
            username=username,
            email=email,
            password=password,
            confirm=password
        ), follow_redirects=True)

    def test_routes(self):
        print("\n# Testing response codes and content length")
        
        static_paths = ['/static/media/flask-icon.png', '/static/media/flask-logo.png']

        for route in routes:
            with self.subTest(route=route):
                if routes[route]['authRequired']:
                    response = self.app.get(route)
                    self.assertEqual(response.status_code, 401)
                    response = self.login('test', 'Test#1234')
                    self.assertEqual(response.status_code, 200)
                    self.logout()
                else: 
                    response = self.app.get(route)
                    self.assertEqual(response.status_code, 200)
                    self.assertNotEqual(len(response.data), 0)

        for path in static_paths:
            with self.subTest(path=path):
                with self.app.get(path) as response:
                    self.assertEqual(response.status_code, 200)
                    self.assertNotEqual(len(response.data), 0)

    def test_index(self):
        response = self.app.get('/')
        self.assertIn(b'<title>Flask template</title>', response.data)

    def test_signin(self):
        response = self.app.get('/account/signin')
        self.assertIn(b'<title>Sign in</title>', response.data)

    def test_create(self):
        response = self.app.get('/account/create')
        self.assertIn(b'<title>Sign up</title>', response.data)
    
    def test_home(self):
        self.login(self.simpleUser.username, self.simpleUser.password)
        response = self.app.get('/account/home')
        self.assertIn(b'<title>Wellcome</title>', response.data)
        self.logout()

if __name__ == '__main__':
    unittest.main()
