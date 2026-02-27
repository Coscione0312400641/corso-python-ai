import csv

from classi.ESERCITAZIONE.Richiesta import Richiesta


class Validator:
    def validare(self,richiesta):
        try:
            if not richiesta.nome or richiesta.nome.strip() == "":
                return False
            if '@' not in richiesta.email:
                return False
            if richiesta.eta < 18:

                return False
            return True
        except Exception as e:
            print(f"Errore nella validazione di {richiesta.id}: {e}")
            return False

v=Validator()
