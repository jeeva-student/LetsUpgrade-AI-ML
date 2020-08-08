import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import preprocessing

df = pd.read_excel(r"C:\letsupgrage assignment\Bank_Personal_Loan_Modelling.xlsx", sheet_name=1)
df.info()

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=1000, max_features=2, oob_score=True)
features = ["Age", "Experience", "Income", "Family",
            "CCAvg", "Education", "Mortgage", "Securities Account",
            "CD Account", "Online", "CreditCard"]
rf_model.fit(X=df[features], y=df["Personal Loan"])
print("\n oob accuracy:")
print(rf_model.oob_score_);
print("\n")
for features, imp in zip(features, rf_model.feature_importances_):
    print(features, imp);
    
predictors = pd.DataFrame([df["Income"], df["Family"], df["CCAvg"],
                          df["Education"]]).T

tree_model = tree.DecisionTreeClassifier(max_depth=12)
tree_model.fit(X = predictors, y = df["Personal Loan"])

#with open("Dtree3.dot", 'w')as f:
 #   f = tree.export_graphviz(tree_model, feature_names=["Income", "Family",
  #                                                      "CCAvg", "Education"], out_file=f);
    
print("\n the accuracy of the model")
print(tree_model.score(X = predictors, y = df["Personal Loan"]))
