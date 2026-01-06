import sys

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
        return "Non hai indovinato."

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
        # index = content.index("£")
        # question = content[0:index]
        # answers = content[index+1:]
        # print(question)
        # print('-------')
        # print(answers)
        # print(content)
        # print(type(content))
        # print (len(content))
        # print(content.index("£"))

def estrai_index(content: str) -> int:
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    # index = content.index("£")
    return content[0:index]
    # return question
def estrai_risposte(content: str, index: int) -> str:
    # index = content.index("£")
    return content[index+1:]
    # return answers

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
    # print(f"Hai risposto correttamente a {risposte_esatte} domande.")
    # print(f"Hai risposto in modo errato a {risposte_non_esatte} domande.")
    return statistica

def conta_domanda(counter_domanda_corrente: int, lista_domande_len: int) -> None:
    print('*'*40)
    print(f"Domanda {counter_domanda_corrente +1} di {lista_domande_len}")
    print('*'*40)



def main():
    lista_domande: list[str] = []
    domanda_e_risposta: dict[str, str] = {
        "domanda": None,
        "risposta": None
    }

    counter_domanda_corrente: int = 0
    risultato_finale: list[dict[str, str | bool]] = []

    # with open("domande.txt","r") as f:
    #     for i in f:
    #         # print(i)
    #         # print(i.strip())
    #         lista_domande.append(i.strip())
    #     # print(f.read())

    # with open(lista_domande[0],"r") as f:
    #     for i in f:
    #         print(i.strip())

    lista_domande = estrai_lista_domande("domande.txt")
    lista_domande_length: int = len(lista_domande)
    # print(f"domande: {counter_domanda_corrente}")

    # {
        # "domanda": "file_nome.txt",
        # "risposta_corretta": True
    # }

    while counter_domanda_corrente < lista_domande_length:
        conta_domanda(counter_domanda_corrente, lista_domande_length)
    # for q in range(counter_domanda_corrente):
        risultato: dict[str, str | bool] = {}
        content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        # print(lista_domande)
        index: int = estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content, index)
        domanda_e_risposta["risposta"] = estrai_risposte(content, index)
        # input(domanda_e_risposta["domanda"])
        # print(domanda_e_risposta)
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
            # domanda_pre_o_su = domanda_precendete_o_sucessiva(counter_domanda_corrente, lista_domande_length)
            # counter_domanda_corrente = aggiorna_counter_domanda(counter_domanda_corrente, domanda_pre_o_su)
            # counter_domanda_corrente += 1
        else:
            feedback = "Inserisci solo la risposta tra le opzioni elencate"

        mostra_feedback(feedback)
    
    statistiche = genera_statistiche(risultato_finale)
    print(f"Risposte esatte: {statistiche['risposte_esatte']}")
    print(f"Risposte non esatte: {statistiche['risposte_non_esatte']}")

    print(risultato_finale)
    
        


#Entry point del nostro programma
main()

