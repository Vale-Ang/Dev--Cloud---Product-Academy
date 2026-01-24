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
    except exceptions.ConnectionError as e:
        raise exceptions.ConnectionError(
            f"Errore di connessione. Verifica la tua connessione internet: {e}"
        ) from e
    except exceptions.Timeout as e:
        raise exceptions.Timeout(
            f"Timeout della richiesta. Il server non ha risposto in tempo: {e}"
        ) from e
    except exceptions.RequestException as e:
        raise exceptions.RequestException(f"Errore generico nella richiesta: {e}"
        ) from e
    
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
    
def print_products(products: list[dict[str, any]]) -> None:
    print("*"*30)
    print("ELENCO PRODOTTI:")
    print("*"*30)
    for product in products:
        print(f"ID: {product['id']}")
        print(f"Titolo: {product['title']}")


def products_model(products: list[dict[str, any]]) -> list[dict[str, any]]:
    return [product_model_id_titolo(product) for product in products]
    
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
        id = input("Inserisci l'ID del prodotto da cercare: ").strip()
        if not id:
            print("❌ Errore: L'ID non può essere vuoto")
            return
        
        # Validazione che sia un numero
        if not id.isdigit():
            print("❌ Errore: L'ID deve essere un numero")
            return
        product = product_model(get_data(f"{BASE_URL}/{id}"))
        print_prodotto(product)

    except exceptions.HTTPError as e:
        if "404" in str(e):
            print(f"❌ Prodotto con ID '{id}' non trovato")
        else:
            print(f"❌ Errore HTTP: {e}")
            
    except exceptions.ConnectionError:
        print("❌ Impossibile connettersi al server. Controlla la tua connessione internet")
        
    except exceptions.Timeout:
        print("❌ Il server ha impiegato troppo tempo a rispondere. Riprova più tardi")
        
    except exceptions.RequestException as e:
        print(f"❌ Errore di rete: {e}")
        
    except (KeyError, TypeError) as e:
        print(f"❌ Errore nei dati ricevuti: {e}")
        
    except ValueError as e:
        print(f"❌ Errore di validazione: {e}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operazione annullata dall'utente")
        
    except Exception as e:
        print(f"❌ Errore imprevisto: {type(e).__name__}: {e}")


    products_list = products_model(get_data(f"{BASE_URL}"))
    print_products(products_list)

if __name__ == "__main__":
    main()