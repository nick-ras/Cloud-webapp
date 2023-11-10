# base_test.py
import unittest
from src import create_app, db
from src import User

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Create an instance of the app with the testing configuration
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        # Set up the database
        db.create_all()

        # Add a test user
        test_user = User(email='test@example.com', password='testpassword')
        db.session.add(test_user)
        db.session.commit()

    def tearDown(self):
        # Tear down database
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login_test_user(self):
        # Helper method to log in the test user
        return self.client.post('/login', data={
            'email': 'test@example.com',
            'password': 'testpassword'
        }, follow_redirects=True)

    # ... other helper methods ...
