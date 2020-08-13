def svm_svc():
    import pandas as pd
    df = pd.read_excel(r"C:\letsupgrage assignment\train.xlsx", sheet_name=0)
    from sklearn import preprocessing
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    from sklearn import svm
    from sklearn.model_selection import train_test_split
    
    le = preprocessing.LabelEncoder()
    le.fit(df["Sex"])
    df["Sex"] = le.fit_transform(df["Sex"])
    df["Embarked"] = le.fit_transform(df["Embarked"])
    
    df1 = df.drop(["Name", "Ticket", "Cabin", "PassengerId", "Age", "Fare"], axis=1)
    
    features = ["Survived", "Pclass", "Sex",
            "SibSp", "Parch", "Embarked"]
    
    for i in features:
        print("\nthe feature is:", i)
        y = df1[i]
        X = df1.drop([i], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = None)
        clf = svm.SVC(gamma = 0.01, C = 100)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print("\n the accurcy using the feature: ", i)
        print(accuracy_score(y_test, y_pred, normalize=True))
        print("\nthe confusion matrix using the feature:", i)
        print(confusion_matrix(y_test, y_pred))
        print("----------------------------------------------------------------------------------------")
    
    
svm_svc()