# ===========================
# Repository
# ===========================
import requests

"""Restituisce un oggetto TextIO con il contenuto del file specificato"""
def get_file_content(file_path: str)-> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError("Il file non esiste")
    
def get_data_from_server(url: str) -> str:
    if not url or not isinstance(url, str):
        raise ValueError("URL deve essere una stringa non vuota")
    try:
        response = requests.get(url)
        return response.text 
        # print(response.text) #serializzo il contenuto della risposta 
        # print(response)
        # print(type(response)) #oggetto di tipo response

    except Exception:
        raise Exception("Problema con la chiamata al server")
