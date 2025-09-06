from pydantic import BaseModel, Field, EmailStr, ConfigDict


class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: EmailStr
    password: str


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    refresh_token: str = Field(alias="refreshToken")


class TokenSchema(BaseModel):
    """
    Описание структуры запроса для получения тела токена.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """
    Описание структуры запроса для получения токена.
    """
    token: TokenSchema