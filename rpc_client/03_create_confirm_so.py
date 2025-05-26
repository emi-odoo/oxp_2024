# step up our game!
# let's create some products in the DB


import requests
from const import DB, URL, PASS, UID


def _rpc_call(model, method, *args, **kwargs):
    payload = {
        "jsonrpc": "2.0",  # specify json-rpc version
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [
                DB,
                UID,
                PASS,
                model,
                method,
            ],
        },
    }
    if args:
        payload["params"]["args"].append(args)
    if kwargs:
        payload["params"]["args"].append(kwargs)
    return requests.post(URL, json=payload).json()["result"]


def main():
    # 1. get name of the lot being sold
    product_name = input("Enter name of product that has been sold: ")

    # 2. find if the product exists in Odoo
    product = _rpc_call("product.product", "search_read", [["name", "=", product_name]], ["id", "name"])
    if not product:
        # 2b. fail
        raise NotImplementedError(f"Product {product_name} doesn't exist in Odoo yet")
    product_id = product[0]["id"]

    # 3. Get price from user input
    price = float(input("Enter price of the product: "))

    # 4. Get name from user input
    partner_name = input("Enter name of the customer: ")

    # 5. Perform RPC call to find the ID of the partner
    partner = _rpc_call("res.partner", "search_read", [["name", "=", partner_name]], ["id", "name"])
    if not partner:
        # 5b. Create it if not found
        partner = _rpc_call("res.partner", "create", {"name": partner_name})
    else:
        partner = partner[0]['id']

    # 6. Create Sale Order
    so = _rpc_call(
        "sale.order",
        "create",
        {
            "partner_id": partner,
            "order_line": [
                (0, 0, {"product_id": product_id, "product_uom_qty": 1, "price_unit": price}),
            ],
        },
        context={"default_payment_term_id": 1},
    )
    print(f'SO {so} created')

    # 7. Confirm Sale Order
    if input("Confirm sale order? (y/n): ") == "y":
        _rpc_call("sale.order", "action_confirm", [so])
    else:
        return

    # 8. Create an invoice
    if input("Create invoice? (y/n): ") == "y":
        wiz = _rpc_call("sale.advance.payment.inv", "create", {"advance_payment_method": "delivered", "sale_order_ids": [(4, so)]})
        _rpc_call("sale.advance.payment.inv", "create_invoices", [wiz])
    else:
        return


if __name__ == "__main__":
    main()
