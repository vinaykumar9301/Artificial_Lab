import pandas as pd

data = pd.read_csv(
    'https://github.com/datagy/data/raw/main/titanic.csv', 
    usecols=['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
)

data = data.dropna()

X = data.copy()

y = X.pop('Survived')
