try:
    numero_1=int(input("Inserisci un numero: "))
    numero_2 = int(input("Inserisci un altro numero: "))
    print("Risultato: ",numero_1/numero_2)
except ValueError:
    print("Errore: il numero non è un numero")
except ZeroDivisionError:
    print("Non puoi dividere per zero")
else:
    print("Divisione eseguita con successo")
finally:
    print("Qualsiasi cosa succeda, io vengo eseguito!")