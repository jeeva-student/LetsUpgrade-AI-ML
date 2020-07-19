import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as sat

dataset = pd.read_excel("C:\letsupgrage assignment\general data.xlsx")
print(dataset.head())
print(dataset.columns)
print(dataset.isnull())
print(dataset.duplicated())
print(dataset.drop_duplicates())
dataset1 = dataset[["Age", "Attrition", "DistanceFromHome", "MonthlyIncome", 
                         "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
                         "TotalWorkingYears", "TrainingTimesLastYear", 
                         "YearsAtCompany", "YearsSinceLastPromotion", "YearsWithCurrManager"]].mean()
#print(dataset1)

#dataset2 = dataset[["Age", "Attrition", "DistanceFromHome", 
 #                      "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
  #                       "TotalWorkingYears", "TrainingTimesLastYear", 
   #                     "YearsAtCompany", "YearsSinceLastPromotion", "YearsWithCurrManager"]].median()
#print(dataset2)

#dataset3 = dataset[["Age", "Attrition", "DistanceFromHome", "MonthlyIncome", 
 #                        "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
  #                     "TotalWorkingYears", "TrainingTimesLastYear", 
   #                    "YearsAtCompany", "YearsSinceLastPromotion", "YearsWithCurrManager"]].mode()
#print(dataset3)
      
#dataset4 = dataset[["Age", "Attrition", "DistanceFromHome", "MonthlyIncome", 
   #                      "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
  #                       "TotalWorkingYears", "TrainingTimesLastYear", 
 #                        "YearsAtCompany", "YearsSinceLastPromotion", "YearsWithCurrManager"]].var()
#print(dataset4)
      
#dataset5 = dataset[["Age", "Attrition", "DistanceFromHome", "MonthlyIncome", 
 #                        "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
  #                       "TotalWorkingYears", "TrainingTimesLastYear", 
   #                      "YearsAtCompany", "YearsSinceLastPromotion", "YearsWithCurrManager"]].skew()
#print(dataset5)

#dataset6 = dataset[["Age", "Attrition", "DistanceFromHome", "MonthlyIncome", 
   #                      "NumCompaniesWorked", "PercentSalaryHike", "StandardHours",
  #                       "TotalWorkingYears", "TrainingTimesLastYear", 
 #                        "YearsAtCompany", "YearsSinceLastPromotion", "YearsWithCurrManager"]].kurt()
#print(dataset6)

#dataset7 = dataset.describe()
#print(dataset7)


#plt.scatter("YearsSinceLastPromotion", "YearsAtCompany")
#plt.xlabel("MonthlyIncome")
#plt.ylabel("YearsAtCompany")
#box_plot = dataset1.MonthlyIncome
#plt.boxplot(box_plot)
#print(dataset["Age"].mean())

#standard_deviation = sat.stdev("Age")
dataset8 = dataset["MonthlyIncome"].median()
print("the value of the median = ", dataset8)