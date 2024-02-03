import allure
import pytest

from http import HTTPStatus

from sources.client.constants import Constants
from sources.client.order_support import get_body_request_order, get_response_post_order


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
            phone, renttime, deliverydate, comment, color, cansel_fix):
        order_lst = [firstname, lastname, address, metrostation,
                     phone, renttime, deliverydate, comment, color]
        payload = get_body_request_order(order_lst)
        response = get_response_post_order(get_url, payload)
        assert response.status_code == HTTPStatus.CREATED

    @allure.title('Проверка ответа при успешном заказе самоката')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment',
        [Constants.test_data_customer]
    )
    def test_get_order_response_contains_track_success(
            self, get_url, firstname, lastname, address, metrostation,
            phone, renttime, deliverydate, comment, cansel_fix):
        color = []
        order_lst = [firstname, lastname, address, metrostation,
                     phone, renttime, deliverydate, comment, color]
        payload = get_body_request_order(order_lst)
        response = get_response_post_order(get_url, payload)
        assert 'track' in response.json()
