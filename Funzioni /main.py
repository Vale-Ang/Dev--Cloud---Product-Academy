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

def is_risposta_esatta(scelta: str) -> bool:
    if scelta.upper() == "A":
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
def mostra_domanda() -> None:
    print(
"""
Domanda?
A
B
C
D
"""
)



"""
Questa funzione si occupa solamente di prendere l'input dell'utente
Il controllo di tale valore avverrà attraverso una funzione dedicata.
"""
def raccogli_risposta() -> str:
    return input("Inserisci la tua scelta: ")


def main():
    is_risposta_corretta: bool = False
    while True:
        mostra_domanda()
        risposta_da_validare: str = valida_scelta()
        risposta_validarta: bool = valida_scelta(risposta_da_validare)
        feedback: str = ""

        if risposta_validarta == True:
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare)
            feedback = genera_feedback(is_risposta_corretta)
        else:
            feedback = "Inserisci solo la risposta tra le opzioni elencate"
        
        mostra_feedback(feedback)
        if is_risposta_corretta == True:
            break

#Entry point del nostro programma
main()