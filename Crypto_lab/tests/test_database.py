# tests/test_database.py
import pytest
from app import db

def test_database_connection():
    assert db.session is not None
