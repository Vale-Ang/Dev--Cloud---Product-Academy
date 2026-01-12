"""
class Formina:
    def __init__(self, nome_forma: str):
        self.forma = nome_forma




biscotto1 = Formina("Stellina")
biscotto2 = Formina("Cuoricino")

print(biscotto1.forma)  
print(biscotto2.forma)
"""

class Persona:
    def __init__(self, nome: str, cognome: str, isEgemonyPartecipant: bool):
        self.nome = nome
        self.cognome = cognome
        self.isEgemonyPartecipant = isEgemonyPartecipant

    # def printNome(self):
    #     print(self.nome)

    def printIsEgemonyPartecipant(self):
        print(f"{self.nome} {self.cognome}: {self.isEgemonyPartecipant}")

class Corso:
    def __init__(self, nome):
        self.nome = nome
        self.partecipants = []
    
    def addPartecipant(self, p: Persona)-> bool:
        if p.isEgemonyPartecipant:
            self.partecipants.append(f"{p.nome} {p.cognome}")
            return True
        else:
            return False


persona1 = Persona("Claudia", "Nigro", True)
persona2 = Persona("Valeria", "Angioj", True)
persona3 = Persona("Maria", "Rossi", False)

ar = [persona1, persona2, persona3]

for persona in ar:
    persona.printIsEgemonyPartecipant()
    # print(f"{persona.nome} {persona.cognome}: {persona.isEgemonyPartecipant}")