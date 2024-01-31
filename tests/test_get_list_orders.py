import allure
import pytest
import requests


@pytest.mark.get_url('get_list_orders')
class TestGetListOrders:

    @allure.title('Проверка получения списка заказов в ответе')
    def test_get_list_orders_return_order_list_success(self, get_url):
        with allure.step("Получение ответа"):
            response = requests.get(url=get_url)
        with allure.step("Получение первого элемента в теле ответа"):
            first_key = list(response.json().keys())[0]
        with allure.step("Проверка наименования и значения первого элемента в теле ответа"):
            assert first_key == 'orders' and isinstance(response.json()[first_key], list)
