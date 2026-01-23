from requests import get, exceptions
BASE_URL: str = 'https://api.escuelajs.co/api/v1/products'
id: str ='52'

def get_data(URL: str)-> dict[str, any] | list[dict[str, any]]:
    if URL is None:
        raise ValueError("URL non può essere vuoto")
    
    try:
        response = get(URL)
        # print(res.txt)
        # print(res.json())
        response.raise_for_status()
        return response.json()
    except exceptions.HTTPError as e:
        # TODO: correggere exception
        raise exceptions.HTTPError(f"HTTP error occurred: {e}")
    
def product_model(product: dict[str, any]) -> dict[str, any]:
    return {
        "id": product["id"],
        "title": product["title"],
        "price": product["price"],
        "category": product["category"]["name"],
        "description": product["description"],
    }

    
def print_prodotto(product: dict[str, any]) -> None:
    print("*"*30)
    print("PRODOTTO:")
    print("*"*30)

    print(f"ID: {product['id']}")
    print(f"Titolo: {product['title']}")
    print(f"Categoria: {product['category']}")
    print(f"Prezzo: {product['price']}")
    print(f"Descrizione: {product['description']}")

def main():

    try:
        id = input("Inserisci l'ID del prodotto da cercare: ")
        product = product_model(get_data(f"{BASE_URL}/{id}"))
        print_prodotto(product)

    except Exception as e:
        print(f"Errore durante il recupero dei dati: {e}")


   

if __name__ == "__main__":
    main()