from main import app, get_temperature
import pytest


@pytest.fixture
def client():  # Setup test client for unit tests
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_post(client):
    '''
    Tests a POST request with a valid city name
    returns a response with status code 200 and msg containing
    the city name and temperature.
    '''
    response = client.post('/', data={'usr_city': 'London'})
    assert response.status_code == 200
    assert b'The current temperature in London is' in response.data


def test_index_post_invalid_city(client):
    '''
    Tests that a POST request to the app with an invalid city name
    returns a response with status code 200 and a message
    that the temperature is unknown.
    '''
    response = client.post('/', data={'usr_city': 'Fake City'})
    assert response.status_code == 200
    assert b'The current temperature in Fake City is unknown.' in response.data


def test_index_get(client):
    '''
    Tests that a GET request returns a response with status
    code 200 and the expected HTML content.
    '''
    response = client.get('/')
    assert response.status_code == 200
    assert b'<p>City:</p>' in response.data


def test_get_temperature():
    '''
    Tests the get_temperature function directly to ensure 
    that it returns a floating-point temperature value.
    '''
    temperature = get_temperature('London')
    assert isinstance(temperature, float)
