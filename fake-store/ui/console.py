
def print_products(products: list[dict[str, any]]) -> None:
    print("*"*30)
    print("ELENCO PRODOTTI:")
    print("*"*30)
    for product in products:
        print(f"{product['id']} - {product['title']}")

def print_prodotto(product: dict[str, any]) -> None:
    print("*"*30)
    print("PRODOTTO:")
    print("*"*30)

    print(f"ID: {product['id']}")
    print(f"Titolo: {product['title']}")
    print(f"Categoria: {product['category']}")
    print(f"Prezzo: {product['price']}")
    print(f"Descrizione: {product['description']}")