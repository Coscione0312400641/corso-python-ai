temperature=[18,22,30,12,15,32,27,19,28,20]
massime=[]
#creare una nuova lista con le temperature superiori a 20
def superiori_a_venti(temperature):
    for minima in range(len(temperature)):
        if temperature[minima] > 20:
            massime.append(temperature[minima])
    print(massime)
superiori_a_venti(temperature)
