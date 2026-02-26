import csv
import json
with open("utenti.json", "r") as f_in:
    utenti = json.load(f_in)
    print(type(utenti))

    for u in utenti:
        eta = u["eta"]
        print(type(eta))

        if eta > 27:
            u["categoria"] = "Senior"
        else:
            u["categoria"] = "Junior"

    print(utenti)

with open("utenti_classificati.json", "w") as f_out:
    json.dump(utenti, f_out, indent=4)