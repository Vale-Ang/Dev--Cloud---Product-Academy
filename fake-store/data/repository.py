from requests import get, post, Response
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException  

def get_lista_prodotti(URL: str) -> list[dict[str, any]]:
    if URL is None:
        raise ValueError("URL non può essere vuoto")
    try:
        response: Response = get_data(URL)
        data = response.json()
        if not isinstance(data, list):
            raise TypeError(f"Risposta inattesa: attesa una lista di prodotti, ma ricevuto {type(data).__name__}")
        return data
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")

def get_prodotto(URL: str) -> dict[str, any]:
    if URL is None:
        raise ValueError("URL non può essere vuoto")
    try:
        response: Response = get_data(URL)
        data = response.json()
        if not isinstance(data, dict):
            raise TypeError(f"Risposta inattesa: mi aspettavo un dizionario, ma ricevuto {type(data).__name__}")
        return data
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")
    
def send_product(url: str, data: dict) -> dict[str, any]:
    if url is None:
        raise ValueError("URL non può essere vuoto")
    if data is None:
        raise ValueError("I dati del prodotto non possono essere vuoti")
    if not isinstance(data, dict):
        raise TypeError(f"Risposta inattesa: mi aspettavo un dizionario, ma ricevuto {type(data).__name__}")
    try:
        response = post_data(url, data)
        return response.json()
    except Exception as e:
        raise Exception(f"Problema con la response: {e}")
    
def post_data(URL: str, data: dict[str, any]) -> Response:
    try:
        response = post(URL, headers={"Content-Type": "application/json"}, json=data)
        response.raise_for_status()
        return response
    # .json()
    except HTTPError as e:
        r = e.response
        details = None
        if r is not None:
            try:
                details = r.json()
            except Exception:
                details = r.text
        raise HTTPError(f"{(r.status_code if r else 'N/A')} su {URL}: "
                        f"{(r.reason if r else '')} - Dettagli: {details}"
                        ) from e
    except ConnectionError as e:
        raise ConnectionError(
            f"Errore di connessione. Verifica la tua connessione internet: {e}"
        ) from e
    except Timeout as e:
        raise Timeout(
            f"Timeout della richiesta. Il server non ha risposto in tempo: {e}"
        ) from e
    except RequestException as e:
        raise RequestException(f"Errore generico nella richiesta: {e}"
        ) from e

def get_data(URL: str)-> Response:
# dict[str, any] | list[dict[str, any ]]:
    if URL is None:
        raise ValueError("URL non può essere vuoto")
    try:
        response = get(URL)
        # print(res.txt)
        # print(res.json())
        response.raise_for_status()
        return response
        # return response.json()
    except HTTPError as e:
        raise HTTPError(f"HTTP error occurred: {e}")
    except ConnectionError as e:
        raise ConnectionError(
            f"Errore di connessione. Verifica la tua connessione internet: {e}"
        ) from e
    except Timeout as e:
        raise Timeout(
            f"Timeout della richiesta. Il server non ha risposto in tempo: {e}"
        ) from e
    except RequestException as e:
        raise RequestException(f"Errore generico nella richiesta: {e}"
        ) from e

