import pandas as pd
dati={
    "settore":["Tech","Retail","Finance","Tech","Tech","Retail","Finance"],
    "dipendenti":[50,70,30,90,80,75,20],
    "fatturato":[50000,60000,33000,20000,90000,85000,18000],

}
df=pd.DataFrame(dati)
#fatturato medio per settore
print(df.groupby("settore")["fatturato"].mean())
#numero totale di dipendenti per settore
print(df.groupby("settore")["dipendenti"].sum())
#settore con massimo fatturato totale
totali=df.groupby("settore")["fatturato"].sum()
print(totali.idxmin())
print(totali.idxmax())