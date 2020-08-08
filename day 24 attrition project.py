import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import preprocessing

df = pd.read_excel(r"C:\letsupgrage assignment\general data.xlsx", sheet_name=0)
from sklearn.ensemble import RandomForestClassifier
label_encoder = preprocessing.LabelEncoder()
df["BusinessTravel"] = label_encoder.fit_transform(df["BusinessTravel"])
df["Department"] = label_encoder.fit_transform(df["Department"])
df["EducationField"] = label_encoder.fit_transform(df["EducationField"])
df["Gender"] = label_encoder.fit_transform(df["Gender"])
df["JobRole"] = label_encoder.fit_transform(df["JobRole"])
df["MaritalStatus"] = label_encoder.fit_transform(df["MaritalStatus"])
df["Over18"] = label_encoder.fit_transform(df["Over18"])

rf_model = RandomForestClassifier(n_estimators=1000, max_features=2, oob_score=True)
features = ["Age", "BusinessTravel", "Department", "DistanceFromHome",
            "Education", "EducationField", "EmployeeCount", 
            "EmployeeID", "Gender", "JobLevel", "JobRole", "MaritalStatus",
            "MonthlyIncome", "NumCompaniesWorked", "Over18", "PercentSalaryHike",
            "StandardHours", "StockOptionLevel", "TotalWorkingYears",
            "TrainingTimesLastYear", "YearsAtCompany", "YearsSinceLastPromotion",
            "YearsWithCurrMa0ger"]
rf_model.fit(X=df[features], y=df["Attrition"])
print("\noob accuracy:")
print(rf_model.oob_score_);
print("\n")
for features, imp in zip(features, rf_model.feature_importances_):
    print(features, imp);
    
predictors = pd.DataFrame([df["Age"], df["DistanceFromHome"], df["MonthlyIncome"],
                          df["PercentSalaryHike"], df["TotalWorkingYears"],
                          df["YearsAtCompany"]]).T

tree_model = tree.DecisionTreeClassifier(max_depth=12)
tree_model.fit(X = predictors, y = df["Attrition"])

with open("Dtree1.dot", 'w')as f:
    f = tree.export_graphviz(tree_model, feature_names=["Age", "DistanceFromHome",
                                                        "MonthlyIncome", "PercentSalaryHike",
                                                        "TotalWorkingYears", "YearsAtCompany"], out_file=f);
print("\nthe accuracy of the model")
print(tree_model.score(X = predictors, y = df["Attrition"]))

   




