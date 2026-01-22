import requests
from data import get_file, get_data

def get_domanda_e_risposta_singola(file_path: str) -> str:
    try:
        with get_file(file_path) as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {file_path} non è stato trovato.")
    except RuntimeError:
        raise RuntimeError("Si è verificato un errore durante la lettura del file.")
    except Exception:
        raise Exception("Si è verificato un errore.")
    if not content.strip():
        raise ValueError("Il file è vuoto: nessuna domanda trovata")
    return content

def get_domanda_e_risposta_singola_url(URL: str) -> str:
    if URL is None:
        raise ValueError("L'URL non può essere una stringa vuota")
    try:
        return get_data(URL)
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {URL} non è stato trovato.")
    except RuntimeError:
        raise RuntimeError("Si è verificato un errore durante la lettura del file.")
    except Exception as e:
        raise Exception("Si è verificato un errore {e}.")

def get_lista_domande_e_risposte_from_server(url: str) -> str:
    lista_domande: list[str] = []
    if not url or not isinstance(url, str):
        raise ValueError("URL deve essere una stringa non vuota")
    try:
        response = requests.get(url)
        response.raise_for_status() # Verifica se la richiesta HTTP è andata a buon fine
        
        # Dividiamo il testo della risposta in righe e puliamo gli spazi
        lista_domande = [line.strip() for line in response.text.splitlines() if line.strip()]
        if not lista_domande:
            raise ValueError("Nessuna domanda valida trovata nell'URL fornito")
        return lista_domande
    except FileNotFoundError:
        raise FileNotFoundError(f"L'URL {url} non è stato trovato.")
    except RuntimeError:
        raise RuntimeError("Si è verificato un errore durante la lettura del file.")
    except Exception:
        raise Exception("Si è verificato un errore.")
    
def recupera_dati_domanda_web(url_domanda: str) -> dict[str, str]:
    """Recupera il contenuto di una singola domanda da un URL"""
    try:
        response = requests.get(url_domanda)
        response.raise_for_status()
        content = response.text
        
        index = estrai_index(content)
        return {
            "domanda": estrai_domanda(content, index),
            "risposta": estrai_risposte(content, index).strip()
        }
    except Exception as e:
        raise RuntimeError(f"Impossibile recuperare la domanda dall'URL {url_domanda}: {e}")
    
def get_lista_domande_e_risposte(file_path: str) -> list[str]:
    lista_domande: list[str] = []
    try:
        with get_file(file_path) as f:
            for i in f:
                lista_domande.append(i.strip())
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {file_path} non è stato trovato.")
    except RuntimeError:
        raise RuntimeError("Si è verificato un errore durante la lettura del file.")
    except Exception:
        raise Exception("Si è verificato un errore.")
    if not lista_domande:
        raise ValueError("Nessuna domanda valida trovata nel file")
    return lista_domande

def get_lista_domande_e_risposte_url(URL: str) -> list[str]:
    if URL is None:
        raise ValueError("L'URL non può essere una stringa vuota")
    lista_domande: list[str] = []
    try:
        text = get_data(URL)
        lista_domande = [riga.strip() for riga in text.splitlines() if riga.strip() ]
        # for i in text.splitlines():
        #         lista_domande.append(i.strip())
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {URL} non è stato trovato.")
    except RuntimeError:
        raise RuntimeError("Si è verificato un errore durante la lettura del file.")
    except Exception as e:
        raise Exception("Si è verificato un errore {e}.")
    return lista_domande

def estrai_index(content: str) -> int:
    return content.index("£")

def estrai_domanda(content: str, index: int) -> str:
    return content[0:index]

def estrai_risposte(content: str, index: int) -> str:
    return content[index+1:]

def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    return scelta.upper() == risposta_esatta
    # if scelta.upper() == risposta_esatta:
    #     return True
    # else:
    #     return False
    
"""
Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A, B, C e D.
Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è tra quelle elencate.
"""
def valida_scelta(scelta: str) -> bool:
    scelta_tmp = scelta.upper()
    return scelta_tmp in ["A", "B", "C", "D"]
    # if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
    #     return True
    # else:
    #     return False
    
"""Restituisce il valore del counter aggiornato per proseguire sulla domanda successiva o precedente."""
def get_couter_aggiornato(counter_domanda_corrente: int, input: str) -> int:
    if input.upper() == "P":
        return counter_domanda_corrente - 1
    else:
        return counter_domanda_corrente + 1

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

"""Calcola la percentuale (0-100) date due quantità."""
def calcola_percentuale(parte: int, totale: int) -> float:
    if totale == 0:
        return 0.0
    return (parte / totale) * 100

"""Restituisce True se la percentuale è maggiore o uguale alla soglia."""
def verifica_superamento(percentuale: float, soglia: float = 60.0) -> bool:
    return percentuale >= soglia

"""Gestisce il parsing di ogni domanda"""
def recupera_dati_domanda(nome_file: str) -> dict[str, str]:
    content: str = get_domanda_e_risposta_singola(f"domande_risposte/{nome_file}")
    index: int = estrai_index(content)
    return {
        "domanda": estrai_domanda(content, index),
        "risposta": estrai_risposte(content, index)
    }

"""Gestisce il parsing di ogni domanda"""
def recupera_dati_domanda_url(URL: str) -> dict[str, str]:
    content: str = ""
    if URL is None:
        raise ValueError("L'URL non può essere una stringa vuota")
    try:
        content = get_data(URL)
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {URL} non è stato trovato.")
    except RuntimeError:
        raise RuntimeError("Si è verificato un errore durante la lettura del file.")
    except Exception as e:
        raise Exception("Si è verificato un errore {e}.")

    index: int = estrai_index(content)
    return {
        "domanda": estrai_domanda(content, index),
        "risposta": estrai_risposte(content, index)
    }

"""Aggiorna la lista dei risultati gestendo sia l'inserimento che la modifica."""
def aggiorna_lista_risultati(lista_risultati: list, nuovo_risultato: dict, indice: int) -> None:
    indice_lista_risultati: int = len(lista_risultati)
    if indice < indice_lista_risultati:
        lista_risultati[indice] = nuovo_risultato
    else:
        lista_risultati.append(nuovo_risultato)

# def get_domanda_e_risposte(content: str) -> tuple[str, str]:
#     index = content.index("£")
#     domanda = content[0:index]
#     risposte = content[index+1:]
#     return domanda, risposte