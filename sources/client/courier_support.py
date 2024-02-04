import allure
import requests
import random
import string

from sources.client.constants import Constants
from sources.client.urls import CourierAPIRoutes


@allure.step('Формирование тела запроса')
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


@allure.step('Регистрация нового курьера и формирование тела запроса')
def register_new_courier_and_return_login_password(get_new_data):
    payload = get_new_data
    url_courier_create = f'{Constants.MAIN_URL}{CourierAPIRoutes.ENDPOINT_COURIER_CREATE}'
    response = requests.post(url=url_courier_create, data=payload)
    if response.status_code == 201:
        return payload


@allure.step('Формирование тела запроса')
def get_data_for_check_status_code(condition, get_new_data):
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
        payload = register_new_courier_and_return_login_password(get_new_data)
        payload['password'] = f"new{get_new_data['password']}"
    return payload


@allure.step('Формирование тела запроса')
def get_data_for_check_response_error(condition, current_data):
    payload = {}
    if condition == 'uncorrect_login':
        payload = {
            'login': f"new{current_data['login']}",
            'password': current_data['password']
        }
    if condition == 'uncorrect_password':
        payload = {
            'login': current_data['login'],
            'password': f"new{current_data['password']}"
        }
    return payload


@allure.step('Формирование тела запроса')
def get_data_without_one_required_field(payload, current_data):
    if 'login' in payload:
        payload['login'] = current_data['login']
    if 'password' in payload:
        payload['password'] = current_data['password']
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


@allure.step('Получение ответа на POST-запрос')
def get_response_post_courier(get_url, payload):
    response = requests.post(url=get_url, data=payload)
    return response


@allure.step('Получение ответа на GET-запрос')
def get_response_get_courier(get_url, payload):
    response = requests.post(get_url, payload)
    return response
