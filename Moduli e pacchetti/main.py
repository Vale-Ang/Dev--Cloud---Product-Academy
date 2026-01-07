import sys
# import operazioni
# from operazioni import moltiplica
import operazioni as op 

def mostra_feedback(messaggio: str) -> None:
    simbol = "*"*40
    print(f"""
{simbol}
{messaggio}
{simbol}
""")

def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False

"""
Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
Questa funzione viene eseguita solo se la funzione di validazione restituisce true.
"""
def genera_feedback(is_corretta: bool) -> str:
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato. Ritenta!"

"""
Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D.
Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è tra quelle elencate.
"""
def valida_scelta(scelta: str) -> bool:
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else:
        return False
    
"""
Questa funzione restituisce la domanda e le opzioni della risposta
"""
def mostra_domanda(domanda: str) -> None:
    print(domanda)



"""
Questa funzione si occupa solamente di prendere l'input dell'utente
Il controllo di tale valore avverrà attraverso una funzione dedicata.
"""
def raccogli_risposta() -> str:
    return input("Inserisci la tua scelta: ")


def leggi_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
        return content
         

def estrai_index(content: str) -> int:
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    return content[0:index]

def estrai_risposte(content: str, index: int) -> str:
    return content[index+1:]

def estrai_lista_domande(file_path: str) -> list[str]:
    lista_domande: list[str] = []
    with open(file_path,"r") as f:
        for i in f:
            lista_domande.append(i.strip())
    return lista_domande

def genera_statistiche(risultato_finale: list[dict[str, str | bool]]) -> dict[str, int]:
    statistica: dict[str, int] = {}
    risposte_esatte: int = 0
    risposte_non_esatte: int = 0
    for i in risultato_finale:
        if i["risposta_corretta"]:
            risposte_esatte += 1
        else:
            risposte_non_esatte += 1
    statistica["risposte_esatte"] = risposte_esatte
    statistica["risposte_non_esatte"] = risposte_non_esatte
    return statistica

"""Restiusce l'indice della domanda corrente incrementato di 1 per l'utente."""

def get_numero_domanda_corrente(value: int) -> int:
    return value +1

"""Restituisce l'indicatore della domanda corrente, rispetto alle domande totali"""
def print_numero_domanda(valore_domanda_corrente: int, lista_domande_length) -> None:
    print("------------------------------")
    print(f"Domanda {valore_domanda_corrente} di {lista_domande_length}")
    print("------------------------------")

"""Restituisce il valore del counter aggiornato per proseguire sulla domanda successiva o precedente."""
def get_couter_aggiornato(counter_domanda_corrente: int, input: str) -> int:
    if input.upper() == "P":
        counter_domanda_corrente -= 1
    else:
        counter_domanda_corrente += 1
    return counter_domanda_corrente

def main():
    lista_domande: list[str] = []
    domanda_e_risposta: dict[str, str] = {
        "domanda": None,
        "risposta": None
    }

    counter_domanda_corrente: int = 0
    risultato_finale: list[dict[str, str | bool]] = []

    lista_domande = estrai_lista_domande("domande.txt")
    lista_domande_length: int = len(lista_domande)

    while counter_domanda_corrente <= lista_domande_length:
        if counter_domanda_corrente == lista_domande_length:
            break
         
        
        content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index: int = estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposte(content, index)
        valore_domanda_corrente: int = get_numero_domanda_corrente(counter_domanda_corrente)
        print_numero_domanda(valore_domanda_corrente, lista_domande_length)
        mostra_domanda(domanda_e_risposta["domanda"])
        risposta_utente: str = raccogli_risposta()
        is_risposta_valid: bool = valida_scelta(risposta_utente)
        feedback: str = ""

        if is_risposta_valid == True:
            risultato: dict[str, str | bool] = {}
            is_risposta_corretta: bool = is_risposta_esatta(risposta_utente, domanda_e_risposta["risposta"])
            feedback = genera_feedback(is_risposta_corretta)
            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta
            risultato_finale_len: int = len(risultato_finale)

            if counter_domanda_corrente < risultato_finale_len:
                risultato_finale[counter_domanda_corrente] = risultato
            else:
                risultato_finale.append(risultato)
        else:
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)
        if counter_domanda_corrente > 0:
            input_prev_next = input("Digita 'P' per tornare alla domanda precedente, qualsiasi altro tasto per proseguire: ")
            counter_domanda_corrente = get_couter_aggiornato(counter_domanda_corrente, input_prev_next)
        else:
            counter_domanda_corrente += 1
    
    statistiche = genera_statistiche(risultato_finale)
    print("*"*40)
    print("GIOCO TERMINATO! Ecco i risultati:")
    print("*"*40)
    print(f"Risposte esatte: {statistiche['risposte_esatte']}")
    print(f"Risposte non esatte: {statistiche['risposte_non_esatte']}")

    print(risultato_finale)

#Entry point del nostro programma
# main()


"""Esempi di utilizzo del modulo operazioni.py"""
# print(operazioni.moltiplica(2,2))
# print(moltiplica(2,2))
print(op.moltiplica(2,2))