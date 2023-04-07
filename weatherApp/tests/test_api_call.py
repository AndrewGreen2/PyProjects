import sys
sys.path.append('C:/Users/andre/Documents/PyProjects/weatherApp/')
from main import app

# Test index route is returning expected HTML on GET request
def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'<p>City:</p>' in response.data