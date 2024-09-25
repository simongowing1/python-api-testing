import pytest

from api_testing.utils.api_client import APIClient

def test_delete_specific_user_204(api_client, user_fixture):
    id = user_fixture['data']['id']
    response = api_client.delete(f"/api/users/{id}")
    assert response.status_code == 204, f"Test failed. Response status code is {response.status_code}: {response.text}"

    assert response.text == ''