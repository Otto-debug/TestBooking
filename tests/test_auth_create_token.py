import allure

from register.auth_create_token import AuthCreateToken

from configurations import AUTH_CREATE_TOKEN_URL

@allure.title("Test Authentication")
@allure.description("This test makes a check to see if the correct token has been received")
class TestAuthCreateToken:
    def test_auth(self):
        response = AuthCreateToken(url=AUTH_CREATE_TOKEN_URL).auth_create_token()
        assert response.status_code == 200

        