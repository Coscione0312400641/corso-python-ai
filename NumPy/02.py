import numpy as np

studenti=np.array([
    [80,79,90],
    [60,75,90],
    [88,93,90],
    [55,60,70]
])
'''
ogni riga è uno studente , ogni colonna è il voto di una materia
trova media per studente, media per materia , 
studenti con media >75 e normalizzare il dataset
'''
media_studente=np.mean(studenti,axis=1)
media_materia=np.mean(studenti,axis=0)
medie_superiori=media_studente>75
studenti_sopra_75=studenti[medie_superiori]
minimo=np.min(studenti)
massimo=np.max(studenti)
normalizzazione=(studenti-minimo)/(massimo-minimo)
print(media_studente)
print(media_materia)
print(medie_superiori)
print(minimo)
print(massimo)
print(normalizzazione)
print(studenti_sopra_75)
