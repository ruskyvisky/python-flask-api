import pytest
from app import app 
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client 
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Merhaba, Dünya!"
