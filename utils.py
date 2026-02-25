
def somma(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Argument must be a integer')
    return a+b
def moltiplicazione(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Argument must be a integer')
    return a*b

def sottrazione(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Argument must be a integer')
    return a-b

def divisione(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Argument must be a integer')
    if b==0:
        raise ZeroDivisionError("il divisore non può essere 0")
    return a/b
def converti_in_maiuscolo(string):
    if not isinstance(string,str):
        raise TypeError('Argument must be a string')
    return string.upper()
#funzioni di somma,sottrazione,moltiplicazione,divisione