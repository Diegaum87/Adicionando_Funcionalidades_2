from product_handler import add_product
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    menu = []

    produto1 = {"nome": "Produto 1", "preco": 10.99}
    produto2 = {"nome": "Produto 2", "preco": 19.99}

    produto_adicionado1 = add_product(menu, **produto1)
    produto_adicionado2 = add_product(menu, **produto2)

    print("Produto adicionado 1:")
    print(produto_adicionado1)
    print("Produto adicionado 2:")
    print(produto_adicionado2)

    consumptions = [
        {"_id": produto_adicionado1["_id"], "amount": 5},
        {"_id": produto_adicionado2["_id"], "amount": 3}
    ]

    subtotal = calculate_tab(consumptions)
    print("Subtotal:")
    print(subtotal)
