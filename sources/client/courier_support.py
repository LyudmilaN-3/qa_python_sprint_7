import allure
import requests
import random
import string

from sources.client.constants import Constants
from sources.client.courier_routes import CourierAPIRoutes


def get_data_for_create_courier():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    # собираем тело запроса
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }
    return payload


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []
    payload = get_data_for_create_courier()
    url_courier_create = f'{Constants.MAIN_URL}{Constants.ENDPOINT_COURIER_CREATE}'
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(url=url_courier_create, data=payload)
    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(payload['login'])
        login_pass.append(payload['password'])
        login_pass.append(payload['firstName'])
    # возвращаем список
    return login_pass


def get_exist_data_for_create_courier():
    login_pass = register_new_courier_and_return_login_password()
    payload = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }
    return payload


@allure.step('Формирование тела запроса')
def get_data_for_check_status_code(condition, get_new_data, get_exist_data):
    payload = {}
    if condition == 'valid_data':
        payload = {
            'login': get_new_data['login'],
            'password': get_new_data['password']
        }
    if condition == 'only_login':
        payload = {
            'login': get_new_data['login'],
        }
    if condition == 'exist_data':
        payload = {
            'login': get_exist_data['login'],
            'password': f"new{get_exist_data['password']}"
        }
    return payload


@allure.step('Формирование тела запроса')
def get_data_for_check_response_error(condition, get_login_data):
    payload = {}
    if condition == 'uncorrect_login':
        payload = {
            'login': f"new{get_login_data['login']}",
            'password': get_login_data['password']
        }
    if condition == 'uncorrect_password':
        payload = {
            'login': get_login_data['login'],
            'password': f"new{get_login_data['password']}"
        }
    return payload


@allure.step('Формирование тела запроса')
def get_data_without_one_required_field(payload, get_login_data):
    if 'login' in payload:
        payload['login'] = get_login_data['login']
    if 'password' in payload:
        payload['password'] = get_login_data['password']
    return payload


@allure.step('Удаление учетной записи созданного курьера')
def delete_courier(payload):
    url = CourierAPIRoutes()
    if 'firstName' in payload:
        payload.pop('firstName')
    response = requests.post(url=url.get_api_courier_route(), data=payload)
    if 'id' in response.json():
        courier_id = response.json()['id']
        requests.delete(url=f'{url.post_api_courier_route()}/{courier_id}')
    else:
        print('Учетная запись отсутствует')
