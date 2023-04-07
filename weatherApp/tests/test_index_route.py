import sys
sys.path.append('C:/Users/andre/Documents/PyProjects/weatherApp/')
from main import app


def test_index_route():  # Test index route is returning expected HTML on GET
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'<p>City:</p>' in response.data
