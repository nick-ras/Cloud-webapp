from flask import url_for
from bs4 import BeautifulSoup

def test_home_page(client):
		# Assuming you have a test client fixture
		response = client.get(url_for("core.home"))
		assert response.status_code == 200  # Check if the response status is OK (200)
		# Parse the HTML using BeautifulSoup
		soup = BeautifulSoup(response.data, 'html.parser')

		# Find all <h1> elements with a specific class
		h1_element = soup.find('h1')
		assert h1_element.text.startswith("Welcome, Guest!")