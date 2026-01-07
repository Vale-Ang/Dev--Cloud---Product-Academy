from matematica.operazioni import somma

def sommatoria (a: int, b: int, c: int) -> int:
    """Calcola la sommatoria di tre numeri usando la funzione somma del modulo operazioni"""
    return somma(somma(a, b), c)