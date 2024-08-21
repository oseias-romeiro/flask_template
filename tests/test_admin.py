
import unittest, os

from app import app
from models.User import Role

class AdminTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.system('flask db upgrade')
        os.system('flask seed users')
    
    @classmethod
    def tearDownClass(cls):
        os.system('flask db downgrade')

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        self.app.application.config['WTF_CSRF_ENABLED'] = False # disable CSRF protection
        self.routes = app.url_map.iter_rules()

    def login(self, username, password):
        return self.app.post('/signin', data=dict(
            username=username,
            password=password
        ))
    
    def logout(self):
        self.app.get('/signout')
        
    def test_adminDeleteUser(self):
        print("\n# Testing Admin delete users")

        self.login('bob', '1234')

        response = self.app.post('/account/john/delete', follow_redirects=True)
        self.assertIn(b"User deleted", response.data)
        
        self.logout()
    
    def test_adminChangeUserRole(self):
        print("\n# Testing Admin change users role")

        self.login('bob', '1234')
        
        response = self.app.get(f'/admin/panel/role?username=jane&role={Role.USER}', follow_redirects=True)
        self.assertIn(b"jane's role changed", response.data)

        self.logout()
    
