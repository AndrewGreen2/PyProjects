from main import app, get_temperature
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_post(client):
    response = client.post('/', data={'usr_city': 'London'})
    assert response.status_code == 200
    assert b'The current temperature in London is' in response.data


def test_index_post_invalid_city(client):
    response = client.post('/', data={'usr_city': 'Nonexistent City'})
    assert response.status_code == 200
    assert b'The current temperature in Nonexistent City is unknown.' in response.data


def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<p>City:</p>' in response.data


def test_get_temperature():
    temperature = get_temperature('London')
    assert isinstance(temperature, float)
