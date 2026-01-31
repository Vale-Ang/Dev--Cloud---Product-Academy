def is_carrello_pieno(carrello_della_spesa: list[str], lista_spesa_len: int) -> bool:
    if len(carrello_della_spesa) < lista_spesa_len:
        return True
    else:
        return False

def get_prodotto_formattato(prodotto: str) -> str:
    if not prodotto:
        log_message("Il prodotto non deve essere vuoto", "ERROR")
    
    return prodotto.strip().lower()

def get_input_from_utente(text: str) -> str:
    if not text:
        log_message("Il messaggio non deve essere vuoto", "ERROR")

    print("*"*30)
    return input(text)

def log_message(message: str, type: str = "INFO") -> None:
   if not message:
        log_message("Il messaggio non deve essere vuoto", "ERROR")
    
   icon = None
   match type:
     case "ALERT":
      icon = "⚠️"
     case "INFO":
      icon = "✅"
     case "ERROR":
      icon = "❌"
    
   print(f"{icon} - {message}")



def main() -> None:
    log_message("Start del programma")

    lista_spesa: list[str] = ["farina", "acqua", "lievito", "pane", "pomodoro", "mozzarella", "sale", "olio", "zucchero", "uova"]
    carrello_della_spesa: list[str] = []
    lista_spesa_len: int = len(lista_spesa)

    while(is_carrello_pieno(carrello_della_spesa,lista_spesa_len)):
        prodotto: str = get_input_from_utente("inserisci un prodotto: ")
        if not prodotto:
            log_message("Il prodotto non può essere vuoto", "ERROR")

        prodotto_formattato: str = get_prodotto_formattato(prodotto)
        
        if prodotto_formattato in lista_spesa:

            if prodotto_formattato in carrello_della_spesa:
                log_message("Prodotto già inserito", "ALERT")
            else:
                carrello_della_spesa.append(prodotto_formattato)
                log_message(prodotto_formattato, "INFO")

        else: 
            log_message("Prodotto non valido", "ALERT")


    print("Procedi al pagamento")
    print("End del programma")

main()
    



