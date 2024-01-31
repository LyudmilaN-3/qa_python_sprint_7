from sources.client.constants import Constants


class CourierAPIRoutes:

    def post_api_courier_route(self):
        url = f'{Constants.MAIN_URL}{Constants.ENDPOINT_COURIER_CREATE}'
        return url

    def get_api_courier_route(self):
        url = f'{Constants.MAIN_URL}{Constants.ENDPOINT_COURIER_LOGIN}'
        return url
