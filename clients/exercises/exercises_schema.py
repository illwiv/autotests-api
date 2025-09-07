from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4, alias="courseId")
    max_score: int = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int = Field(default_factory=fake.min_score, alias="minScore")
    order_index: int = Field(default_factory=fake.integer, alias="orderIndex")
    description: str = Field(default_factory=fake.sentence)
    estimated_time: str = Field(default_factory=fake.estimated_time, alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка упражнений.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнения по id.
    """
    exercise: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score, alias="maxScore")
    min_score: int | None = Field(default_factory=fake.min_score, alias="minScore")
    order_index: int | None = Field(default_factory=fake.integer, alias="orderIndex")
    description: str | None = Field(default_factory=fake.sentence)
    estimated_time: str | None = Field(default_factory=fake.estimated_time, alias="estimatedTime")
