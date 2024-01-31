import allure
import pytest
import requests

from http import HTTPStatus

from sources.client.constants import Constants
from sources.client.courier_support import (get_data_for_check_status_code,
                                            get_data_without_one_required_field,
                                            delete_courier)


@pytest.mark.get_url('create_courier')
class TestCreateCourier:

    @allure.title('Проверка возможности создания курьера')
    def test_create_courier_available_success(self, get_url, new_data_response):
        with allure.step('Получение ответа и проверка кода ответа'):
            assert new_data_response.status_code == HTTPStatus.CREATED

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_create_courier_as_prev_courier_unavailable_success(self, get_url, exist_data_response):
        with allure.step('Получение ответа и проверка кода ответа'):
            assert exist_data_response.status_code == HTTPStatus.CONFLICT

    @allure.title('Проверка возможности создания курьера при передаче всех обязательных полей')
    def test_create_courier_with_required_fields_available_success(self, get_url, new_data_response):
        with allure.step('Получение ответа и проверка кода ответа'):
            assert new_data_response.status_code == HTTPStatus.CREATED

    @allure.title('Проверка кода ответа при создании курьера')
    @pytest.mark.parametrize('condition, status_code', (('valid_data', 201), ('only_login', 400), ('exist_data', 409)))
    def test_create_courier_return_with_required_status_code_success(
            self, get_url, condition, status_code, get_new_data, get_exist_data):
        condition = condition
        with allure.step('Формирование тела запроса'):
            payload = get_data_for_check_status_code(condition, get_new_data, get_exist_data)
        with allure.step('Получение ответа'):
            response = requests.post(url=get_url, data=payload)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == status_code
        with allure.step('Удаление учетных записей созданных курьеров'):
            delete_courier(get_new_data)
            delete_courier(get_exist_data)

    @allure.title('Проверка ответа успешного запроса создания курьера')
    def test_create_courier_return_ok_success(self, get_url, new_data_response):
        with allure.step('Получение ответа и проверка тела ответа'):
            assert new_data_response.json() == Constants.RESPONSE_SUCCESS

    @allure.title('Проверка ответа при отсутствии в запросе обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_required_field_unavailable_success(self, get_url, field, get_login_data):
        payload = dict.fromkeys([field,])
        with allure.step('Формирование тела запроса'):
            payload = get_data_without_one_required_field(payload, get_login_data)
        with allure.step('Получение ответа'):
            response = requests.post(url=get_url, data=payload)
        with allure.step('Проверка тела ответа'):
            assert response.json()['message'] == Constants.ERROR_MESSAGE_CREATE_WITHOUT_REQUIRED_FIELD

    @allure.title('Проверка невозможности создания курьера c существующим логином')
    def test_create_courier_with_exist_login_unavailable_success(self, get_url, get_exist_data):
        with allure.step('Формирование тела запроса'):
            payload = get_exist_data
            old_password = get_exist_data['password']
            payload['password'] = f"new{get_exist_data['password']}"
        with allure.step('Получение ответа'):
            response = requests.post(url=get_url, data=payload)
        with allure.step('Проверка тела ответа'):
            assert response.json()['message'] == Constants.ERROR_MESSAGE_FOR_EXIST_LOGIN
        with allure.step('Удаление учетной записи созданного курьера'):
            payload['password'] = old_password
            delete_courier(payload)
