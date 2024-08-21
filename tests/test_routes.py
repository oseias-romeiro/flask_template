import unittest, os

from app import app

class RouteTest(unittest.TestCase):
    
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

    def test_routes_noauthed(self):
        print("\n# Testing GET routes with no session")

        for route in self.routes:
            if 'public_app.' in route.endpoint and 'GET' in route.methods:
                response = self.app.get(route.rule)
                self.assertEqual(response.status_code, 200)
            
            elif ('account_app.' in route.endpoint or 'admin_app.' in route.endpoint) and 'GET' in route.methods:
                response = self.app.get(route.rule, follow_redirects=True)
                self.assertIn(b'<title>Sign in</title>', response.data)
    
    def test_authedRoutes(self):
        print("\n# Testing GET routes with normal user authenticated")

        

        for route in self.routes:
            with self.subTest(route=route):
                if 'GET' in route.methods and 'account_app.' in route.endpoint:
                    self.login('jane', '1234')
                    
                    response = self.app.get(route.rule, follow_redirects=True)
                    self.assertEqual(response.status_code, 200)
                    
                    self.logout()
                elif 'GET' in route.methods and 'admin_app.' in route.endpoint:
                    self.login('jane', '1234')

                    response = self.app.get(route.rule, follow_redirects=True)
                    self.assertIn(b'Wellcome', response.data)

                    self.logout()
    
    def test_adminRoutes(self):
        print("\n# Testing GET routes with admin user authenticated")

        for route in self.routes:
            with self.subTest(route=route):

                if 'GET' in route.methods and 'account_app.' in route.endpoint or 'admin_app.' in route.endpoint:
                    self.login('bob', '1234')
                    
                    response = self.app.get(route.rule, follow_redirects=True)
                    self.assertEqual(response.status_code, 200)
                    
                    self.logout()
        
    
    def test_notFound(self):
        print("\n# Testing not found page")

        response = self.app.get("/0248gtroqfahvc")
        self.assertEqual(response.status_code, 404)
