from pytest_voluptuous import S
from requests import Response

from schemas.reqres import single_user_schema, login_schema, \
    create_user_schema, register_unsuccessfull_schema, update_user_schema, \
    register_user_schema, unsuccessfull_login_schema


def test_get_users_users_quantity(reqres):
    """Проверяем значение id пользователей и их количество."""

    for number_user in range(1, 13):
        response: Response = reqres.get(f"/users/{number_user}")

        assert response.status_code == 200
        assert number_user == response.json()['data']['id']


def test_get_validate_schema_single_user(reqres):
    """Проверяем, что ответ приходит в правильной форме,и для single user соответствует single_user_schema."""

    response: Response = reqres.get("/users/2")

    assert response.status_code == 200
    assert S(single_user_schema) == response.json()


def test_post_login_user(reqres):
    """Проверяем, что ответ на post запрос соответствует login_schema, значение токена."""

    payload = {'email': "eve.holt@reqres.in", 'password': 'cityslicka'}

    response: Response = reqres.post("/login", data=payload)

    assert response.status_code == 200
    assert S(login_schema) == response.json()
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_post_unsuccessful_login_user(reqres):
    """Проверяем, что нельзя залогиниться без пароля."""

    payload = {'email': 'peter@klaven'}

    response: Response = reqres.post("/login", data=payload)

    assert response.status_code == 400
    assert S(unsuccessfull_login_schema) == response.json()
    assert response.json()['error'] == 'Missing password'


def test_get_single_user_not_found(reqres):
    """Проверяем get запрос для несуществующего юзера - single user not found."""

    response: Response = reqres.get("/users/23")

    assert response.status_code == 404


def test_post_create_user(reqres):
    """Проверяем, что ответ на post запрос соответствует create_user_schema, проверяем значения данных юзера."""

    payload = {'name': 'morpheus', 'job': 'leader'}

    response: Response = reqres.post("/users", data=payload)

    assert response.status_code == 201
    assert S(create_user_schema) == response.json()
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'


def test_update_user(reqres):
    """Проверяем, что ответ на post запрос соответствует create_user_schema, проверяем значения данных юзера."""

    payload = {'name': 'morpheus', 'job': 'zion resident'}

    response: Response = reqres.put("/users/2", data=payload)

    assert response.status_code == 200
    assert S(update_user_schema) == response.json()
    assert response.json()['job'] == 'zion resident'


def test_post_register_unsuccessfull(reqres):
    """Проверяем, что нельзя зарегистрироваться без пароля, проверяем ответ на соответствие register_unsuccessfull_schema."""

    payload = {'email': 'sydney@fife'}

    response: Response = reqres.post("/register", data=payload)

    assert response.status_code == 400
    assert S(register_unsuccessfull_schema) == response.json()
    assert response.json()['error'] == 'Missing password'


def test_post_register_user(reqres):
    """Проверяем, ответ на post запрос регистрации юзера, проверяем id юзера, соответствие schema."""

    payload = {'email': 'eve.holt@reqres.in', 'password': 'pistol'}

    response: Response = reqres.post("/register", data=payload)

    assert response.status_code == 200
    assert S(register_user_schema) == response.json()
    assert response.json()['id'] == 4


def test_delete_user(reqres):
    """Проверяем delete запрос."""

    response: Response = reqres.delete("/users/2")

    assert response.status_code == 204
