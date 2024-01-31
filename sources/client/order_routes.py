from sources.client.constants import Constants


class OrderAPIRoutes:

    def get_post_api_order_route(self):
        url = f'{Constants.MAIN_URL}{Constants.ENDPOINT_ORDERS_CREATE_GET_LIST}'
        return url
