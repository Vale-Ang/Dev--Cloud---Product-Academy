# from requests.exceptions import ValueError, FileNotFoundError, Exception
from data.repository import get_prodotto, get_lista_prodotti, post_data, send_product
from data.service import product_model, products_model
from ui.console import print_products, print_prodotto
from constants import BASE_URL


product = {
  "title": "Shirt",
  "price": 50,
  "description": "A description",
  "categoryId": 1,
  "images": ["https://placehold.co/600x400"]
}


def main():

    while True:
        titolo = input("Inserisci il titolo del prodotto: ").strip()
        if titolo is None or titolo == "" or type(titolo) is not str:
            print("Errore: Il titolo che hai inserito non è valido.")
            continue
        else:
            product["title"] = titolo
            break
    while True:
        prezzo = input("Inserisci il prezzo del prodotto: ").strip()
        try:
            prezzo_float = float(prezzo)
            if prezzo_float <= 0 or prezzo_float is None or type(prezzo_float) is not float:
                print("Errore: Il prezzo che hai inserito non è valido.")
                continue
            product["price"] = prezzo_float
            break
        except ValueError:
            print("Errore: Il prezzo deve essere un numero valido.")
    while True:
        descrizione = input("Inserisci la descrizione del prodotto: ").strip()
        if descrizione is None or descrizione == "" or type(descrizione) is not str:
            print("Errore: La descrizione che hai inserito non è valida.")
            continue
        else:
            product["description"] = descrizione
            break

    try:
        products_list = products_model(get_lista_prodotti(f"{BASE_URL}"))
        print_products(products_list)
        # print_prodotto(product_model(send_product(BASE_URL, product)))
        # id = input("Inserisci l'ID del prodotto da cercare: ").strip()
        # if not id:
        #     print("Errore: L'ID non può essere vuoto")
        #     return
        
        # # Validazione che sia un numero
        # if not id.isdigit():
        #     print("Errore: L'ID deve essere un numero")
        #     return
        # product = product_model(get_prodotto(f"{BASE_URL}/{id}"))
        # print_prodotto(product)

    except ValueError as e:
        print(f"Errore di validazione: {e}")
    except FileNotFoundError as e:
        print(f"File non trovato: {e}")
    except Exception as e:
        print(f"Errore imprevisto: {e}")

    # except exceptions.HTTPError as e:
    #     if "404" in str(e):
    #         print(f"❌ Prodotto con ID '{id}' non trovato")
    #     else:
    #         print(f"❌ Errore HTTP: {e}")
            
    # except exceptions.ConnectionError:
    #     print("❌ Impossibile connettersi al server. Controlla la tua connessione internet")
        
    # except exceptions.Timeout:
    #     print("❌ Il server ha impiegato troppo tempo a rispondere. Riprova più tardi")
        
    # except exceptions.RequestException as e:
    #     print(f"❌ Errore di rete: {e}")
        
    # except (KeyError, TypeError) as e:
    #     print(f"❌ Errore nei dati ricevuti: {e}")
        
    # except ValueError as e:
    #     print(f"❌ Errore di validazione: {e}")
        
    # except KeyboardInterrupt:
    #     print("\n\n⚠️  Operazione annullata dall'utente")
        
    # except Exception as e:
    #     print(f"❌ Errore imprevisto: {type(e).__name__}: {e}")


    # try:
    #     products_list = products_model(get_lista_prodotti(f"{BASE_URL}"))
    #     print_products(products_list)
    # except ValueError as e:
    #     print(f"Errore di validazione: {e}")
    # except FileNotFoundError as e:
    #     print(f"File non trovato: {e}")
    # except Exception as e:
    #     print(f"Errore imprevisto: {e}")

if __name__ == "__main__":
    main()