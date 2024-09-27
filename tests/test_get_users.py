import pytest
from api_testing.utils.helper import assertion_error_message_standard

def test_get_users(api_client):
    response = api_client.get("/api/users")
    assert response.status_code == 200, assertion_error_message_standard(response)

def test_total_users(api_client):
    response = api_client.get("/api/users")
    assert response.status_code == 200, assertion_error_message_standard(response)

    json_response = response.json()
    assert 'total' in json_response, "Test failed. Response JSON does not contain key: 'total'."

    total_users = json_response['total']
    assert total_users > 0, f"Test failed. The total number of users is zero."