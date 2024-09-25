import pytest

from api_testing.utils.api_client import APIClient
    
def test_get_specific_user_success(api_client, user_fixture):
    id = user_fixture['data']['id']
    response = api_client.get(f"/api/users/{id}")
    assert response.status_code == 200, f"Test failed. Response status code is {response.status_code}: {response.text}"

    json_response = response.json()
    assert isinstance(json_response, dict), f"Response JSON is not of type: 'dictionary'."

    assert json_response == user_fixture

def test_get_specific_user_failure(api_client, user_fixture):
    response = api_client.get("/api/users/foo")
    assert response.status_code == 404, f"Test failed. Request status code is {response.status_code}: {response.text}"
