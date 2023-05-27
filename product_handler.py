def add_product(menu, **kwargs):
    if not menu:
        new_id = 1
    else:
        max_id = max(product.get("_id", 0) for product in menu)
        new_id = max_id + 1

    kwargs["_id"] = new_id
    menu.append(kwargs)

    return kwargs
