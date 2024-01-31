import allure
import pytest
import requests

from sources.client.courier_routes import CourierAPIRoutes
from sources.client.courier_support import delete_courier
from sources.client.order_routes import OrderAPIRoutes


pytest_plugins = ['sources.fixtures.courier_fixtures']


@allure.step('Получение URL')
@pytest.fixture
def get_url(request):
    marker = request.node.get_closest_marker('get_url')
    data_marker = None if marker is None else marker.args[0]
    if data_marker == 'create_courier':
        url = CourierAPIRoutes()
        test_url = url.post_api_courier_route()
    elif data_marker == 'login_courier':
        url = CourierAPIRoutes()
        test_url = url.get_api_courier_route()
    elif data_marker in ('create_order', 'get_list_orders'):
        url = OrderAPIRoutes()
        test_url = url.get_post_api_order_route()
    else:
        return None
    return test_url


@allure.step('Отправка запроса на эндпоинт и получение ответа')
@pytest.fixture(name='new_data_response')
def get_response_with_new_data(get_url, get_new_data, request):
    payload = get_new_data
    response = requests.post(url=get_url, data=payload)
    yield response
    delete_courier(payload)


@allure.step('Отправка запроса на эндпоинт и получение ответа')
@pytest.fixture(name='exist_data_response')
def get_response_with_exist_data(get_url, get_exist_data, request):
    payload = get_exist_data
    response = requests.post(url=get_url, data=payload)
    yield response
    delete_courier(payload)


@allure.step('Отправка запроса на эндпоинт и получение ответа')
@pytest.fixture(name='login_data_response')
def get_response_with_login_data(get_url, get_login_data, request):
    payload = get_login_data
    response = requests.post(url=get_url, data=payload)
    yield response
    delete_courier(payload)
