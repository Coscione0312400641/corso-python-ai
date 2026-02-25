numeri=[3,6,9,12,15,18,21,24,27,30]
#creare un dizionario chiave->numero,valore->numero/3

divisibili_per_3={n:n/3 for n in numeri}
print(divisibili_per_3)

nomi=["Anna","Ciccio","Francesca","Annibale"]
#creare un dizionario chiave->nome,valore->"Lungo se la lunghezza è >5 else "Corto"
lunghezza={nome:"Lungo" if len(nome)>5 else "Corto" for nome in nomi}
print(lunghezza)