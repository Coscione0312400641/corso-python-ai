#aggiungere una colonna "categoria"
"se l'età è >=27, la categoria è Senior, altrimenti Junior"
import csv
nomi_completi=[]
with open("data.txt",'r') as f:
    next(f)
    righe=f.readlines()
    #nomi_completi.append(nomi)
    with open("dati.csv","w",newline='') as csvfile:
        #reader = csv.DictReader(f_input)
        #utenti_modificati=[]
        colonne=["nome","eta","citta","categoria"]
        writer=csv.DictWriter(csvfile,fieldnames=colonne)
        writer.writeheader()
        for riga in righe:
            nome,eta,citta=riga.strip().split(",")
            #eta = int(row["eta"])
            eta=int(eta)
            if eta>=27:
                categoria="Senior"
            else:
                categoria="Junior"
            #row["categori"]=categoria
            #utenti_modificati.append(row)
            writer.writerow({
                "nome":nome,
                "eta":eta,
                "citta":citta,
               "categoria":categoria
            })
    f.close()
'''
    with open("dati_nuovi.csv","w",newline='') as f_output:
        colonne=["nome","eta","citta","categoria"]
        writer=csv.DictWriter(f_output,fieldnames=colonne)
        
'''
