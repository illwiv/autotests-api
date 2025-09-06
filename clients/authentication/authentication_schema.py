from pydantic import BaseModel, Field, EmailStr


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
    refresh_token: str = Field(alias="refreshToken")


class TokenSchema(BaseModel):
    """
    Описание структуры запроса для получения тела токена.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """
    Описание структуры запроса для получения токена.
    """
    token: TokenSchema