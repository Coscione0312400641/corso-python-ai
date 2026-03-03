import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
pd.options.display.max_columns = 8
pd.options.display.max_rows = 100
df=pd.read_csv('TitanicDataset.csv')
survived=df['Survived'].value_counts()
print(survived)
survived_by_sex=df.groupby("Sex")["Survived"].mean()
print(survived_by_sex)
survived_by_class=df.groupby("Pclass")["Survived"].mean()
print(survived_by_class)
avg_age_survived=df[df['Survived']==1]['Age'].mean()
print(avg_age_survived)
avg_age_survived=df[df['Pclass']==1]['Age'].mean()
print(avg_age_survived)
print(df.groupby('Pclass')["Fare"].max())
print(df.head())
print(df.info())
df=df.drop(["PassengerId","Name","Cabin","Ticket"],axis=1)
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.info())
print(df.isnull().sum())
X=df.drop(["Survived"],axis=1)
y=df["Survived"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train)
print(X_test)
print(y_train)
print(y_test)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
