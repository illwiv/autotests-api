import pytest


@pytest.fixture(scope='class', autouse=True)
def send_analytics_data():
    print("autouse")


@pytest.fixture(scope='session')
def settings():
    print("session")


@pytest.fixture(scope='class')
def user():
    print("class")


@pytest.fixture()
def user_client(settings):
    print("function")


class TestUserFlow:
    def test_user_can_login(self, settings, user, user_client):
        pass

    def test_user_can_create_course(self, settings, user, user_client):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, user_client):
        pass


@pytest.fixture()
def user_data():
    print("Создаем П для теста")
    yield {"username": "test_user", "email": "exmaple@mail.ru"}
    print("Удаляем П после теста")


def test_user_email(user_data):
    print(user_data)
    assert user_data["email"] == "exmaple@mail.ru"


def test_user_name(user_data):
    print(user_data)
    assert user_data["username"] == "test_user"
