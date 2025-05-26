# step up our game!
# let's create some products in the DB


import requests
from const import DB, URL, PASS, UID

auction_list_italian = [
    ["_ext_id_.auction_tv", "TV"],
    ["_ext_id_.auction_car", "Auto"],
    ["_ext_id_.auction_house", "Casa"],
    ["_ext_id_.auction_boat", "Barca"],
]


def main():
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
                [["id", "name"], auction_list_italian],
                {
                    "context": {"lang": "it_IT"},       #!!!!!
                },
            ),
        },
        "id": 123,  # this uniquely identifies the request
    }
    response = requests.post(URL, json=payload).json()
    print(response)


if __name__ == "__main__":
    main()
