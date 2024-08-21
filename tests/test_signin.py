import unittest, os

from app import app

class SignInTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.system('flask db upgrade')
        os.system('flask seed users')
    
    @classmethod
    def tearDownClass(cls):
        os.system('flask db downgrade')
        
    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client()
        self.app.application.config['WTF_CSRF_ENABLED'] = False # disable CSRF protection
        
    def test_blank(self):
        print("\n# Testing signin with blank data")

        response = self.app.post('/signin', follow_redirects=True)
        self.assertIn(b'This field is required.', response.data)
    
    def test_nouser(self):
        print("\n# Testing signin with not exist user")

        response = self.app.post('/signin', data=dict(
            username="anyone",
            password="1234"
        ), follow_redirects=True)
        self.assertIn(b'Incorrect username/password', response.data)
    
    def test_wrongpass(self):
        print("\n# Testing signin with wrong password")

        response = self.app.post('/signin', data=dict(
            username="jane",
            password="123"
        ), follow_redirects=True)
        self.assertIn(b'Incorrect username/password', response.data)

    def test_success(self):
        print("\n# Testing signin with success")

        response = self.app.post('/signin', data=dict(
            username="jane",
            password="1234"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    