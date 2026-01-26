from requests import get
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException    
 

def get_data(URL: str)-> dict[str, any] | list[dict[str, any]]:
    if URL is None:
        raise ValueError("URL non può essere vuoto")
    
    try:
        response = get(URL)
        # print(res.txt)
        # print(res.json())
        response.raise_for_status()
        return response.json()
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

