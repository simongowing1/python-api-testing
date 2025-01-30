# Python-api-testing

## Simon Gowing's Solution:

- **Language**: [Python3](https://www.python.org/doc/)
- **Tests**: [Pytest](https://docs.pytest.org/)
- **Automation**: [GitHub Actions](https://docs.github.com/en/actions)


## File Structure

| File(s)                                 | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `/.github/workflows`                    | Contains GitHub Action workflow yml script/s                                          |
| `/tests/test_*`                         | Contains all files containing tests (prefixed 'test_')                                |
| `/tests/fixtures.py`                    | Contains all fixtures for tests                                                       |
| `/tests/conftest.py`                    | Exports fixtures - must be updated when new fixture is added to `/fixtures`           |
| `/utils/api_client.py`                  | Contains APIClient class and all api request methods                                  |
| `/utils/helper.py`                      | Contains helper functions such as `assertion_error_message_standard`                  |
| `/requirements.txt`                     | Contains all python package requirements                                              |


## Configuration

Create virtual environment (venv):

```bash
python3 -m venv venv
```

Activate venv:

```bash
source venv/bin/activate
```

Install all necessary packages according to `requirements.txt`:

```bash
pip install -r requirements.txt
```

Run tests from the command line:

```bash
pytest --no-header -v -s
```


## Tests

1. Attempt to login via a POST request to `https://reqres.in/api/login`:

| Test                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `test_login_success_correct_details`    | Verify a `200` response when the `correct data` is provided to the API                |
| `test_login_failure_incorrect_details`  | Verify a `400` response when the `incorrect data` is provided to the API              |
| `test_login_failure_password_null`      | Verify a `400` response when incomplete data is provided: `password is null`          |
| `test_login_failure_email_null`         | Verify a `400` response when incomplete data is provided: `email is null`             |
| `test_login_failure_email_empty_string` | Verify a `400` response when incomplete data is provided: `email is empty string`     |
| `test_login_failure_password_empty_string`| Verify a `400` response when incomplete data is provided: `password is empty string`|
| `test_login_failure_email_and_password_empty_strings`| Verify a `400` response when incomplete data is provided: `email and password are empty strings`|
| `test_login_failure_request_body_empty`| Verify a `400` response when incomplete data is provided: `request body is empty`|
| `test_login_failure_invalid_email`| Verify a `400` response when incomplete data is provided: `email is invalid format`|
| `test_login_failure_injection_attack`| Verify a `400` response when SQL injection attach is attempted|


2. GET a list of users from the `https://reqres.in/api/users` endpoint:

| Test                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `test_get_users`    | Verify a `200` response when `/api/users` is requested from API                |
| `test_total_users`  | Verify that number of users is greater than zero and print number of users             |


3. GET information on a specific user

| Test                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `test_get_specific_user_success`    | Verify a `200` response and `correctly structured JSON` is data returned for a specific, valid user                |
| `test_get_specific_user_failure`  | Verify a `404` response when an `invalid user` is requested             |


4. POST to `https://reqres.in/api/users` to create a new user:

| Test                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `test_create_user_success`    | Verify a `201` response is given with the `expected JSON attributes`                |
| `test_create_user_failure_empty_body`  | Verify that number of users is greater than zero and print number of users             |


5. DELETE a user

| Test                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `test_delete_specific_user_204`    | Verify a `204` response with `no body`                |


## Notes:

**Recommendations:**

The following tests are defying their assertions and failing, requiring improvements in the API.

| Test                                    | Description                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `test_login_failure_injection_attack`    | Allows an SQL injection attack to happen, granting `200` response and issuing an access token                 |
| `test_create_user_failure_empty_body`    | Allows a user to be created with no content: `{"id":"193","createdAt":"2024-09-27T11:29:17.667Z"}`                |


# Scenario:

Your company's development team has created some new APIs that need to be tested. Your manager wants these tests automated so they can be executed daily. You can also do manual testing of these APIs if you would like. Your automated test script should report on the pass/fail status of each test.

The development team has sent you the documentation listed on https://reqres.in/ and asked you to test the following:

1. Attempt to login via a POST request to https://reqres.in/api/login
   - Verify a 200 response when the correct data is provided to the API
   - Verify a 400 response when incomplete data is provided, for example: password is left blank
2. GET a list of users from the https://reqres.in/api/users endpoint
   - Verify a 200 response and the report on the number of users returned with the expectation that the number is greater than zero.
3. GET information on a specific user
   - Verify a 200 response and correctly structured JSON is data returned for a specific, valid user. (Item 2 above will give you a collection of valid users)
   - Verify a 404 response when an invalid user is requested
4. POST to https://reqres.in/api/users to create a new user
   - Verify a 201 response is given with the expected JSON attributes
5. DELETE a user
   - Verify a 204 response with no body

# Pre-requisites

This technical assessment requires a GitHub account. Since you will need to push code to your repository, you will either need to upload your SSH key to GitHub or configure a personal access token. To upload an SSH key, go to GitHub -> Settings -> SSH and GPG keys. If you prefer to use a personal access token, you can create one by going to GitHub -> Settings -> Developer settings -> Personal access tokens.

Remember to keep your SSH key and/or personal access token private. Please do not share this key/token with your interviewers.

You can complete this assessment using the IDE of your choice **except for Jupyter/IPython Notebook**. We recommend VS Code, but you can choose to use a different one. You must use Python 3 but you can use any version of Python 3. You can use any Python library you wish.

As you work on this assessment, consider the possible **edge cases** and how to best handle them. You must commit and push your final code to this git repository by the end of the technical assessment. The technical assessment ends when the interview begins. During the interview, you will present your code to a panel of testers and/or developers. Be prepared to discuss any additional testing you would perform if you were testing a real API.

# Resources:

Feel free to use any resource you wish as you complete this assessment. As in the real world, you can search Google, Stack Overflow, etc.
