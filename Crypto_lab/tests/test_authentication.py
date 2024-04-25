# tests/test_authentication.py
import pytest
from app.auth.models import User

def test_user_creation():
    user = User(username='testuser', email='test@example.com')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
