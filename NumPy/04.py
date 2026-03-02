import random
import numpy as np
#5 persone con 4 feature
#età,altezza,peso,punteggio
dataset=np.random.randint(0,100,(5,4))
print(dataset)
dataset_originale=dataset.copy()
features_ds=dataset[:,1:]
print(features_ds)
minimo=np.min(features_ds,axis=0)
massimo=np.max(features_ds,axis=0)
features_norm=(features_ds-minimo)/(massimo-minimo)
print(features_norm)
print(features_ds)
print(dataset)
dataset[:,1:]=features_norm
print(dataset)
media_feature=np.mean(dataset[:,1:],axis=0)
media_feature=media_feature.reshape(-1,1)
print(media_feature)
dataset_con_media=np.random.uniform((dataset,media_feature))
print(dataset_con_media)
features_ds=dataset[:,1:]
print(features_ds)
