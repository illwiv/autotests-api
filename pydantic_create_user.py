from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """Модель данных пользователя"""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Схема запроса на создание пользователя"""
    email: EmailStr = Field(min_length=1, max_length=250)
    password: str = Field(min_length=1, max_length=250)
    last_name: str = Field(alias="lastName", min_length=1, max_length=50)
    first_name: str = Field(alias="firstName", min_length=1, max_length=50)
    middle_name: str = Field(alias="middleName", min_length=1, max_length=50)


class CreateUserResponseSchema(BaseModel):
    """Схема ответа с данными созданного пользователя"""
    user: UserSchema
