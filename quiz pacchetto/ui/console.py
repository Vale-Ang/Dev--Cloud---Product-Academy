
def mostra_feedback(messaggio: str) -> None:
    simbol = "*"*40
    print(f"""
{simbol}
{messaggio}
{simbol}
""")
    
"""
Questa funzione restituisce la domanda e le opzioni della risposta
"""
def mostra_domanda(domanda: str) -> None:
    print(domanda)

"""Restituisce l'indicatore della domanda corrente, rispetto alle domande totali"""
def print_numero_domanda(valore_domanda_corrente: int, lista_domande_length) -> None:
    print("------------------------------")
    print(f"Domanda {valore_domanda_corrente} di {lista_domande_length}")
    print("------------------------------")


def print_gioco_terminato() -> None:
    print("*"*40)
    print("GIOCO TERMINATO! Ecco i risultati:")
    print("*"*40)

def print_statistiche(statistiche: dict[str, int], risultato_finale: list[dict[str, str | bool]]) -> None:   
    print(f"Risposte esatte: {statistiche['risposte_esatte']}")
    print(f"Risposte non esatte: {statistiche['risposte_non_esatte']}")
    print(risultato_finale)