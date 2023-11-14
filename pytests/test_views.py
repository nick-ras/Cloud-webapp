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

def test_login_page(client):
		# Assuming you have a test client fixture
		response = client.get(url_for("accounts.login"))
		assert response.status_code == 200  # Check if the response status is OK (200)
		# Parse the HTML using BeautifulSoup
		soup = BeautifulSoup(response.data, 'html.parser')

		# Find all <h1> elements with a specific class
		h1_element = soup.find('h1')
		assert h1_element.text.startswith("Please sign in")
  
import pytest
from flask import url_for
from flask_login import current_user
from src.accounts.models import User

def test_register_success(client, session):
		# Simulate a successful registration attempt with valid form data
		response = client.post(
				url_for("accounts.register"),
				data={
						"email": "test@example.com",
						"password": "testpassword",
						"confirm": "testpassword",
				},
				follow_redirects=True,
		)					

		# Check if the user is redirected to the home page
		assert response.status_code == 200  # You can adjust this status code based on your application's behavior

		# Check if the user is logged in
		assert current_user.is_authenticated

		# Check if the success flash message is present in the response content
		assert b"You registered and are now logged in. Welcome!" in response.data