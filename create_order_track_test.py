import data
import sender_state_request


# Функция для проверки, что код ответа равен 200.
def get_order_test(body):
    track = sender_state_request.get_new_order_track(body)
    res = sender_state_request.get_order(track)
    assert res.status_code == 200


get_order_test(data.order)
