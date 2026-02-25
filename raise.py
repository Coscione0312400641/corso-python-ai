from ErroreCustom import ErroreCustom


def dividi(a,b):
    if b==7:
        raise ErroreCustom
    return a/b
try:
    print(dividi(1,7))
except ErroreCustom as e:
    print("Non mi piace il 7, prova un altro numero")