# import pytest
# from src import create_app, db
# from src.accounts.models import User

# @pytest.fixture
# def app():
#     app = create_app('testing_config')
#     with app.app_context():
#         db.create_all()
#         yield app
#         db.session.remove()
#         db.drop_all()

# @pytest.fixture
# def client(app):
#     return app.test_client()

# def test_user_creation(app):
#     # Use app context to access the database
#     with app.app_context():
#         user = User(email='test@example.com', password='password', is_admin=False)
#         db.session.add(user)
#         db.session.commit()
        
#         assert user.email == 'test@example.com'
        # assert user.is_admin is False