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
    
def test_get_specific_user_success(api_client, user_fixture):
    id = user_fixture['data']['id']
    response = api_client.get(f"/api/users/{id}")
    assert response.status_code == 200, f"Request failed with status code {response.status_code}: {response.text}"

    json_response = response.json()
    assert isinstance(json_response, dict), f"Response JSON is not type: 'dictionary'."

    assert json_response == user_fixture

def test_get_specific_user_failure(api_client, user_fixture):
    response = api_client.get("/api/users/foo")
    assert response.status_code == 404, f"Test failed. Request status code {response.status_code}: {response.text}"
