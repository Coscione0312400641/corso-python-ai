# This is a sample Python script.
import utils
from classi.LLMRequest import LLMRequest

request=LLMRequest("Di che colore è il cielo?")
request._prompt="Prompt cambiato"
with open("data.txt","r") as f:
    nomi=f.readlines()
print(nomi)
nomi_puliti=[]
#nomi_puliti=[f.strip().title().replace("\n","")for r in f.readlines()]
for n in nomi:
    nome=n.strip()
    nome=nome.title()
    nome=nome.replace("\n","")
    nomi_puliti.append(nome)
print(nomi_puliti)
with open("dati_puliti.txt","w") as f:
    for nome in nomi_puliti:
        f.write(nome+"\n")
        #f.write("\n".join(nomi_puliti))
#with open("data.txt","w") as f:
#    f.write("Parole")
#with open("data.txt","a") as f:
#    f.write("Aggiungere")
#for line in contenuto:
#    print(line)
#f=open("data.txt","r")
#print(f.read())
f.close()
'''
r->lettura
w->scrittura e sovrascrittura
a->append
r+->lettura + scrittura

apertura file->trasformazione -> nuovo file
'''
a=0
b=1
# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print(utils.converti_in_maiuscolo('hello world'))
print(utils.somma(a,b))
print(utils.sottrazione(a,b))
print(utils.moltiplicazione(a,b))
print(utils.divisione(a,b))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
numeri=[1,2,3,4]
quadrati=[numero**2 for numero in numeri]
#[trasformazione for elemento in elementi]
print(quadrati)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
