from register.auth import body
from configurations import AUTH_CREATE_TOKEN_URL

from models.schema_token import TokenModel

import requests
import logging

logger = logging.getLogger('auth')


class AuthCreateToken:
    def __init__(self, url: str):
        self.url = url

    def auth_create_token(self):
        response = requests.post(url=AUTH_CREATE_TOKEN_URL, json=body)
        try:
            token_data = TokenModel(**response.json())
            logger.info(token_data)
        except ValueError as e:
            logger.info(f'Value error: {e}')
        return response
