#creare una nuova lista solo con i numeri >10 e %2
numeri=[5,12,26,30,20,9,14,209]
nuova_lista=[]
for i in numeri:
    if i>10:
        nuova_lista.append(i/2)
print(nuova_lista)