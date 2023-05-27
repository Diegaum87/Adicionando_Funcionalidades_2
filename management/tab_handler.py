def calculate_tab(consumptions):
    subtotal = 0.0
    for consumption in consumptions:
        product_id = consumption["_id"]
        amount = consumption["amount"]

        product_prices = {
            1: 10.99,
            2: 19.99
        }

        if product_id in product_prices:
            product_price = product_prices[product_id]
            subtotal += product_price * amount

    formatted_subtotal = "${:.2f}".format(subtotal)
    return {"subtotal": formatted_subtotal}
