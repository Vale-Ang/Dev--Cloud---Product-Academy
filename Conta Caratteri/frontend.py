"""Stampa il numero di caratteri di un file di testo."""
def stampa_numero_caratteri(numero_caratteri: int) -> None:
    print(f"Il file contiene {numero_caratteri} caratteri.")

def stampa_frequenza_caratteri(frequenza: dict) -> None:
    print("Frequenza dei caratteri nel file:")
    for carattere, conteggio in frequenza.items():
        print(f"'{carattere}': {conteggio}")