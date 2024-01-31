import allure
import pytest
import requests

from http import HTTPStatus

from sources.client.constants import Constants
from sources.client.order_support import (get_body_request_order,
                                          cancel_order)


@pytest.mark.get_url('create_order')
class TestCreateOrder:

    @allure.title('Проверка позитивного сценария заказа самоката '
                  'при разных вариантах указания цвета')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment',
        [Constants.test_data_customer]
    )
    @pytest.mark.parametrize('color', [*Constants.test_data_color])
    def test_get_order_with_diff_colors_success(
            self, get_url, firstname, lastname, address, metrostation,
            phone, renttime, deliverydate, comment, color):
        order_lst = [firstname, lastname, address, metrostation,
                     phone, renttime, deliverydate, comment, color]
        with allure.step("Формирование тела запроса"):
            payload = get_body_request_order(order_lst)
        with allure.step("Получение ответа"):
            response = requests.post(url=get_url, data=payload)
        with allure.step("Проверка кода ответа"):
            assert response.status_code == HTTPStatus.CREATED
        with allure.step('Отмена созданного заказа'):
            cancel_order(payload)

    @allure.title('Проверка ответа при успешном заказе самоката')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment',
        [Constants.test_data_customer]
    )
    def test_get_order_response_contains_track_success(
            self, get_url, firstname, lastname, address, metrostation,
            phone, renttime, deliverydate, comment):
        color = []
        order_lst = [firstname, lastname, address, metrostation,
                     phone, renttime, deliverydate, comment, color]
        with allure.step("Формирование тела запроса"):
            payload = get_body_request_order(order_lst)
        with allure.step("Получение ответа"):
            response = requests.post(url=get_url, data=payload)
        with allure.step("Проверка наличия в ответе 'track'"):
            assert 'track' in response.json()
        with allure.step('Отмена созданного заказа'):
            cancel_order(payload)

