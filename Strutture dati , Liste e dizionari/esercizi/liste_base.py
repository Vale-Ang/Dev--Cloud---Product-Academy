lista : list [str] = ["web01", "db01", "cache01"]
lista.append("backup01")
lista.insert(0, "proxy01")
indice_deleted = lista.index("cache01")
lista.pop(indice_deleted)
print (lista)
print (f" Numero server: {len(lista)}")