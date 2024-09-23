# SAS-SDET-python-interview

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
