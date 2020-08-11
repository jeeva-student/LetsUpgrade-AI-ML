import pandas as pd

df = pd.read_csv(r"C:\letsupgrage assignment\train.csv")
print(df.columns)

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

le = preprocessing.LabelEncoder()
le.fit(df["Sex"])
df["Sex"] = le.transform(df["Sex"])
le.fit(df["Embarked"])
df["Embarked"] = le.transform(df["Embarked"])

def pc_class():
    print("\nthe pc_class")
    Y = df["Pclass"]
    X = df.drop(["Pclass", "PassengerId", "Name", "Ticket", "Cabin"], axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)
    clf = BernoulliNB()
    y_pred = clf.fit(X_train, Y_train).predict(X_test)
    print("\nthe accuracy of this model:")
    print(accuracy_score(Y_test, y_pred, normalize=True))
    print("\nthe confusion matrix is:")
    print(confusion_matrix(Y_test, y_pred))
print(pc_class())

def sex_col():
     print("\nthe sex_col")
     Y = df["Sex"]
     X = df.drop(["Sex", "PassengerId", "Name", "Ticket", "Cabin"], axis=1)
     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)
     clf = BernoulliNB()
     y_pred = clf.fit(X_train, Y_train).predict(X_test)
     print("\nthe accuracy of this model:")
     print(accuracy_score(Y_test, y_pred, normalize=True))
     print("\nthe confusion matrix is:")
     print(confusion_matrix(Y_test, y_pred))
print(sex_col())

def SibSp_col():
     print("\nthe SibSp_col")
     Y = df["SibSp"]
     X = df.drop(["SibSp", "PassengerId", "Name", "Ticket", "Cabin"], axis=1)
     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)
     clf = BernoulliNB()
     y_pred = clf.fit(X_train, Y_train).predict(X_test)
     print("\nthe accuracy of this model:")
     print(accuracy_score(Y_test, y_pred, normalize=True))
     print("\nthe confusion matrix is:")
     print(confusion_matrix(Y_test, y_pred))
print(SibSp_col())

def Parch_col():
     print("\nthe Parch_col")
     Y = df["Parch"]
     X = df.drop(["Parch", "PassengerId", "Name", "Ticket", "Cabin"], axis=1)
     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)
     clf = BernoulliNB()
     y_pred = clf.fit(X_train, Y_train).predict(X_test)
     print("\nthe accuracy of this model:")
     print(accuracy_score(Y_test, y_pred, normalize=True))
     print("\nthe confusion matrix is:")
     print(confusion_matrix(Y_test, y_pred))
print(Parch_col())

def Embarked_col():
     print("\nthe Embarked_col")
     Y = df["Embarked"]
     X = df.drop(["Embarked", "PassengerId", "Name", "Ticket", "Cabin"], axis=1)
     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=0)
     clf = BernoulliNB()
     y_pred = clf.fit(X_train, Y_train).predict(X_test)
     print("\nthe accuracy of this model:")
     print(accuracy_score(Y_test, y_pred, normalize=True))
     print("\nthe confusion matrix is:")
     print(confusion_matrix(Y_test, y_pred))
print(Embarked_col())