import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt;
data=pd.read_csv("https://github.com/datagy/data/raw/main/titanic.csv",usecols=['Survived','Pclass','Age','SibSp','Fare'])
data=data.dropna()
X=data.copy();
y=X.pop("Survived")
from sklearn.model_selection import train_test_split
X_train, X_Test, y_train ,y_test = train_test_split(X,y,random_state=100)
from sklearn.tree import DecisionTreeClassifier
DecisionTreeClassifier(
    criterion='gini', 
    splitter='best', 
    max_depth=None, 
    min_samples_split=2, 
    min_samples_leaf=1, 
    min_weight_fraction_leaf=0.0, 
    max_features=None, 
    random_state=None, 
    max_leaf_nodes=None, 
    min_impurity_decrease=0.0, 
    class_weight=None, 
    ccp_alpha=0.0
)
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_Test)
print(predictions[:5])