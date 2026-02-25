numeri=[5,12,7,20,3,18]
'''
crea lista che divida per 2 i numeri maggiori di 10
e lasci invariati gli altri
'''
nuova_lista=[numero/2 if numero>10 else numero for numero in numeri]
print(nuova_lista)