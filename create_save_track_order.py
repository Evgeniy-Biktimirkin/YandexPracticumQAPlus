import configuration
import requests
import data





def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=body,
                        headers=data.header_1)



def get_order():
    response_track = post_new_order(data.order_body)
    track = response_track.json()['track']

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(track)
                        )
