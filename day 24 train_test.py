import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import preprocessing

df = pd.read_csv(r"C:\letsupgrage assignment\train.csv")
df["Age"].mean()
new_age_var = np.where(df["Age"].isnull(),32,df["Age"])
df["Age"] = new_age_var
label_encoder = preprocessing.LabelEncoder()
encoded_sex = label_encoder.fit_transform(df["Age"])

tree_model = tree.DecisionTreeClassifier()
tree_model.fit(X = pd.DataFrame(encoded_sex), y = df["Survived"])

predictors = pd.DataFrame([encoded_sex, df["Age"], df["Fare"]]).T
tree_model = tree.DecisionTreeClassifier(max_depth=8)
tree_model.fit(X = predictors, y = df["Survived"])

with open("Dtree2.dot", 'w') as f:
    f = tree.export_graphviz(tree_model, feature_names = ["Sex", "Age", "Fare"], out_file=f);
print("the model accuracy")
print(tree_model.score(X = predictors, y = df["Survived"]))
