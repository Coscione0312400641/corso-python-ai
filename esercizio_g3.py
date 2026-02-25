def converti(lista):
    numeri=[]
    for n in lista:
        try:
            numeri.append(int(n))
        except ValueError:
            pass
    return numeri
def filtra(lista):
    return [n for n in lista if n>10]
def somma(lista):
    return sum(lista)
def main():
    dati=["5","43","undici","15","6","80"]
    numeri=converti(dati)
    filtrati=filtra(numeri)
    risultato=somma(filtrati)
    print("Somma: ", risultato)

main()