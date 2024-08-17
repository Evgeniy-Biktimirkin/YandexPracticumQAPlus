import configuration
import requests
import data
import blasted_order_check_test



def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=body,
                        headers=data.header_1)



def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(track)
                        )
