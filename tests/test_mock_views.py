
import pytest
from unittest.mock import patch

from learning.temp2 import main_function, create_player
import learning.temp2 as temp2
import  src.accounts as accounts
from src.accounts.forms import RegisterForm, BookBoxForm

# #TRY MYSELF------------------------
def mock_get():
    
    return "mock from book box form not needed"
 
def test_forms(monkeypatch):
 
    # def mock_get(*args, **kwargs):
    #     return Mock_get_locations()
 
    monkeypatch.setattr(RegisterForm, "test", mock_get, raising=True)
 
    expected_value = "mock from book box form not needed"
    assert RegisterForm.test() == expected_value


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



