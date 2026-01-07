from io_utils import leggi_file
from text_analyzer import conta_caratteri, frequenza_caratteri
from frontend import stampa_numero_caratteri, stampa_frequenza_caratteri

def main():
    percorso_file = "prova.txt"
    testo: str = leggi_file(percorso_file)
    numero_caratteri: int = conta_caratteri(testo)
    stampa_numero_caratteri(numero_caratteri)
    frequenza: dict = frequenza_caratteri(testo)
    stampa_frequenza_caratteri(frequenza)


    

if __name__ == "__main__":
    main()