import pandas as pd

data = pd.read_csv(
    "https://github.com/datagy/data/raw/main/titanic.csv", 
    usecols=['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Fare', 'Embarked']
)

data = data.dropna()

print(data.head())
