import pandas as pd
dati={
    "nome":["Ciccio","anna "," Marcello","Francesca","PAOLO"],
    "email": ["cicciol@email.it","anna@email.com","marcello@redyard.com ","francesca@email.com","paolo@paolo.it"],
    "eta":[25,22,38,20,21],
    "stipendio":[1200,1800,1900,2100,1750],
    "citta":["Roma","Milano","Firenze","Roma","Roma"],
    "categoria": ["A","A","B","A","B"],
    "vendite": [240,250,190,310,370]
}
df=pd.DataFrame(dati)
print(df)
print(df.isnull().sum())
print(df.info())
print(df.describe())
print(df.dropna())
#pulizia del nome
df["nome"]=df["nome"].str.strip().str.title()
#pulizia della media
df["email"]=df["email"].str.strip().str.title()
print(df)
#media_eta=df["eta"].mean()
#df["eta"]=df["eta"].fillna(media_eta)
media_stipendio=df["stipendio"].mean()
#df["eta"]=df["eta"].fillna(df["eta"].mean())
#df["stipendio"]=df["stipendio"].fillna(df["stipendio"].mean())
df=df.dropna(subset=["email"])
#pulizia e popolamento dell'età con la media
df=df[df["email"].str.contains("@")]
df["eta"]=pd.to_numeric(df["eta"],errors="coerce")
df=df.dropna(subset=["eta"])
df["eta"]=df["eta"].astype(int)
#popolamento dello stipendio con la media
df["stipendio"]=df["stipendio"].fillna(media_stipendio)
print(df.info())
#raggruppare vendite per città
print(df.groupby("citta")["vendite"].sum().mean())
print(df.groupby(["categoria","citta"])["vendite"].sum())