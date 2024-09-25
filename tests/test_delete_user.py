import pytest

from api_testing.utils.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_fixture():
    return {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
            },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
            }
            }
    
def test_delete_specific_user_204(api_client, user_fixture):
    id = user_fixture['data']['id']
    response = api_client.delete(f"/api/users/{id}")
    assert response.status_code == 204, f"Test failed. Response status code {response.status_code}: {response.text}"

    assert response.text == ''