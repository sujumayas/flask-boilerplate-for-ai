# backend/tests/unit/test_user_service.py
import pytest
from app.services.user_service import UserService

def test_create_user(app):
    service = UserService()
    user_data = {'username': 'testuser', 'email': 'test@example.com'}
    user = service.create_user(user_data)
    assert user.id is not None
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
