import pytest
from api_testing.utils.helper import assertion_error_message_standard

def test_delete_specific_user_204(api_client, user_fixture):
    id = user_fixture['data']['id']
    response = api_client.delete(f"/api/users/{id}")
    assert response.status_code == 204, assertion_error_message_standard(response)

    assert response.text == ''