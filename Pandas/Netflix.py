import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("NetFlix.csv")
feature_text = ["director", "cast", "genres", "description"]

df[feature_text] = df[feature_text].fillna("")

df["combined_text"] = df[feature_text].agg(" ".join, axis=1)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["combined_text"])

print(tfidf_matrix.shape)
model = NearestNeighbors(metric="cosine", algorithm="brute")
model.fit(tfidf_matrix)


def recommend_by_title(title: str, k: int = 10, same_genre: bool = False) -> pd.DataFrame:
    # Verifica colonna title minuscolo
    df["title"] = df["title"].str.lower()
    title = title.lower()

    seed = df[df["title"] == title]
    if seed.empty:
        raise ValueError("Title not found in dataset")

    idx = seed.index[0]

    distances, indices = model.kneighbors(tfidf_matrix[idx], n_neighbors=k + 1)

    recs = df.iloc[indices[0]].copy()

    # Rimuove il film seed
    recs = recs[recs["title"] != title]

    # Filtra per stesso genere se richiesto
    if same_genre:
        recs = recs[recs["genres"] == seed.iloc[0]["genres"]]

    return recs[["title", "director", "cast", "genres"]].head(k)
    distances,indices=model.kneighbors(tfidf_matrix[idx],n_neighbors=k+1)
    recs=df.iloc[indices[0]].copy()
    recs[recs[recs["title"]]!=title]
    return recs[["title","director", "genres", "descriptions"]].head(k)

print(recommend_by_title("The Hobbit", k=5))