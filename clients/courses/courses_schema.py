from pydantic import BaseModel, Field, ConfigDict
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    user_id: str = Field(alias="userId")

class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка курсов.
    """
    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int = Field(default_factory=fake.min_score, alias="minScore")
    description: str = Field(default_factory=fake.sentence)
    preview_file_id: str = Field(default_factory=fake.uuid4, alias="previewFileId")
    estimated_time: str = Field(default_factory=fake.estimated_time, alias="estimatedTime")
    created_by_user_id: str = Field(default_factory=fake.uuid4, alias="createdByUserId")


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")
    description: str | None = Field(default_factory=fake.sentence)
    estimated_time: str | None = Field(default_factory=fake.estimated_time, alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса.
    """
    course: CourseSchema
