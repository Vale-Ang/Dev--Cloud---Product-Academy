from io_utils import leggi_file

def conta_caratteri(testo: str) -> int:
    numero_caratteri = len(testo)
    return numero_caratteri

def frequenza_caratteri(testo: str) -> dict:
    frequenza = {}
    for carattere in testo:
        if carattere in frequenza:
            frequenza[carattere] += 1
        else:
            frequenza[carattere] = 1
    return frequenza