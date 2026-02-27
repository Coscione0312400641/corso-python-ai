import csv
from abc import ABC,abstractmethod,abstractclassmethod


class Richiesta(ABC):
    def __init__(self,id, nome, email, eta, servizio):
        self.id = id
        self.nome = nome
        self.email = email
        self.eta = eta
        self.servizio = servizio
        self.categoria = None
    @classmethod

    def validare(self,file):
        lista = []
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                nome_corretto = row['nome'].strip().lower().title()
                mail_corretta = row['email'] if '@' in row['email'] else ""
                age = int(row['eta']) if row['eta'].isdigit() else 0

                if age >= 18 and age < 25:
                    categoria = "Junior"
                elif age >= 25 and age < 40:
                    categoria = "Adult"
                else:
                    categoria = "Senior"
                if nome_corretto != "" and mail_corretta != "" and age != 0 and age >= 18:
                    r = self(row['id'], nome_corretto, mail_corretta, age, row['servizio'])
                    r.categoria = categoria
                    lista.append(r)
                    #lista.append((row['id'], nome_corretto, mail_corretta, row['eta'], row['servizio'], categoria))
        return lista

richieste_valide=(Richiesta.validare("requests.csv"))
for r in richieste_valide:
    print(r)
'''
Un'azienda raccoglie richieste clienti tramite CSV (requests.csv).

Obiettivi:

1. Leggere il file CSV
2. Validare i dati

	Regole:

	- email deve contenere "@"
	- età deve essere >= 18
	- nome non deve essere vuoto

	Se una riga non è valida deve essere scartata.

3. Sanificare i dati (rimuovere spazi superflui, capitalizzazioni errate ecc.)

4. Aggiungere campo "categoria_eta":

	18–25 → "Junior"
	26–40 → "Adult"
	40 → "Senior"

5. Organizzare i dati

	- lista richieste valide
	- set servizi unici richiesti
	- dizionario conteggio richieste per servizio

6. Creare:

	- Classe Richiesta
	- Classe Validator
	- Classe Pipeline

7. Salvare output JSON

File: output.json

Struttura:

{
  "totale_richieste": X,
  "servizi_unici": [...],
  "conteggio_servizi": {...},
  "richieste": [...]
}


'''