from sources.client.constants import Constants


class CourierAPIRoutes:

    ENDPOINT_COURIER_CREATE = '/api/v1/courier'
    ENDPOINT_COURIER_LOGIN = '/api/v1/courier/login'

    def post_api_courier_route(self):
        url = f'{Constants.MAIN_URL}{self.ENDPOINT_COURIER_CREATE}'
        return url

    def get_api_courier_route(self):
        url = f'{Constants.MAIN_URL}{self.ENDPOINT_COURIER_LOGIN}'
        return url


class OrderAPIRoutes:

    ENDPOINT_ORDERS_CREATE_GET_LIST = '/api/v1/orders'
    ENDPOINT_ORDER_CANCEL = '/api/v1/orders/cancel'

    def get_post_api_order_route(self):
        url = f'{Constants.MAIN_URL}{self.ENDPOINT_ORDERS_CREATE_GET_LIST}'
        return url
