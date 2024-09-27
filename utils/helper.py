def assertion_error_message_standard(response):
    return f"\n[ERROR] Test failed. \n[ERROR] Status Code: {response.status_code}\n[ERROR] Response: {response.text}"