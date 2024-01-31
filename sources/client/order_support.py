import allure
import requests
import json

from sources.client.constants import Constants
from sources.client.order_routes import OrderAPIRoutes


@allure.step('Формирование тела запроса')
def get_body_request_order(order_lst):
    current_data = {
        'firstName': order_lst[0],
        'lastName': order_lst[1],
        'address': order_lst[2],
        'metroStation': order_lst[3],
        'phone': order_lst[4],
        'rentTime': order_lst[5],
        'deliveryDate': order_lst[6],
        'comment': order_lst[7],
        'color': order_lst[8]
    }
    payload = json.dumps(current_data)
    return payload


@allure.step('Отмена заказа')
def cancel_order(payload):
    url = OrderAPIRoutes()
    response = requests.post(url=url.get_post_api_order_route(), data=payload)
    if 'track' in response.json():
        order_track = response.json()['track']
        payload = {
            'track': order_track
        }
        requests.put(url=f'{Constants.MAIN_URL}{Constants.ENDPOINT_ORDER_CANCEL}', data=payload)
    else:
        print('Заказ отсутствует')
