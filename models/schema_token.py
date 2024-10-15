from pydantic import BaseModel, constr, field_validator


class TokenModel(BaseModel):
    token: constr(min_length=1, max_length=100)  # Ограничение длины токена

    @field_validator('token')
    def check_to_int_token(cls, v): # Проверка токена на целочисленное значение
        if isinstance(v, int):
            raise ValueError('The token does not have to be an integer')
        return v

    # class Config:
    #     # Дополнительные настройки валидации
    #     min_anystr_length = 1
    #     anystr_strip_whitespace = True  # Убираем пробелы в начале и в конце строки

