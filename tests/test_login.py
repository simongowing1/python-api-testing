import pytest
from api_testing.utils.helper import assertion_error_message_standard

# correct login details from https://reqres.in/
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
    assert response.status_code == 200, assertion_error_message_standard(response)

def test_login_failure_incorrect_details(api_client, incorrect_login_details):
    response = api_client.post("/api/login", incorrect_login_details)
    assert response.status_code == 400, assertion_error_message_standard(response)

def test_login_failure_password_null(api_client, correct_login_details):
    response = api_client.post("/api/login", {"email": correct_login_details["email"]})
    assert response.status_code == 400, assertion_error_message_standard(response)

def test_login_failure_email_null(api_client, correct_login_details):
    response = api_client.post("/api/login", {"password": correct_login_details["password"]})
    assert response.status_code == 400, assertion_error_message_standard(response)

def test_login_failure_email_empty_string(api_client, correct_login_details):
    response = api_client.post("/api/login", {"email": "", "password": correct_login_details["password"]})
    assert response.status_code == 400, assertion_error_message_standard(response)

def test_login_failure_password_empty_string(api_client, correct_login_details):
    response = api_client.post("/api/login", {"email": correct_login_details["email"], "password": ""})
    assert response.status_code == 400, assertion_error_message_standard(response)

def test_login_failure_email_and_password_empty_strings(api_client):
    response = api_client.post("/api/login", {"email": "", "password": ""})
    assert response.status_code == 400, assertion_error_message_standard(response)

def test_login_failure_empty_body(api_client):
    response = api_client.post("/api/login", {})
    assert response.status_code == 400, assertion_error_message_standard(response)

def test_login_failure_invalid_email(api_client, correct_login_details):
    response = api_client.post("/api/login", {"email": "emailaddress", "password": correct_login_details['password']})
    assert response.status_code == 400, assertion_error_message_standard(response)

# DOES NOT FAIL - INJECTION ATTACK PASSES AND TOKEN IS ISSUED
def test_login_failure_injection_attack(api_client, correct_login_details):
    response = api_client.post("/api/login", {"email": correct_login_details["email"], "password": "' OR '1'='1"})
    assert response.status_code == 400, assertion_error_message_standard(response)