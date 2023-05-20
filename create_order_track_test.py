import data
import sender_state_request

# Функция для проверки, что код ответа равен 200.
def get_order_test():
    track = sender_state_request.get_new_order_track()
    res = sender_state_request.get_order(track)
    print(res.status_code)
    assert res.status_code == 200

get_order_test()





