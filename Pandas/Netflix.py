import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

pd.options.display.max_columns = 20

df = pd.read_csv("NetFlix.csv")

print("Righe totali:", len(df))
missing_values = df.isnull().sum()
print(missing_values)

feature_text = ["director", "cast", "description"]

df["genres"] = df["genres"].fillna("Unknown")
df[feature_text] = df[feature_text].fillna("")

df["combined_text"] = (
        df["director"] + " " +
        df["cast"] + " " +
        df["description"] + " " +
        df["genres"]
)

X = df["combined_text"]

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(X)

print(tfidf_matrix.shape)
model = NearestNeighbors(metric="cosine", algorithm="brute")
model.fit(tfidf_matrix)