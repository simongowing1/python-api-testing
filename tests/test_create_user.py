import pytest
from api_testing.utils.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def dummy_user_details():
    return {
    "name": "morpheus",
    "job": "leader"
}

def test_create_user_success(api_client, dummy_user_details):
    response = api_client.post("/api/users", dummy_user_details)
    assert response.status_code == 201, f"Request failed with status code {response.status_code}: {response.text}"
    print("response:", response.json())

# FAILS - CREATES USER WITH JUST "ID" AND "CREATEDATE"
def test_create_user_failure_empty_body(api_client):
    response = api_client.post("/api/users", {})
    assert response.status_code == 400, f"Request failed with status code {response.status_code}: {response.text}"
    print("response:", response.json())