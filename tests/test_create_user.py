import pytest
from utils.helper import assertion_error_message_standard

@pytest.fixture
def dummy_user_details():
    return {
    "name": "morpheus",
    "job": "leader"
}

def test_create_user_success(api_client, dummy_user_details):
    response = api_client.post("/api/users", dummy_user_details)
    assert response.status_code == 201, assertion_error_message_standard(response)

    json_response = response.json()
    assert 'name' in json_response, "Test failed. Response JSON does not contain key: 'name'."
    assert json_response['name'] == dummy_user_details['name'], f"Test failed. Response does not match expected value for 'name'"

    assert 'job' in json_response, "Test failed. Response JSON does not contain key: 'job'."
    assert json_response['job'] == dummy_user_details['job'], f"Test failed. Response does not match expected value for 'job'"
   
    print("response:", json_response)

# FAILS - CREATES USER WITH JUST "ID" AND "CREATEDATE"
def test_create_user_failure_empty_body(api_client):
    response = api_client.post("/api/users", {})
    assert response.status_code == 400, assertion_error_message_standard(response)
    print("response:", response.json())