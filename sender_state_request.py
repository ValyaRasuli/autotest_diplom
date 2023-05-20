import configuration
import requests
import data


# Эта функция выполняет запрос на создание заказа
def post_new_order():
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREAT_NEW_ORDER,
        json=data.order,
        headers=data.headers,
    )

# Эта функция сохраняет номер трекер заказа
def get_new_order_track():
    res = post_new_order()
    return res.json()["track"]


# Эта функция выполняет запрос на получения заказа по треку заказа
def get_order(track):
    r = requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER + str(track),
        headers={"Content-Type": "application/json"}
    )

    return r


