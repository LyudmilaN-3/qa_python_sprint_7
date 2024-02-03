import pytest

from sources.client.urls import CourierAPIRoutes, OrderAPIRoutes


pytest_plugins = ['sources.fixtures.courier_fixtures', 'sources.fixtures.order_fixtures']


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
