#età,reddito annuo, numero debiti e punteggio credito #approvazione
#label dirà se il prestito può essere erogato sarà 0 se non approvato, 1 altrimenti
import numpy as np
np.random.seed(42)
dataset=np.array([
    [25,30000,2,650,1],
    [45,80000,1,720,1],
    [35,50000,5,580,0],
    [23,25000,3,600,0],
    [52,120000,0,800,1],
    [40,70000,4,610,0]

])
x=dataset[:,:-1]#tutte le colonne tranne l'ultima
y=dataset[:,-1]
minimo=np.min(x,axis=0)
maximo=np.max(x,axis=0)
x_norm=(x-minimo)/(maximo-minimo)
print(x_norm)
#rapporto di debiti su reddito
reddito=x[:,1]
debito=x[:,2]
rapporto_debiti=debito/reddito
print(rapporto_debiti)
rapporto_debiti=rapporto_debiti.reshape(-1,1)
print(rapporto_debiti)
X_enhanced=np.hstack((x_norm,rapporto_debiti))
print(X_enhanced)
indices=np.arange(len(X_enhanced))
print(indices)
np.random.shuffle(indices)
train_size=int(len(indices)*0.8)
train_idx=indices[:train_size]
test_idx=indices[train_size:]
X_train=X_enhanced[train_idx]
y_train=y[train_idx]
X_test=X_enhanced[test_idx]
y_test=y[test_idx]
print(y_train)
print(y_test)
