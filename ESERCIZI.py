numeri=[3,6,9,12,15,18,21,24,27,30]
#creare un dizionario chiave->numero,valore->numero/3

divisibili_per_3={n:n/3 for n in numeri}
print(divisibili_per_3)

nomi=["Anna","Ciccio","Francesca","Annibale"]
#creare un dizionario chiave->nome,valore->"Lungo se la lunghezza è >5 else "Corto"
lunghezza={nome:"Lungo" if len(nome)>5 else "Corto" for nome in nomi}
print(lunghezza)

interi_corretti=[]
'''
scrivere una pipeline che (funzioni,try,catch,list comprehension)
riceve una lista di stringhe numeri ["23"...]
li converte in interi, gestendo gli errori
restituisce solo i >10
calcola la somma
4 funzioni (ricevere stringhe,quella che li converte, quelli che fa la somma, quelli maggiori di 10)

except:
    pass
'''
numeri_stringhe=["20","60","18","7","1","30","10"]
def ricevi_stringhe(numeri_stringhe):
    for num in numeri_stringhe:
        if not isinstance(num, str):
            raise TypeError('Argument must be a String')
    return numeri_stringhe
print(ricevi_stringhe(numeri_stringhe))
def controllo(numeri_stringhe):
    return [int(num) for num in numeri_stringhe]

print(controllo(interi_corretti))
da_sommare=[]
def maggiori_di_10(interi_corretti):
    return [num for num in interi_corretti if num>10]
print(maggiori_di_10(interi_corretti))
def sommatoria(da_sommare):
    return sum(da_sommare)

stringhe=ricevi_stringhe(numeri_stringhe)
interi=controllo(stringhe)
filtrati=maggiori_di_10(interi)
totale=sommatoria(filtrati)

print("Interi: ",interi)
print("Maggiori di 10: ",filtrati)
print("Somma: ",totale)