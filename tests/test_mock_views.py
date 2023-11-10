
from flask import Flask, jsonify, request
import pytest
from unittest.mock import patch

from learning.temp2 import main_function, create_player
import learning.temp2 as temp2
import  src.accounts as accounts
from src.accounts.forms import RegisterForm, BookBoxForm
from src.core.views import get_locations
from src import create_app

# mock testing get _locations() and mocking get_locations_by_size
# def mock_get():
    
#     return 1
 
def test_forms(monkeypatch):
    app = create_app()
    # def mock_get(*args, **kwargs):
    #     return Mock_get_locations()
    with app.test_client() as client:
        app.testing = True
        mock_data = {'sizes': '2'} # Mock form data
        response = client.post('/get-locations', data=mock_data)  # Perform a POST request to the route
        assert response.status_code == 200  #

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



