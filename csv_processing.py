import csv
with open("dati.csv",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    writer=csv.writer(csvfile)
    writer.writerows(["nome","eta","citta"])
    #colonne=["nome","eta","citta"]
   #writer.writeHeader()
    '''
    writer.writerow({["nome":"Mimmo","eta":22,"citta":"Roma"]})
    '''
   # writer.csv.DictWriter(csvfile,fieldnames=colonne)
    writer.writerows(["Ciccio","19","Ancona"])
    dataset=[]
    for riga in reader:
        print(riga)
        dataset.append(riga)
    print(dataset)