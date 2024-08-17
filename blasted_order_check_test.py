import data
import create_save_track_order


def dono_what_for():
    response_track = create_save_track_order.post_new_order(data.order_body)
    track = response_track.json()['track']
    return track


def positive_assert():
    track = dono_what_for()
    status_response = create_save_track_order.get_order(track)
    assert status_response.status_code == 200


def test_get_order_by_track_gets_200_status():
    positive_assert()


# Евгений Биктимиркин, 20-я когорта — Финальный проект. Инженер по тестированию плюс
