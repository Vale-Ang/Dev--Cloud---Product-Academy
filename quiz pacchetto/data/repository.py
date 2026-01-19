from typing import TextIO

"""Recupera un oggetto imput/output (IO) di tipo testuale da un file specificato"""
def get_file(file_path: str) -> TextIO:
    if not isinstance(file_path, str):
        raise TypeError("file_path deve essere una stringa")
    try:
        return open(file_path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {file_path} non è stato trovato.")
    except Exception:
        raise Exception("Si è verificato un errore.")

def send_questions(file_path: str) -> TextIO:
    if not isinstance(file_path, str):
        raise TypeError("file_path deve essere una stringa")
    try:
        return open(file_path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Il file {file_path} non è stato trovato.")
    except Exception:
        raise Exception("Si è verificato un errore.")

