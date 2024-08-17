import create_save_track_order

def positive_assert():
    status_response = create_save_track_order.get_order()
    assert status_response.status_code == 200


def test_get_order_by_track_gets_200_status():
    positive_assert()


# Евгений Биктимиркин, 20-я когорта — Финальный проект. Инженер по тестированию плюс
