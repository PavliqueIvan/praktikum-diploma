import configuration
import requests
import data


# создание нового заказа
def create_new_order(data):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.user_order)


response_new_order = create_new_order(data)


# получение заказа по трек-номеру
def get_track_number():
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_NUMBER,
                        params={"true": response_new_order.json()['track']})


response_track_number = get_track_number()