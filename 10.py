# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:03:04 2023

@author: saksh
"""

import pandas as pd

data=pd.read_csv("10iris.csv")
X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.svm import SVC
clf=SVC(kernel="linear",random_state=0,)

clf.fit(X_train,y_train)
pred=clf.predict(X_test)

from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix
print(metrics.accuracy_score(y_test, pred))
print(metrics.confusion_matrix(y_test, pred))
print(metrics.recall_score(y_test, pred,average="weighted"))
print(metrics.precision_score(y_test, pred,average="weighted"))

