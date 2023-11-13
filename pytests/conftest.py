# conftest.py
from flask import g
from sqlalchemy import MetaData
import config, pytest, sys
from src import create_app, db


#The setup method creates all your tables; authors and articles tables. It then defines the session, which is the Session object in SQLAlchemy in which the conversation with the database occurs
#Software test fixtures initialize test functions. They provide a fixed baseline so that tests execute reliably and produce consistent, repeatable, results. Initialization may setup services, state, or other operating environments. These are accessed by test functions through arguments; for each fixture used by a test function there is typically a parameter (named after the fixture) in the test function’s definition.

@pytest.fixture
def setup_func():#
    app = create_app("config.TestingConfig")
    app.testing = True
    with app.app_context():
        metadata = MetaData()
        print(f"metadata = {metadata}")
        db.create_all()
        session = db.session
        yield session
        
        db.session.remove()
        db.drop_all()
        