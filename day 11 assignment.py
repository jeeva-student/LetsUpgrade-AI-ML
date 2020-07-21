import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as sat
import scipy as sci

dataset = pd.read_excel("C:\letsupgrage assignment\general data.xlsx")
#print(dataset)
dataset.dropna(subset = ["Attrition"], inplace=True)

from scipy.stats import pearsonr
stats, p = pearsonr(dataset.Attrition, dataset.DistanceFromHome)
print("the value of the attrition and the distance from home")
print(stats, p)

plt.scatter(dataset.Attrition, dataset.DistanceFromHome)

dataset.corr()

stats, q = pearsonr(dataset.Attrition, dataset.MonthlyIncome)
print("the valur of the Attrition and the monthly income")
print(stats, q)

plt.scatter(dataset.Attrition, dataset.MonthlyIncome)
dataset.corr()


stats, s = pearsonr(dataset.Attrition, dataset.Over18)
print("the valur of the Attrition and the over 18")
print(stats, s)

plt.scatter(dataset.Attrition, dataset.Over18)
dataset.corr()

stats, t = pearsonr(dataset.Education, dataset.PercentSalaryHike)
print("the valur of the Attrition and the percent salary hike")
print(stats, t)

plt.scatter(dataset.Attrition, dataset.PercentSalaryHike)
dataset.corr()

stats, u = pearsonr(dataset.Attrition, dataset.StandardHours)
print("the valur of the Attrition and the standard hours")
print(stats, u)

plt.scatter(dataset.Attrition, dataset.StandardHours)
dataset.corr()

stats, v = pearsonr(dataset.Attrition, dataset.StockOptionLevel)
print("the valur of the Attrition and the StockOptionLevel")
print(stats, v)

plt.scatter(dataset.Attrition, dataset.StockOptionLevel)
dataset.corr()


stats, x = pearsonr(dataset.Attrition, dataset.TrainingTimesLastYear)
print("the valur of the Attrition and the TrainingTimesLastYear")
print(stats, x)

plt.scatter(dataset.Attrition, dataset.TrainingTimesLastYear)
dataset.corr()

stats, y = pearsonr(dataset.Attrition, dataset.YearsAtCompany)
print("the valur of the Attrition and the YearsAtCompany")
print(stats, y)

plt.scatter(dataset.Attrition, dataset.YearsAtCompany)
dataset.corr()

stats, z = pearsonr(dataset.Attrition, dataset.YearsSinceLastPromotion)
print("the valur of the Attrition and the YearsSinceLastPromotion")
print(stats, z)

plt.scatter(dataset.Attrition, dataset.YearsSinceLastPromotion)
dataset.corr()

stats, a = pearsonr(dataset.Attrition, dataset.YearsWithCurrManager)
print("the valur of the Attrition and the YearsWithCurrManager")
print(stats, a)

plt.scatter(dataset.Attrition, dataset.YearsWithCurrManager)
dataset.corr()

stats, b = pearsonr(dataset.Attrition, dataset.Education)
print("the value of the Attrition and the education")
print(stats, b)

plt.scatter(dataset.Attrition, dataset.Education)

dataset.corr()