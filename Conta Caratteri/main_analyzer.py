# from io_utils import leggi_file
# from text_analyzer import conta_caratteri, frequenza_caratteri
# from frontend import stampa_numero_caratteri, stampa_frequenza_caratteri

# ===========================
# Repository
# ===========================

from typing import TextIO

"""Restituisce un oggetto TextIO con il contenuto del file specificato"""
def get_file_content(file_path: str)-> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError
    

# ===========================
# Service
# ===========================

# def stampa_testo_input(text:TextIO) -> None:
#     with text as f:
#         content = f.read()
#         print (content)

# def get_testo(text: TextIO) -> str:
     
#     with text as f:
#         content = f.read()
#         return content

def get_text_len(text: str) -> int:
    if text is None:
        print("La stringa è vuota")
    print(len(text))

import re
def get_text_len_no_space(text: str) -> int:
    print(len(re.findall(r"\S", text)))

def main():

    try:
        # print("aperto stream")
        content: str = get_file_content("helloword.txt")
        # testo: str = get_testo(content)
        print(content)
        get_text_len(content)
        get_text_len_no_space(content)
    except ValueError as e:    
        print(f"{e}")
    except FileNotFoundError as e:
        print(f"{e}")
    except Exception as e:
        print(f"{e}")
    finally:
        print("fine try catch")
    
    # except FileNotFoundError as e:
        # print(f"File not found {e}")
    # finally:
    #     print ("stream chiuso")
#     percorso_file = "prova.txt"
#     testo: str = leggi_file(percorso_file)
#     numero_caratteri: int = conta_caratteri(testo)
#     stampa_numero_caratteri(numero_caratteri)
#     frequenza: dict = frequenza_caratteri(testo)
#     stampa_frequenza_caratteri(frequenza)


    

if __name__ == "__main__":
    main()


"""
- Dove si trova il testo?
    - Il testo viene preso da un file
    - I file vengono mostrati a video dalla console
- Voglio contare i caratteri di un testo
    - Contare i caratteri con e senza spazi
    - Voglio contare anche le parole
    - Voglio contare le frasi
    - Voglio contare i paragrafi
    - Voglio avere il tempo di lettura
    - Voglio verificare le ripetizioni delle parole e della lettera
- Dove voglio mostrare il risultato?
    - Console
    - Scriverlo su file

input --> programma --> output
"""