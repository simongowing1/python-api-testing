import pytest
from api_testing.utils.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def correct_login_details():
    return {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
        }

@pytest.fixture
def incorrect_login_details():
    return {
        "email": "name@email.com",
        "password": "password"
        }

def test_login_success_correct_details(api_client, correct_login_details):
    response = api_client.post("/api/login", correct_login_details)
    assert response.status_code == 200, f"Failed with status code {response.status_code}: {response.text}"

def test_login_success_incorrect_details(api_client, incorrect_login_details):
    response = api_client.post("/api/login", incorrect_login_details)
    assert response.status_code == 400, f"Failed with status code {response.status_code}: {response.text}"

def test_login_failure_no_password(api_client, correct_login_details):
    response = api_client.post("/api/login", {"email": correct_login_details["email"]})
    assert response.status_code == 400, f"Failed with status code {response.status_code}: {response.text}"

def test_login_failure_no_email(api_client, correct_login_details):
    response = api_client.post("/api/login", {"password": correct_login_details["password"]})
    assert response.status_code == 400, f"Failed with status code {response.status_code}: {response.text}"

