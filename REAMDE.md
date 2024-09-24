# Flask Boilerplate for backend applications

Scalable and comprehensive boilerplate incorporating best practices for Test-Driven Development (TTD), API-first design, Service-Repository architecture, centralized logging, and seamless integration with a Single Page Application (SPA) frontend.

## File Structure: 

```md
my_flask_app/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── services/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── endpoints/
│   │   └── utils/
│   ├── tests/
│   │   ├── unit/
│   │   └── integration/
│   ├── requirements.txt
│   └── wsgi.py
├── spa/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── App.vue
│   ├── package.json
│   └── webpack.config.js
├── logs/
├── .gitignore
├── docker-compose.yml
└── README.md
```

###  Key Components:

- **backend/:** Contains the Flask application.
- **app/:** Core Flask app with configurations, models, repositories, services, API endpoints, and utilities.
- **tests/:** Organized into unit and integration tests.
- **spa/:** Frontend SPA (e.g., built with Vue.js, React, or Angular).
- **logs/:** Centralized logging files.
- **docker-compose.yml:** For containerization and orchestration (optional but recommended).
- **README.md:** Project documentation.


## Writing Tests First
For each new functionality, start by writing tests.

## Example User Tests:

```bash
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
```

```bash
# backend/tests/integration/test_user_api.py
def test_get_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_user(client):
    user_data = {'username': 'testuser', 'email': 'test@example.com'}
    response = client.post('/api/users', json=user_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['username'] == 'testuser'
    assert data['email'] == 'test@example.com'
```

Then, add a script to your package.json or Makefile for running tests.

```bash
# Run pytest
pytest
```





