import csv
prodotti=[
    {"id":1,"nome":"PC","prezzo":999.00},
    {"id": 2, "nome": "Monitor", "prezzo": 699.00},
    {"id": 3, "nome": "Mouse", "prezzo": 99.00},
    {"id": 4, "nome": "Tastiera", "prezzo": 129.00}
]
with open("dati.csv","w",newline='') as csvfile:
    colonne=["id","nome","prezzo"]
    writer=csv.DictWriter(csvfile,fieldnames=colonne)
    writer.writeheader()
    for p in prodotti:
        writer.writerow(p)
        #indice={p["id"]:p for p in prodotti}
#print(indice)