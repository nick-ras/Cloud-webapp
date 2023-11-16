from temp2 import main_function, create_player
import temp2


def test_main_function(monkeypatch):

		def mockreturn():
				return 100

		monkeypatch.setattr(temp2, 'request', mockreturn)
		expected_value = 100
		assert main_function() == expected_value


 
class MockResponse:
 
    @staticmethod
    def get_info():
        return {"name": "test", "level" : 200}
 
def test_create_player(monkeypatch):
 
    def mock_get(*args, **kwargs):
        return MockResponse() # returnthe dict with name and level
 
    monkeypatch.setattr('temp2.Player', mock_get)
 
    expected_value = {"name": "test", "level" : 200}
    assert create_player() == expected_value