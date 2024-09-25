import pytest
from api_testing.utils.api_client import APIClient

def test_get_users(api_client):
    response = api_client.get("/api/users")
    assert response.status_code == 200, f"Test failed. Response status code is {response.status_code}: {response.text}"

def test_total_users(api_client):
    response = api_client.get("/api/users")
    assert response.status_code == 200, f"Test failed. Response status code is {response.status_code}: {response.text}"

    json_response = response.json()
    assert 'total' in json_response, "Test failed. Response JSON does not contain key: 'total'."

    total_users = json_response['total']
    assert total_users > 0, f"Test failed. The total number of users is zero."