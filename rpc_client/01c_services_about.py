# in these examples the payload is written manually
# you could simply create some helper methods to generate the payload
# but for teaching purposes I will write it manually


import requests
from const import DB, URL, USER, PASS, UID


def main():

    payload = {
        "jsonrpc": "2.0",  # specify json-rpc version
        "method": "call",
        "params": {
            "service": "common",
            "method": "about",
            "args": (True,),
        },
        "id": 123,  # this uniquely identifies the request
    }
    response = requests.post(URL, json=payload).json()
    print(response)
    # check following file:
    # odoo/service/common.py

    # Services available:
    # rpc_dispatchers = {
    #     'common': odoo.service.common.dispatch,
    #     'db': odoo.service.db.dispatch,
    #     'object': odoo.service.model.dispatch,
    # }


if __name__ == "__main__":
    main()
