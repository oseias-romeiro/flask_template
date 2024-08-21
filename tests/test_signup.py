import unittest, os

from app import app

class SignUpTest(unittest.TestCase):

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
        print("\n# Testing signup with blank data")

        response = self.app.post('/signup', follow_redirects=True)
        self.assertIn(b'This field is required.', response.data)

    def test_invalid_email(self):
        print("\n# Testing signup with invalid email")

        response = self.app.post('/signup', data=dict(
            username="testuser",
            email="invalidemail",
            password="1234"
        ), follow_redirects=True)
        self.assertIn(b"Digit a valid email address", response.data)
    
    def test_invalid_password(self):
        print("\n# Testing signup with invalid password")

        response = self.app.post('/signup', data=dict(
            username="testuser",
            email="testuser@email.com",
            password="1234"
        ), follow_redirects=True)
        self.assertIn(b"Password must contain at least 8 characteres and one digit, one uppercase letter ad one special symbol", response.data)

    def test_success(self):
        print("\n# Testing signup with success")

        response = self.app.post('/signup', data=dict(
            username="testuser1",
            email="testuser1@email.com",
            password="Test#1234",
            confirm="Test#1234"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
