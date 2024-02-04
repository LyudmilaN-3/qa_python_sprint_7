import allure
import pytest

from http import HTTPStatus

from sources.client.constants import Constants
from sources.client.courier_support import (get_data_for_check_response_error,
                                            get_data_without_one_required_field,
                                            register_new_courier_and_return_login_password as exist_courier_data,
                                            get_response_get_courier)


@pytest.mark.get_url('login_courier')
class TestLoginCourier:

    @allure.title('Проверка возможности авторизации курьера')
    def test_login_courier_available_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        response = get_response_get_courier(get_url, payload)
        assert response.status_code == HTTPStatus.OK
        assert 'id' in response.json()

    @allure.title('Проверка возможности авторизации курьера при передаче всех обязательных полей')
    def test_login_courier_with_required_fields_available_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        response = get_response_get_courier(get_url, payload)
        assert response.status_code == HTTPStatus.OK
        assert 'id' in response.json()

    @allure.title('Проверка ошибки авторизации курьера при неправильном логине или пароле')
    @pytest.mark.parametrize('condition', ('uncorrect_login', 'uncorrect_password'))
    def test_login_courier_with_uncorrect_login_password_return_error_success(
            self, get_url, condition, get_new_data):
        current_data = exist_courier_data(get_new_data)
        payload = get_data_for_check_response_error(condition, current_data)
        response = get_response_get_courier(get_url, payload)
        assert response.json()['message'] == Constants.ERROR_MESSAGE_FOR_UNCORRECT_LOGIN_PASSWORD

    @allure.title('Проверка ошибки авторизации курьера при отсутствии в запросе обязательного поля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_courier_without_one_field_return_error_success(self, get_url, field, get_new_data):
        current_data = exist_courier_data(get_new_data)
        payload = dict.fromkeys([field, ])
        payload = get_data_without_one_required_field(payload, current_data)
        response = get_response_get_courier(get_url, payload)
        message = response.json()['message']
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert message == Constants.ERROR_MESSAGE_LOGIN_WITHOUT_REQUIRED_FIELD

    @allure.title('Проверка авторизации курьера под несуществующим пользователем')
    def test_login_courier_with_required_fields_available_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        password = get_new_data['login']
        payload['login'] = f"new{get_new_data['login']}"
        response = get_response_get_courier(get_url, payload)
        payload['login'] = password
        message = response.json()['message']
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert message == Constants.ERROR_MESSAGE_FOR_UNCORRECT_LOGIN_PASSWORD

    @allure.title('Проверка наличия id в ответе при успешной авторизации курьера')
    def test_login_courier_id_in_response_success(self, get_url, get_new_data):
        payload = exist_courier_data(get_new_data)
        response = get_response_get_courier(get_url, payload)
        assert response.status_code == HTTPStatus.OK
        assert 'id' in response.json()
