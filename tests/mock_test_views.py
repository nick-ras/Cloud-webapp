# tests/test_views.py
import pytest
from unittest.mock import patch
from src import create_app, db
from src.accounts.models import User

@pytest.fixture
def app():
    app = create_app('testing_config')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_admin_access_to_edit(client):
    # Arrange
    admin_email = 'admin@example.com'
    admin_password = 'adminpass'
    admin_user = User(email=admin_email, password=admin_password, is_admin=True)
    db.session.add(admin_user)
    db.session.commit()

    # Act
    # We need to mock login because we cannot login via the test client
    with patch('flask_login.utils._get_user') as mock_user:
        mock_user.return_value = admin_user

        response = client.get('/edit_page')  # Assuming '/edit_page' requires admin access

    # Assert
    assert b'Edit Form' in response.data  # Assuming 'Edit Form' is part of the HTML returned for the edit page
    assert response.status_code == 200
