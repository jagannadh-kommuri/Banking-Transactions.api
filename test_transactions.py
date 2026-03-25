import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert b'healthy' in rv.data

def test_create_transfer(client):
    rv = client.post('/api/transactions/transfer', 
                    json={
                        'amount': 1000.50,
                        'account': 'ACC123',
                        'fromAccount': 'ACC123',
                        'toAccount': 'ACC456'
                    })
    assert rv.status_code == 201
