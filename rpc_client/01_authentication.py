# in these examples the payload is written manually
# you could simply create some helper methods to generate the payload
# but for teaching purposes I will write it manually


import requests
from const import DB, URL, USER, PASS, UID


def main():

    payload = {
        "jsonrpc": "2.0",  # specify json-rpc version
        "method": "whatever1233",  # the method is actually IGNORED by odoo
        "id": 123,  # this uniquely identifies the request
        "params": {
            "service": "common",
            "method": "login",
            "args": (DB, USER, PASS),
            # Name of the psql Database in which we created our odoo instance
            # login of the user performing the request
            # password or api key of the user performing the request
        },
    }
    # check following file:
    # odoo/service/common.py

    # Services available:
    # 'common' -> utility functions like login
    # 'db' -> database functions
    # 'object' -> CRUD operations and actions
    response = requests.post(URL, json=payload).json()
    print(response)
    assert response["result"] == [2]
    assert response["jsonrpc"]
    assert response["id"] == 123
    assert response["result"] == [UID]
    print(response)

    """
    `JSON-RPC 2 <http://www.jsonrpc.org/specification>`_ over HTTP.

        Our implementation differs from the specification on two points:

        1. The ``method`` member of the JSON-RPC request payload is
           ignored as the HTTP path is already used to route the request
           to the controller.
        2. We only support parameter structures by-name, i.e. the
           ``params`` member of the JSON-RPC request payload MUST be a
           JSON Object and not a JSON Array.

        In addition, it is possible to pass a context that replaces
        the session context via a special ``context`` argument that is
        removed prior to calling the endpoint.
    """


if __name__ == "__main__":
    main()
