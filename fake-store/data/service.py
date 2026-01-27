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

def products_model(products_list: list[dict[str, any]]) -> list[dict[str, any]]:
    """Restituisce una lista di prodotti con solo id e titolo."""
    # return [product_model_id_titolo(product) for product in products]  
    return [{"id": str(product["id"]), "title": product["title"]} for product in products_list]

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
    
   