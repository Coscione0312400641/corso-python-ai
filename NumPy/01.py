import numpy as np
#età,altezza e peso
dati=np.array([
    [34,167,89],
    [37,185,23],
    [22,173,65]
])
eta=(dati[:,0])
media=np.mean(dati,axis=0) #axis=1 per media sulle righe
print(media)
print(type(dati))
punteggi = np.array([23,46,78,56,98,34,65,32,67,45])
media = np.mean(punteggi)
print(media)

sopra_media = punteggi > media
numero_sopra_media = np.sum(sopra_media)
pc = (numero_sopra_media / len(punteggi)) * 100
print(pc)

minimo = np.min(punteggi)
massimo = np.max(punteggi)
normalizzati = (punteggi - minimo) / (massimo - minimo)
print(normalizzati)

print(sopra_media)
#numeri=[1,2,3,4]
#voglio moltiplicare tutto per 2
#nuovi=[n*2 for n in numeri]
'''
#con NumPy
array=np.array(numeri)
nuovi=array*2
print(nuovi)
numeri_random=np.random.randint(1,101,10)
print(np.mean(numeri_random))
print(np.max(numeri_random))
print(numeri_random*3)
print(numeri_random[numeri_random]>50)#filtro

#array numerico casuale tra 1 e 100, calcolare media e massimo, moltiplica *3 e filtrare i numeri maggiori di 50
#oppure
#for n in numeri:
 #   numeri.append(n*2)

 #numeri_random=np.random.randint(1,101,10)
 #print(numeri_random)
 #.mean media , .max -> il valore massimo

'''