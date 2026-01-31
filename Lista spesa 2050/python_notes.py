"""
- input -> programma -> output
Programma per fare la Spesa nel 2050.
Obiettivo: Creare un programma che simuli una spesa al supermercato. 
Il programma deve gestire una Lista della Spesa (ciò che devi comprare) e un Carrello (ciò che stai prendendo).
Scenario: Siamo nel 2050. I carrelli del supermercato sono robotizzati. 
Per evitare sprechi, il carrello si rifiuta di aprirsi se cerchi di inserire un prodotto che non è nella tua lista della spesa digitale.

-Passi:
1. prendi i prodotti da carrello (interagisci con l'utente) (input) -> if / else per controllare input -> output
2. - prendi i prodotti della lista della spesa

-- Cosa mi serve
- input 
    - perché voglio prendere i prodotti dal carrello
- lista della spesa
- lista prodotti nel carrello
- if / else
    - input è vuoto?
    - caratteri piccoli
    - controllo che il prodotto sia nella lista della spesa
    - controllo che il prodotto non sia già stato inserito nel carrello
    - se il prodotto passa i controlli aggiungi prodotto alla lista del carrello
    - altrimenti restituisci errore e poi input
- if / else
    - se la lista della spesa == alla lista prodotti nel carrello allora procedi al pagamento
        - tutti i prodotti sono stati presi?
        - controllo con un ciclo quali sono i prodotti che mancano
    - altrimenti riproponi input con messaggio dei prodotti che mancano
"""