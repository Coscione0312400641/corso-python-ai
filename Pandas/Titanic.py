import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt

pd.options.display.max_columns = 8
pd.options.display.max_rows = 100

# ======================
# 1️⃣ CARICAMENTO DATI
# ======================
df = pd.read_csv('TitanicDataset.csv')

print(df['Survived'].value_counts())
print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Survived"].mean())
print(df[df['Survived'] == 1]['Age'].mean())
print(df[df['Pclass'] == 1]['Age'].mean())
print(df.groupby('Pclass')["Fare"].max())
print(df.head())
print(df.info())

# ======================
# 2️⃣ GRAFICO PRIMA DEL GET_DUMMIES
# ======================
survived_by_sex = df.groupby("Sex")["Survived"].mean() * 100

plt.figure(figsize=(6,4))
plt.bar(survived_by_sex.index, survived_by_sex.values, color=["pink","steelblue"])
plt.title("Sopravvivenza sul Titanic per sesso")
plt.ylabel("Percentuale (%)")
plt.ylim(0,100)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()

# ======================
# 3️⃣ FEATURE ENGINEERING
# ======================
df["IsMaleChild"] = 0
df.loc[df["Name"].str.contains("Master"), "IsMaleChild"] = 1

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = 0
df.loc[df["FamilySize"] == 1, "IsAlone"] = 1

df["Age0015"] = 0
df["Age1540"] = 0
df["Age4080"] = 0

df.loc[(df["Age"] > 0) & (df["Age"] <= 15), "Age0015"] = 1
df.loc[(df["Age"] > 15) & (df["Age"] <= 40), "Age1540"] = 1
df.loc[df["Age"] > 40, "Age4080"] = 1

df = df.drop(["PassengerId", "Name", "Cabin", "Ticket", "Fare", "SibSp", "Parch", "Age"], axis=1)

df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

print(df.info())
print(df.isnull().sum())

# ======================
# 4️⃣ TRAIN / TEST SPLIT
# ======================
X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ======================
# 5️⃣ MODELLO
# ======================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Coefficienti
print("\nCoefficienti modello:")
for feature, coef in zip(X.columns, model.coef_[0]):
    print(feature, coef)

# ======================
# 6️⃣ VALUTAZIONE
# ======================
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

train_accuracy = accuracy_score(y_train, model.predict(X_train))
test_accuracy = accuracy_score(y_test, y_pred)

print("Train Accuracy:", train_accuracy)
print("Test Accuracy:", test_accuracy)

# ======================
# 7️⃣ PREDIZIONI PERSONALIZZATE
# ======================
jack = {
    "Pclass": 3,
    "IsMaleChild": 0,
    "FamilySize": 1,
    "IsAlone": 1,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Sex_male": 1,
    "Embarked_Q": 0,
    "Embarked_S": 1,
}

rose = {
    "Pclass": 1,
    "IsMaleChild": 0,
    "FamilySize": 2,
    "IsAlone": 0,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Sex_male": 0,
    "Embarked_Q": 0,
    "Embarked_S": 1,
}

vince = {
    "Pclass": 2,
    "IsMaleChild": 0,
    "FamilySize": 4,
    "IsAlone": 0,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Sex_male": 1,
    "Embarked_Q": 0,
    "Embarked_S": 0,
}

characters = pd.DataFrame([jack, rose, vince], index=["jack", "rose", "vince"])
characters = characters.reindex(columns=X.columns, fill_value=0)

pred_class = model.predict(characters)
pred_proba = model.predict_proba(characters)[:, 1]

results = pd.DataFrame({
    "Predicted Survived": pred_class,
    "Predicted Probability": pred_proba
}, index=characters.index)

print("\nPredizioni personaggi:")
print(results)