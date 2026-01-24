def product_model(product: dict[str, any]) -> dict[str, any]:
    try:
        return {
            "id": product["id"],
            "title": product["title"],
            "price": product["price"],
            "category": product["category"]["name"],
            "description": product["description"],
        }
    except KeyError as e:
        raise KeyError(
            f"Campo obbligatorio mancante nei dati del prodotto: {e}"
        ) from e
    except TypeError as e:
        raise TypeError(
            f"Formato dati non valido: {e}"
        ) from e
    
def products_model(products: list[dict[str, any]]) -> list[dict[str, any]]:
    return [product_model_id_titolo(product) for product in products]

def product_model_id_titolo(product: dict[str, any]) -> dict[str, any]:
    try:
        return {
            "id": product["id"],
            "title": product["title"],
        }
    except KeyError as e:
        raise KeyError(
            f"Campo obbligatorio mancante nei dati del prodotto: {e}"
        ) from e
    except TypeError as e:
        raise TypeError(
            f"Formato dati non valido: {e}"
        ) from e