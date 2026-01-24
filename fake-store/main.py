from requests import exceptions
from data.repository import get_data
from data.service import product_model, products_model
from ui.console import print_products, print_prodotto
from constants import BASE_URL


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