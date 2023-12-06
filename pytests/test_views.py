import pytest
from flask import request, url_for
from bs4 import BeautifulSoup
from flask_login import current_user
from src.accounts.models import User
from pytests.conftest import test_client

# #testing homepage return status code 200, and h1 element
def test_home_page(test_client, db):

	try:
		response = request.get(url_for("core.home"))
		assert response.status_code == 200
	except Exception as e:
		raise e
	# soup = BeautifulSoup(response.data, 'html.parser')

	# h1_element = soup.find('h1')
	# assert h1_element.text.startswith("Welcome, Guest!")

# #testing login page response code and h1 element
# def test_login_page(client):
# 		response = client.get(url_for("accounts.login"))
# 		assert response.status_code == 200
  
# 		soup = BeautifulSoup(response.data, 'html.parser')

# 		h1_element = soup.find('h1')
# 		assert h1_element.text.startswith("Please sign in")

# #testing of login works including, status code, userauthentication and flash message
# def test_register_success(client, session):
# 		response = client.post(
# 				url_for("accounts.register"),
# 				data={
# 						"email": "test@example.com",
# 						"password": "testpassword",
# 						"confirm": "testpassword",
# 				},
# 				follow_redirects=True,
# 		)					

# 		assert response.status_code == 200

# 		assert current_user.is_authenticated

# 		assert b"You registered and are now logged in. Welcome!" in response.data