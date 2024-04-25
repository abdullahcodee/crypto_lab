# tests/fixtures.py
import pytest
from app import app, db
from app.models import User

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def database():
    db.create_all()
    # Additional setup code if needed
    yield db
    db.session.remove()
    db.drop_all()
