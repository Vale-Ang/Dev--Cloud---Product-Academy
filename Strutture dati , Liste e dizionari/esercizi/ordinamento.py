prezzi : list [float] = [45.5, 12.0, 78.3, 23.1, 56.7]
print(f"Prezzi originali: {prezzi}")
prezzi_ordinati = sorted(prezzi)
print(f"Prezzi ordinati: {prezzi_ordinati}")
print(f"Minimo: {prezzi_ordinati[0]}")
# print(min(prezzi))
print(f"Massimo: {prezzi_ordinati[len(prezzi_ordinati)-1]}")
# print(max(prezzi))
indice = prezzi.index(23.1)
if (indice > 0 & indice < len(prezzi)):
    print (f"23.1 presente: {True}")
else:
    print (f"23.1 presente: {False}")
contatore :int = 0
for x in prezzi:
    if (x > 50):
        contatore += 1
print (f"Prezzi > 50: {contatore}")
#print(sum(1 for p in prezzi if p > 50))