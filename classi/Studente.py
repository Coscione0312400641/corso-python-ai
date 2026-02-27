from classi.Persona import Persona
from abc import ABC,abstractmethod
class Studente(Persona):
    def __init__(self,nome,eta,corso):
        super().__init__(nome,eta)
        self.corso=corso
    def saluta(self):
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} e studio {self.corso}"

ciccio=Studente("Ciccio",25,"Python AI")
print(ciccio.saluta())
