from requests import get, exceptions


def get_data(URL: str)-> dict[str, any] | list[dict[str, any]]:
    if URL is None:
        raise ValueError("URL non può essere vuoto")
    
    try:
        response = get(URL)
        # print(res.txt)
        # print(res.json())
        response.raise_for_status()
        return response.json()
    except exceptions.HTTPError as e:
        # TODO: correggere exception
        raise exceptions.HTTPError(f"HTTP error occurred: {e}")
    except exceptions.ConnectionError as e:
        raise exceptions.ConnectionError(
            f"Errore di connessione. Verifica la tua connessione internet: {e}"
        ) from e
    except exceptions.Timeout as e:
        raise exceptions.Timeout(
            f"Timeout della richiesta. Il server non ha risposto in tempo: {e}"
        ) from e
    except exceptions.RequestException as e:
        raise exceptions.RequestException(f"Errore generico nella richiesta: {e}"
        ) from e

