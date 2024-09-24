# backend/tests/conftest.py
import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    app = create_app('app.config.Config')
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    })
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
