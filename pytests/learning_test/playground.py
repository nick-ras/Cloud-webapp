
import os
from flask import Flask, jsonify, request, url_for
import pytest
from unittest.mock import patch
from temp2 import main_function
import temp2 as temp2
import src.accounts as accounts
from src import create_app, db
from src.accounts.models import Boxes
from src.core.views import get_locations

def test_main_function(monkeypatch):
		def mockreturn():
				return 100

		monkeypatch.setattr(temp2, 'request', mockreturn)
		expected_value = 100
		assert main_function() == expected_value

def test_random():
    print(f"database model = {Boxes}")
    assert 1 == 1