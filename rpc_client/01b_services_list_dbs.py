# in these examples the payload is written manually
# you could simply create some helper methods to generate the payload
# but for teaching purposes I will write it manually


import requests
from const import URL


def main():

    payload = {
        "jsonrpc": "2.0",  # specify json-rpc version
        "method": "call",
        "params": {
            "service": "db",
            "method": "list",
            "args": (),
        },
        "id": 123,  # this uniquely identifies the request
    }
    response = requests.post(URL, json=payload).json()
    print(response)


if __name__ == "__main__":
    main()
