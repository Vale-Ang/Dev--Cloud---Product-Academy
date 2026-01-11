# ===========================
# UI
# ===========================

"""Stampa il risultato delle operzioni di calcolo caratteri etc."""
def print_risultato(value: int, spec: str) -> None:
    if value is None:
        raise ValueError(f"{value} è obbligatorio (non può essere None)")
    if not isinstance(value,(int)):
        raise TypeError(f"{value} deve essere un numero")
    
    print('*'*30)
    print(f"Il numero si {spec} è {value }") 
    print('*'*30)