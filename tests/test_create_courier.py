import allure
import pytest

from http import HTTPStatus

from sources.client.constants import Constants
from sources.client.courier_support import (register_new_courier_and_return_login_password as exist_courier_data,
                                            get_data_for_check_status_code,
                                            get_data_without_one_required_field,
                                            get_response_post_courier)


@pytest.mark.get_url('create_courier')
class TestCreateCourier:

    @allure.title('Проверка возможности создания курьера')
    def test_create_courier_available_success(self, get_url, get_new_data):
        payload = get_new_data
        response = get_response_post_courier(get_url, payload)
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == Constants.RESPONSE_SUCCESS

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_create_courier_as_prev_courier_unavailable_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        response = get_response_post_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.CONFLICT
        assert message == Constants.ERROR_MESSAGE_FOR_EXIST_LOGIN

    @allure.title('Проверка возможности создания курьера при передаче всех обязательных полей')
    def test_create_courier_with_required_fields_available_success(self, get_url, get_new_data):
        payload = get_new_data
        response = get_response_post_courier(get_url, payload)
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == Constants.RESPONSE_SUCCESS

    @allure.title('Проверка кода ответа при создании курьера')
    @pytest.mark.parametrize('condition, status_code', (('valid_data', 201), ('only_login', 400), ('exist_data', 409)))
    def test_create_courier_return_with_required_status_code_success(
            self, get_url, condition, status_code, get_new_data):
        payload = get_data_for_check_status_code(condition, get_new_data)
        response = get_response_post_courier(get_url, payload)
        assert response.status_code == status_code

    @allure.title('Проверка ответа успешного запроса создания курьера')
    def test_create_courier_return_ok_success(self, get_url, get_new_data):
        payload = get_new_data
        response = get_response_post_courier(get_url, payload)
        assert response.status_code == HTTPStatus.CREATED
        assert response.json() == Constants.RESPONSE_SUCCESS

    @allure.title('Проверка ответа при отсутствии в запросе обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_required_field_unavailable_success(self, get_url, field, get_new_data):
        payload = dict.fromkeys([field,])
        payload = get_data_without_one_required_field(payload, get_new_data)
        response = get_response_post_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert message == Constants.ERROR_MESSAGE_CREATE_WITHOUT_REQUIRED_FIELD

    @allure.title('Проверка невозможности создания курьера c существующим логином')
    def test_create_courier_with_exist_login_unavailable_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        password = get_new_data['password']
        payload['password'] = f"new{get_new_data['password']}"
        response = get_response_post_courier(get_url, payload)
        payload['password'] = password
        message = response.json()['message']
        assert response.status_code == HTTPStatus.CONFLICT
        assert message == Constants.ERROR_MESSAGE_FOR_EXIST_LOGIN
