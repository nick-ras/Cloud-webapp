
from flask import Flask, jsonify, request
import pytest
from unittest.mock import patch

from learning.temp2 import main_function, create_player
import learning.temp2 as temp2
import  src.accounts as accounts
from src.accounts.forms import RegisterForm, BookBoxForm
from src.core.views import get_locations

# mock testing get _locations() and mocking get_locations_by_size
# def mock_get():
    
#     return 1
 
def test_forms(monkeypatch):
    app = Flask(__name__)
    # def mock_get(*args, **kwargs):
    #     return Mock_get_locations()
    with app.test_client() as client:
        app.testing = True
        mock_data = {'size': '2'}  # Mock form data
        with client.session_transaction() as sess:
            sess['form'] = mock_data  # Set mock form data in session
        response = client.post('/get-locations', data=mock_data)  # Perform a POST request to the route
        assert response.status_code == 200  #
    
    # monkeypatch.setattr('flask.request.form', mock_data, raising=False)

    # expected_value = jsonify([("Frederik's Church",), ('Nyhavn',), ('Strøget',), ('The Round Tower',), ('Tivoli Gardens',)])
    # assert get_locations() == expected_value


# #TESTS
# def test_main_function(monkeypatch):
# 		def mockreturn():
# 				return 100

# 		monkeypatch.setattr(temp2, 'request', mockreturn)
# 		expected_value = 100
# 		assert main_function() == expected_value
 
 
# #TESTS
# class MockResponse:
 
#     @staticmethod
#     def get_info():
#         return {"name": "test", "level" : 200}
 
# def test_create_player(monkeypatch):
 
#     def mock_get(*args, **kwargs):
#         return MockResponse() # returnthe dict with name and level
 
#     monkeypatch.setattr('learning.temp2.Player', mock_get)
 
#     expected_value = {"name": "test", "level" : 200}
#     assert create_player() == expected_value



