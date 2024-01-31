import allure
import pytest

from sources.client.courier_support import (get_data_for_create_courier as new_data,
                                            get_exist_data_for_create_courier as exist_data)


@allure.step('Получение новых данных для регистрации курьера')
@pytest.fixture
def get_new_data():
    payload = new_data()
    print('new_data')
    return payload


@allure.step('Получение существующих данных для регистрации курьера')
@pytest.fixture
def get_exist_data():
    payload = exist_data()
    print('exist_data')
    return payload


@allure.step('Получение данных для авторизации курьера')
@pytest.fixture
def get_login_data():
    data = exist_data()
    payload = {
        'login': data['login'],
        'password': data['password']
    }
    return payload
