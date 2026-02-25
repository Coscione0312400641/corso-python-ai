studente={
    "nome":"Anna",
    "eta":22,
    "corso":"Python"
}
num=[10,20,30]
num_d ={
    "a":10,
    "b":20,
    "c":30
}
quadrati={}
for n in num:
    quadrati[n]=n*n
print(quadrati)
quadrati_c={n:n*n for n in num}
print(quadrati_c)
'''
 {chiave:valore for elemento in sequenza}
'''
#