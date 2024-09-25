import pytest
from api_testing.utils.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("/api/users")
    assert response.status_code == 200, f"Request failed with status code {response.status_code}: {response.text}"

def test_total_users(api_client):
    response = api_client.get("/api/users")
    total_users = response.json()['total']
    assert total_users > 0, f"Test failed. There are no users."