import sys
from data import get_couter_aggiornato, is_risposta_esatta, valida_scelta, genera_statistiche, get_numero_domanda_corrente, get_lista_domande_e_risposte, calcola_percentuale, recupera_dati_domanda, verifica_superamento, aggiorna_lista_risultati
from ui import mostra_feedback, mostra_domanda, print_numero_domanda, print_gioco_terminato, raccogli_risposta, genera_feedback, mostra_risultati_finali, gestisci_menu_fine_gioco


# Funzione mostra_feedback spostata in frontend_layer.py
# def mostra_feedback(messaggio: str) -> None:
#     simbol = "*"*40
#     print(f"""
# {simbol}
# {messaggio}
# {simbol}
# """)

# def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
#     if scelta.upper() == risposta_esatta:
#         return True
#     else:
#         return False

# """
# Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
# Questa funzione viene eseguita solo se la funzione di validazione restituisce true.
# """
# def genera_feedback(is_corretta: bool) -> str:
#     if is_corretta == True:
#         return "Hai indovinato!"
#     else:
#         return "Non hai indovinato. Ritenta!"

# """
# Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D.
# Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è tra quelle elencate.
# """
# def valida_scelta(scelta: str) -> bool:
#     scelta_tmp = scelta.upper()
#     if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
#         return True
#     else:
#         return False

# Funzione mostra_domanda spostata in frontend_layer.py 
# """
# Questa funzione restituisce la domanda e le opzioni della risposta
# """
# def mostra_domanda(domanda: str) -> None:
#     print(domanda)

# """
# Questa funzione si occupa solamente di prendere l'input dell'utente
# Il controllo di tale valore avverrà attraverso una funzione dedicata.
# """
# def raccogli_risposta() -> str:
#     return input("Inserisci la tua scelta: ")

# leggi_file diventa get_domanda e lo sposto in data_model_layer.py
# def leggi_file(file_path: str) -> str:
#     # with open(file_path, "r") as file:
#     with get_file(file_path) as file:
#         content = file.read()
#         return content

# # estrai_index lo sposto in service.py
# def estrai_index(content: str) -> int:
#     return content.index("£")
# # estrai_domanda lo sposto in service.py
# def estrai_domanda(content: str, index: int) -> str:
#     return content[0:index]
# # estrai_risposte lo sposto in service.py
# def estrai_risposte(content: str, index: int) -> str:
#     return content[index+1:]

# estrai_lista_domande diventa get_lista_domande e lo sposto in data_model_layer.py
# def estrai_lista_domande(file_path: str) -> list[str]:
#     lista_domande: list[str] = []
#     # with open(file_path,"r") as f:
#     with get_file(file_path) as f:
#         for i in f:
#             lista_domande.append(i.strip())
#     return lista_domande

# def genera_statistiche(risultato_finale: list[dict[str, str | bool]]) -> dict[str, int]:
#     statistica: dict[str, int] = {}
#     risposte_esatte: int = 0
#     risposte_non_esatte: int = 0
#     for i in risultato_finale:
#         if i["risposta_corretta"]:
#             risposte_esatte += 1
#         else:
#             risposte_non_esatte += 1
#     statistica["risposte_esatte"] = risposte_esatte
#     statistica["risposte_non_esatte"] = risposte_non_esatte
#     return statistica

# """Restiusce l'indice della domanda corrente incrementato di 1 per l'utente."""

# def get_numero_domanda_corrente(value: int) -> int:
#     return value +1

# Funzione print_numero_domanda spostata in frontend_layer.py
# """Restituisce l'indicatore della domanda corrente, rispetto alle domande totali"""
# def print_numero_domanda(valore_domanda_corrente: int, lista_domande_length) -> None:
#     print("------------------------------")
#     print(f"Domanda {valore_domanda_corrente} di {lista_domande_length}")
#     print("------------------------------")

# """Restituisce il valore del counter aggiornato per proseguire sulla domanda successiva o precedente."""
# def get_couter_aggiornato(counter_domanda_corrente: int, input: str) -> int:
#     if input.upper() == "P":
#         counter_domanda_corrente -= 1
#     else:
#         counter_domanda_corrente += 1
#     return counter_domanda_corrente

def main():
    # lista_domande: list[str] = []
    lista_domande = get_lista_domande_e_risposte("domande.txt")

    # domanda_e_risposta: dict[str, str] = {
    #     "domanda": None,
    #     "risposta": None
    # }

    risultato_finale: list[dict[str, str | bool]] = []
    counter_domanda_corrente: int = 0

    # lista_domande = get_lista_domande("domande.txt")
    lista_domande_length: int = len(lista_domande)

    while counter_domanda_corrente <= lista_domande_length:
        if counter_domanda_corrente == lista_domande_length:
            nuovo_indice = gestisci_menu_fine_gioco(counter_domanda_corrente, lista_domande_length, risultato_finale)
            if nuovo_indice is None: 
                break
            counter_domanda_corrente = nuovo_indice
            continue
         
        # # content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        # content: str = get_domanda(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        # index: int = estrai_index(content)
        # domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        # domanda_e_risposta["risposta"] = estrai_risposte(content, index)
        
        # recupero dei dati
        dati_correnti = recupera_dati_domanda(lista_domande[counter_domanda_corrente]) 

        valore_domanda_corrente: int = get_numero_domanda_corrente(counter_domanda_corrente)
        print_numero_domanda(valore_domanda_corrente, lista_domande_length)
        mostra_domanda(dati_correnti["domanda"])

        # input dell'utente
        risposta_utente: str = raccogli_risposta()

        feedback: str = ""

        # is_risposta_valid: bool = valida_scelta(risposta_utente)

        # if is_risposta_valid == True:
        if valida_scelta(risposta_utente):
            is_risposta_corretta: bool = is_risposta_esatta(risposta_utente, dati_correnti["risposta"])
            mostra_feedback(genera_feedback(is_risposta_corretta))
            
            # feedback = genera_feedback(is_risposta_corretta)
            risultato = {
                "domanda": lista_domande[counter_domanda_corrente],
                "risposta_corretta": is_risposta_corretta,
                "risposta_utente": risposta_utente.upper()
            }

            # risultato["domanda"] = lista_domande[counter_domanda_corrente]
            # risultato["risposta_corretta"] = is_risposta_corretta
            # risultato_finale_len: int = len(risultato_finale)

            # if counter_domanda_corrente < risultato_finale_len:
            #     risultato_finale[counter_domanda_corrente] = risultato
            # else:
            #     risultato_finale.append(risultato)

            aggiorna_lista_risultati(risultato_finale, risultato, counter_domanda_corrente)

        else:
            mostra_feedback("Inserisci solo la risposta tra le opzioni elencate")


        if counter_domanda_corrente > 0:
            input_prev_next: str = input("Digita 'P' per tornare alla domanda precedente, qualsiasi altro tasto per proseguire: ")
            counter_domanda_corrente = get_couter_aggiornato(counter_domanda_corrente, input_prev_next)
        else:
            counter_domanda_corrente += 1
    
    #statistiche finali
    print_gioco_terminato()

    statistiche: dict[str, int] = genera_statistiche(risultato_finale)
    esatte = statistiche["risposte_esatte"]
    errate = statistiche["risposte_non_esatte"]
    totale_domande_fatte = esatte + errate

    perc = calcola_percentuale(esatte, totale_domande_fatte)
    is_superato = verifica_superamento(perc)

    mostra_risultati_finali(esatte, errate, totale_domande_fatte, perc, is_superato)
    


    # Creo una funzione print_gioco_terminato in frontend_layer.py
    # print("*"*40)
    # print("GIOCO TERMINATO! Ecco i risultati:")
    # print("*"*40)

    # Creo una funzione print_statistiche in frontend_layer.py
    # print(f"Risposte esatte: {statistiche['risposte_esatte']}")
    # print(f"Risposte non esatte: {statistiche['risposte_non_esatte']}")
     # print(risultato_finale)

    # print_statistiche(statistiche, risultato_finale)

#Entry point del nostro programma
# main()
if __name__ == "__main__":
    
    """Esempi di utilizzo del modulo operazioni.py"""
    # print(operazioni.moltiplica(2,2))
    # print(moltiplica(2,2))
    # print(op.moltiplica(2,2))
    main()