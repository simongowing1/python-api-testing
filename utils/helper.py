def assertion_error_message_standard(response):
    return f"Test failed. Response status code is {response.status_code}: {response.text}"