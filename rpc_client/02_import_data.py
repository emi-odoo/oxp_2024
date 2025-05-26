# step up our game!
# let's create some products in the DB


import requests
from const import DB, URL, PASS, UID

auction_list = [
    ["_ext_id_.auction_tv", "TV", 1],
    ["_ext_id_.auction_car", "Car", 1],
    ["_ext_id_.auction_house", "House", 1],
    ["_ext_id_.auction_boat", "Boat", 1],
]


def main():
    # lines changed -> #!!!!!
    payload = {
        "jsonrpc": "2.0",  # specify json-rpc version
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": (
                DB,
                UID,
                PASS,
                "product.template",
                "load",
                [["id", "name"], auction_list],
            ),
        },
        "id": 123,  # this uniquely identifies the request
    }
    response = requests.post(URL, json=payload).json()
    print(response)


if __name__ == "__main__":
    main()
