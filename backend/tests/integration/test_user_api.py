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
