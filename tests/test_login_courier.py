import allure
import pytest
import requests

from http import HTTPStatus

from sources.client.constants import Constants
from sources.client.courier_support import (get_data_for_check_response_error,
                                            get_data_without_one_required_field,
                                            delete_courier)


@pytest.mark.get_url('login_courier')
class TestLoginCourier:

    @allure.title('Проверка возможности авторизации курьера')
    def test_login_courier_available_success(self, get_url, login_data_response):
        with allure.step("Получение ответа и проверка кода ответа"):
            assert login_data_response.status_code == HTTPStatus.OK

    @allure.title('Проверка возможности авторизации курьера при передаче всех обязательных полей')
    def test_login_courier_with_required_fields_available_success(self, get_url, login_data_response):
        with allure.step("Получение ответа и проверка кода ответа"):
            assert login_data_response.status_code == HTTPStatus.OK

    @allure.title('Проверка ошибки авторизации курьера при неправильном логине или пароле')
    @pytest.mark.parametrize('condition', ('uncorrect_login','uncorrect_password'))
    def test_login_courier_with_uncorrect_login_password_return_error_success(
            self, get_url, condition, get_login_data):
        condition = condition
        with allure.step("Формирование тела запроса"):
            payload = get_data_for_check_response_error(condition, get_login_data)
        with allure.step("Получение ответа"):
            response = requests.post(url=get_url, data=payload)
        with allure.step("Проверка текста ошибки"):
            assert response.json()['message'] == Constants.ERROR_MESSAGE_FOR_UNCORRECT_LOGIN_PASSWORD
        with allure.step('Удаление учетной записи созданного курьера'):
            delete_courier(get_login_data)

    @allure.title('Проверка ошибки авторизации курьера при отсутствии в запросе обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_courier_without_one_field_return_error_success(self, get_url, field, get_login_data):
        payload = dict.fromkeys([field, ])
        with allure.step("Формирование тела запроса"):
            payload = get_data_without_one_required_field(payload, get_login_data)
        with allure.step("Получение ответа"):
            response = requests.post(url=get_url, data=payload)
        with allure.step("Проверка текста ошибки"):
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json()['message'] == Constants.ERROR_MESSAGE_LOGIN_WITHOUT_REQUIRED_FIELD
        with allure.step('Удаление учетной записи созданного курьера'):
            delete_courier(get_login_data)

    @allure.title('Проверка авторизации курьера под несуществующим пользователем')
    def test_login_courier_with_required_fields_available_success(self, get_url, get_login_data, get_new_data):
        with allure.step("Формирование тела запроса"):
            payload = get_login_data
            payload['login'] = get_new_data['login']
        with allure.step("Получение ответа"):
            response = requests.post(url=get_url, data=payload)
        with allure.step("Проверка кода ответа"):
            assert response.status_code == HTTPStatus.NOT_FOUND
        with allure.step('Удаление учетной записи созданного курьера'):
            delete_courier(get_login_data)

    @allure.title('Проверка наличия id в ответе при успешной авторизации курьера')
    def test_login_courier_available_success(self, get_url, login_data_response):
        with allure.step("Получение ответа и проверка наличия в ответе id"):
            assert 'id' in  login_data_response.json()
