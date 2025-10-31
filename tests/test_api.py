import pytest
# app.py dosyasındaki Flask uygulamasını içe aktarıyoruz
from app import app 
@pytest.fixture
def client():
    # Flask uygulamasını test moduna al
    app.config['TESTING'] = True
    # Bir test istemcisi oluştur
    with app.test_client() as client:
        yield client # Testlere istemciyi sağla

def test_home_route(client):
    # Kök adrese GET isteği gönder
    response = client.get('/')
    
    # Yanıt durum kodunu kontrol et
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Merhaba, Dünya!"
