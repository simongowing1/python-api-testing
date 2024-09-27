import pytest
from utils.helper import assertion_error_message_standard
    
def test_get_specific_user_success(api_client, user_fixture):
    id = user_fixture['data']['id']
    response = api_client.get(f"/api/users/{id}")
    assert response.status_code == 200, assertion_error_message_standard(response)

    json_response = response.json()
    assert isinstance(json_response, dict), "Test failed. Response JSON is not of type: 'dictionary'."

    assert json_response == user_fixture, "Test failed. Response JSON does not match the expected user JSON"

def test_get_specific_user_failure(api_client, user_fixture):
    response = api_client.get("/api/users/foo")
    assert response.status_code == 404, assertion_error_message_standard(response)
