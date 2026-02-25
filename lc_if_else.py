numeri=[1,2,3,4,5,6,7,8,9]
#[A if condizione else B for elemento in sequenza]
risultato=["pari" if numero %2==0 else "dispari" for numero in numeri]
print(risultato)