from repository import get_file

def leggi_file(percorso: str) -> str:
    with get_file(percorso) as file:
        return file.read()