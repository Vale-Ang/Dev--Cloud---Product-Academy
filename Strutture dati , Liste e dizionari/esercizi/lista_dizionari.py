prodotti: list[dict[str, str | float | int]] = [
    {
        "nome": "Laptop",
        "prezzo": 899.99,
        "quantità": 5
    },
    {
        "nome": "Mouse",
        "prezzo": 25.50,
        "quantità": 50
    },
    {
        "nome": "Tastiera",
        "prezzo": 75.00,
        "quantità": 30
    },
    {
        "nome": "Monitor",
        "prezzo": 299.99,
        "quantità": 15
    }
]
print("Prodotti > 100€:")
for prodotto in prodotti:
    if prodotto["prezzo"] > 100:
        print(f"- Prodotto: {prodotto['nome']}, Prezzo: {prodotto['prezzo']}")
print("\nValore totale inventario per prodotto:")
valore_totale_inventario: float = 0.0
for prodotto in prodotti:
    valore_totale_per_prodotto = prodotto["prezzo"] * prodotto["quantità"]
    print(valore_totale_per_prodotto)
    valore_totale_inventario += valore_totale_per_prodotto
    print(valore_totale_inventario)
print(f"Valore totale inventario: €{valore_totale_inventario :.2f}")