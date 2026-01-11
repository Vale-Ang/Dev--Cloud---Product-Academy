# CONTACARATTERI

# DOMINIO:
# =========

# 1. INPUT - Sorgente del testo
#    - Lettura da file di testo (.txt)
#    - Visualizzazione contenuto in console

# 2. ELABORAZIONE - Metriche da calcolare
#   - Conteggio caratteri (con e senza spazi)
#   - Conteggio parole
#   - Conteggio frasi
#   - Conteggio paragrafi
#   - Tempo di lettura stimato
#   - Frequenza parole e lettere (ripetizioni)

# 3. OUTPUT - Destinazione risultati
#    - Stampa in console
#    - Scrittura su file

# REGEX REFERENCE:
# ================

# Pattern                 | Descrizione
# ------------------------|--------------------------------------------
# .                       | Tutti i caratteri (con re.DOTALL include \n)
# \S                      | Caratteri senza spazi
# [a-zA-ZÀ-ÿ]             | Solo lettere (incluse accentate)
# \w+                     | Parole (lettere, numeri, underscore)
# [a-zA-ZÀ-ÿ]+            | Parole solo lettere (incluse accentate)
# [^.!?]+[.!?]+           | Frasi (testo seguito da punteggiatura)
# testo.split('\\n\\n')   | Paragrafi (separati da riga vuota)

# ===============================
#   Regex Patterns
# ===============================

# REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
# REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
# REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
# REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
# REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
# REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?


# ===============================
#   TODO 
# =============================== 

# 1. Migliorare gestione delle eccezzioni
# 2. Unificare gestione stream e buffer dati 
# 3. Suddividere in moduli

# ===============================
#   CONFIGURAZIONI E COSTANTI
# =============================== 

REGEX_TUTTI_CARATTERI = r'.'           # Tutti i caratteri (usare con re.DOTALL)
REGEX_SENZA_SPAZI = r'\S'              # Caratteri esclusi gli spazi
REGEX_SOLO_LETTERE = r'[a-zA-ZÀ-ÿ]'   # Solo lettere, incluse accentate
REGEX_PAROLE = r'\w+'                  # Parole (lettere, numeri, underscore)
REGEX_PAROLE_LETTERE = r'[a-zA-ZÀ-ÿ]+' # Parole composte solo da lettere
REGEX_FRASI = r'[^.!?]+[.!?]+'         # Frasi terminate da . ! ?


# from io_utils import leggi_file
# from text_analyzer import conta_caratteri, frequenza_caratteri
# from frontend import stampa_numero_caratteri, stampa_frequenza_caratteri

from ui.console import print_risultato
from data.services import get_caratteri_len, get_text_no_space, get_words_number, get_phrase_number
from data.repositoty import get_file_content

# Sposta in repository
# ===========================
# Repository
# ===========================

# """Restituisce un oggetto TextIO con il contenuto del file specificato"""
# def get_file_content(file_path: str)-> str:
#     if not file_path:
#         raise ValueError("Il file path non può essere vuoto!")

#     try:
#         with open(file_path, 'r') as f:
#             content = f.read()
#             return content
#     except FileNotFoundError:
#         raise FileNotFoundError("Il file non esiste")
    
# Spostato services in data
# # ===========================
# # Service
# # ===========================

# """Conta i caratteri"""
# def get_caratteri_len(text: str)-> int:
#     if not text:
#         return 0
#     return len(text)

# # def stampa_testo_input(text:TextIO) -> None:
# #     with text as f:
# #         content = f.read()
# #         print (content)

# # def get_testo(text: TextIO) -> str:
     
# #     with text as f:
# #         content = f.read()
# #         return content

# # def get_text_len(text: str) -> int:
# #     if text is None:
# #         print("La stringa è vuota")
# #     print(len(text))

# """Restituisci il testo senza gli spazi"""
# import re
# def get_text_no_space(text: str) -> str:
#     return (re.findall(REGEX_SENZA_SPAZI, text))

# """Restituisce il numero di parole in una stringa"""
# def get_words_number(text: str) -> int:
#     if not text:
#         return 0
#     return len(re.findall(REGEX_PAROLE_LETTERE, text))

# """Restituisce il numero di frasi in una stringa"""
# def get_phrase_number(text: str) -> int:
#     if not text:
#         return 0
#     return len(re.findall(REGEX_FRASI, text))


# sposto tutto in console.py
# ===========================
# UI
# ===========================

# """Stampa il risultato delle operzioni di calcolo caratteri etc."""
# def print_risultato(value: int, spec: str) -> None:
#     if value is None:
#         raise ValueError(f"{value} è obbligatorio (non può essere None)")
#     if not isinstance(value,(int)):
#         raise TypeError(f"{value} deve essere un numero")
    
#     print('*'*30)
#     print(f"Il numero si {spec} è {value }") 
#     print('*'*30)


def main():

    try:
        # print("aperto stream")
        content: str = get_file_content("prova.txt")
        # testo: str = get_testo(content)
        print(content)
        print_risultato(get_caratteri_len(content), "caratteri")
        # get_text_len(content)
        print_risultato(get_caratteri_len(get_text_no_space(content)), "caratteri senza spazi")
        print_risultato(get_words_number(content), "parole")
        print_risultato(get_phrase_number(content), "frasi")
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