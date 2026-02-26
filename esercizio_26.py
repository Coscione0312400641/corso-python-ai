# dato il file esercizio_dataset_csv_json.txt
# creare un csv con terne valide e aggiungere
#"se l'età è >=27, la categoria è Senior, altrimenti Junior"
#creare utenti_validi.csv,utenti_non_validi.csv e utenti.json (solo validi)

import csv
import json
'''
def validate_row(row):
    try:
        if not row["nome"].strip():
            return False,"Nome mancante"
        if not row["citta"].strip():
            return False,"Città mancante"
        eta=int(row["eta"])
        if eta <0:
            return False,"Età non valida"
        return True,None
    except KeyError as e:
        return False,e
    except ValueError as e:
        return False,e
    except Exception as e:
        return False,e
#calcolo la categoria
def calculate_category(age):
    if age < 26:
        return"Junior"
    elif age <=30:
        return "Middle"
    else:
        return "Senior"
#pipeline
try:
    with open("users.csv",newline="") as f_input:
        open("valid_users.csv","w",newline="") as f_valid_users:
        open("invalid_users.csv","w",newline="") as f_invalid_users:
        reader = csv.DictReader(f_input)
        valid_fieldnames=reader.fieldnames+["categoria"]
        invalid_fieldnames=reader.fieldnames + ["errore"]
        valid_writer=csv.DictWriter(f_valid_users, fieldnames=valid_fieldnames)
        valid_writer.writeheader()
        invalid_write.writeheader()
        for row in reader:
            is_valid,error= validate_row(row)
        if is_valid:
            eta=int(row["eta"])
            category=calculate_category(eta)
            row["category"] = category
            valid_writer.writerow(row)
            f_valid_users.append({
                "nome": row["nome"],
                "citta": row["citta"],
                "eta": row["eta"],
                "categoria": category
            })
        else:
            row["errore"]=error
            invalid_writer.writerow(row)
    except FileNotFoundError:
        print("File non esistente")
    except Exception as e:
        print(e)
    #salvataggio file json
    try:
        with open("valid_users.json","w") as f_valid_users:
            json.dump(f_valid_users, f_valid_users, indent=4)
    except Exception ad e:
        print(e)
'''
def crea_metodo_csv(file):
    validi = []
    non_validi = []

    with open(file, "r") as f:
        next(f)
        righe = f.readlines()

    with open("utenti_validi.csv", "w", newline="") as f_validi, \
         open("utenti_non_validi.csv", "w", newline="") as f_non_validi:

        colonne = ["nome", "eta", "citta", "categoria"]
        writer_validi = csv.DictWriter(f_validi, fieldnames=colonne)
        writer_validi.writeheader()

        writer_non_validi = csv.writer(f_non_validi)

        for riga in righe:
            campi = riga.strip().split(",")

            if len(campi) != 3 or not campi[1].isdigit():
                non_validi.append(campi)
                writer_non_validi.writerow(campi)
            else:
                nome, eta, citta = campi
                eta = int(eta)
                categoria = "Senior" if eta >= 27 else "Junior"

                writer_validi.writerow({
                    "nome": nome,
                    "eta": eta,
                    "citta": citta,
                    "categoria": categoria
                })

                validi.append({
                    "nome": nome,
                    "eta": eta,
                    "citta": citta,
                    "categoria": categoria
                })

    # Creo JSON solo con validi
    with open("utenti.json", "w") as f_json:
        json.dump(validi, f_json, indent=4)