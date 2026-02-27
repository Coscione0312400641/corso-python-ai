import json
from classi.ESERCITAZIONE.Richiesta import Richiesta
from classi.ESERCITAZIONE.Validator import Validator
import Pipeline
class Pipeline():
    def __init__(self,file_csv):
        self._file_csv=file_csv
        self._validator=Validator()
        self._richieste_valide=[]
        self._servizi_unici= set()
        self._conteggio_servizi= {}
    def esegui(self):
        richieste_valide=Richiesta.validare(self._file_csv)
        for r in richieste_valide:
            if self._validator.validare(r):
                self._richieste_valide.append(r)
                # set dei servizi unici
                self._servizi_unici.add(r.servizio)
                # conteggio richieste per servizio
                if r.servizio not in self._conteggio_servizi:
                    self._conteggio_servizi[r.servizio] = 1
                else:
                    self._conteggio_servizi[r.servizio] += 1

         #   print(r._dict)

    def salva_json(self, output_file="output.json"):
        data = {
            "totale_richieste": len(self._richieste_valide),
            "servizi_unici": list(self._servizi_unici),
            "conteggio_servizi": self._conteggio_servizi,
            "richieste": [
                {
                    "id": r.id,
                    "nome": r.nome,
                    "email": r.email,
                    "eta": r.eta,
                    "servizio": r.servizio,
                    "categoria": r.categoria
                } for r in self._richieste_valide
            ]
        }
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        # prova di stampa in formato JSON leggibile
        print(json.dumps(data, indent=4))
        print(f"File '{output_file}' salvato correttamente!")