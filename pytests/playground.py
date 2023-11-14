
import os
from flask import Flask, jsonify, request, url_for
import pytest
from unittest.mock import patch
from learning import main_function
import learning.temp2 as temp2
import src.accounts as accounts
from src import create_app, db, Boxes, get_locations
from .conftest import setup_func

def test_main_function(monkeypatch):
		def mockreturn():
				return 100

		monkeypatch.setattr(temp2, 'request', mockreturn)
		expected_value = 100
		assert main_function() == expected_value

def test_random(setup_func):
    print(f"setup_func = {setup_func}")
    print(f"database model = {Boxes}")
    assert 1 == 1

# def test_get_locations_by_size():
#     # Create a test database session
#         # Add some test data to the Boxes table
#     box1 = Boxes(location='Location1', size='Small', in_use=False)
#     box2 = Boxes(location='Location2', size='Small', in_use=False)
#     box3 = Boxes(location='Location3', size='Large', in_use=False)
#     db.session.add(box1)
#     app.commit()

#     # Call the method you want to test
#     result = Boxes.get_locations_by_size('Small')

#     # Assertions
#     assert len(result) == 1  # Only one unique location with 'Small' size and in_use=False
#     assert result[0].location == 'Location1'

#     # Clean up (optional)
#     db.session.delete(box1)
#     app.commit()