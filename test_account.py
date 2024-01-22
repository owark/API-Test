import pytest
from faker import Faker

from client import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def generate_user():
    fake = Faker("ru_RU")
    return {
        "login": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
    }


data = [
    {
        "login": "test1",
        "email": "test@mail",
        "password": "password1"
    },
    {
        "login": "test2",
        "email": "test2@mail",
        "password": "password2"
    },
    {
        "login": "test3",
        "email": "test3@mail",
        "password": "password3"
    }
]


@pytest.mark.parametrize("data", data)
def test_post_v1_test_account(client, data):
    response = client.register_user(data)
    assert response.status_code == 200, "Статус код ответа должен быть 400"
