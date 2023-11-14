from flask import url_for

def test_home_page(client):
    # Assuming you have a test client fixture
    response = client.get(url_for("core.home"))
    assert response.status_code == 200  # Check if the response status is OK (200)
    assert b"Welcome to the Home Page" in response.data  # Check for content in the response