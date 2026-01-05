import sys

"""
mostra_menu() (senza return)
- Non prende parametri
- Stampa la domanda e le 4 opzioni
- Non restituisce nulla

raccogli_risposta() (con return)
- Non prende parametri
- Chiede l'input all'utente
- Restituisce la scelta

valida_scelta(scelta) (con return)
- prende come parametro il valore scelto
- Verifica se è A, B, C o D usando if
- Restituisce True se valida, False altrimenti

genera_feedback(scelta) (con return)
- Prende come parametro la lettera che è stata scelta
- Usa if/elif/else per determinare il messaggio
- Restituisce la stringa con il feedback personalizzato

mostra_feedback(messaggio) (senza return)
- Prende come parametro una stringa
- Stampa il feedback in modo formattato
- Non restituisce nulla
"""
"""
Restituisci il feedback formatato nella maniera desiderata.<
"""
def mostra_feedback(messaggio: str) -> None:
    simbol = "*"*40
    print(f"""
{simbol}
{messaggio}
{simbol}
""")

def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    # if scelta.upper() == "A":
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
#     print(
# """
# Domanda?
# A
# B
# C
# D
# """
# )



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
        
# ) -> None:
#     with open("domanda-1.txt", "r") as file:
#         content = file.read()
#     print (content) 

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

def main():
    lista_domande: list[str] = []
    domanda_e_risposta: dict[str, str] = {
        "domanda": None,
        "risposta": None
    }

    counter_domanda_corrente: int = 0
    risultato_finale: list[dict[str, str | bool]] = []

    lista_domande = estrai_lista_domande("domande.txt")
    lista_domande_len: int = len(lista_domande)

    while counter_domanda_corrente < lista_domande_len:

        risultato: dict[str, str | bool] = {}
        content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index: int = estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposte(content, index)

        mostra_domanda(domanda_e_risposta["domanda"])
        risposta_utente: str = raccogli_risposta()
        is_risposta_valid: bool = valida_scelta(risposta_utente)
        feedback: str = ""

        if is_risposta_valid == True:
            is_risposta_corretta: bool = is_risposta_esatta(risposta_utente, domanda_e_risposta["risposta"])
            feedback = genera_feedback(is_risposta_corretta)
            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta
            risultato_finale.append(risultato)
            counter_domanda_corrente += 1
        else:
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)
    
    statistiche = genera_statistiche(risultato_finale)
    print(f"Risposte esatte: {statistiche['risposte_esatte']}")
    print(f"Risposte non esatte: {statistiche['risposte_non_esatte']}")

    print(risultato_finale)
    """
    file_path: str = sys.argv[1]
    # print(sys.argv[1])
    content: str = leggi_file(file_path)
    index: int = estrai_index(content)
    domanda: str = estrai_domanda(content, index)
    risposta: str = estrai_risposte(content, index)

    is_risposta_corretta: bool = False
    while True:
        mostra_domanda(domanda)
        # mostra_domanda()
    
        risposta_da_validare: str = raccogli_risposta()
        # risposta_da_validare: str = valida_scelta()
        risposta_validarta: bool = valida_scelta(risposta_da_validare)
        feedback: str = ""

        if risposta_validarta == True:
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare, risposta)
            feedback = genera_feedback(is_risposta_corretta)
        else:
            feedback = "Inserisci solo la risposta tra le opzioni elencate"
        
        mostra_feedback(feedback)
        if is_risposta_corretta == True:
            break

"""

#Entry point del nostro programma
main()