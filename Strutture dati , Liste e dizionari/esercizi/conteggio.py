voti: list[str] = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
conteggio: dict[str, int] = {}
for voto in voti:
    conteggio[voto] = conteggio.get(voto, 0) + 1
print(conteggio)