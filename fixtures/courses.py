from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FilesFixture
from fixtures.users import function_user, UserFixture
import pytest


class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture()
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)


@pytest.fixture()
def function_course(courses_client: CoursesClient, function_user: UserFixture,
                    function_file: FilesFixture) -> CourseFixture:
    request = CreateCourseRequestSchema()
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
