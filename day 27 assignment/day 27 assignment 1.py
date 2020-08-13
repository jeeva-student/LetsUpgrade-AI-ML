def K_value():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import preprocessing
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    df = pd.read_excel(r"C:\letsupgrage assignment\train.xlsx", sheet_name=0)
    print(df.columns)
    
    le = preprocessing.LabelEncoder()
    le.fit(df["Sex"])
    df["Sex"] = le.transform(df["Sex"])
    le.fit(df["Embarked"])
    df["Embarked"] = le.transform(df["Embarked"])
    df1 = df.drop(["Name", "Ticket", "Cabin"], axis = 1)
    
    from sklearn import neighbors
    y = df1["Pclass"]
    X = df1.drop(["Pclass", "PassengerId"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=None)
    k = []
    s = []
    
    m = range(1, 268)
    for i in m:
        print("\nthe value of K is:  ", i)
        knn = neighbors.KNeighborsClassifier(n_neighbors=i)
        k.append(i)
        print("\nthe accuracy of the model using the K value:  ", i)
        h = knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        score = h.score(X_test, y_test)
        print(score)
        s.append(score)
        print(confusion_matrix(y_test, y_pred))
        print("-----------------------------------------------------------------------------------")
        plt.plot(k, s)
        plt.title("model")
        plt.xlabel("the k value")
        plt.ylabel("accuracy")
        plt.show()

K_value()