import pytest

from utils.api_client import APIClient

@pytest.fixture(scope='session')
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