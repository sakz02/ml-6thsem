# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:15:59 2023

@author: saksh
"""
import pandas as pd

data=pd.read_csv("5user_data.csv")
X=data.iloc[:,[2,3]].values
y=data.iloc[:,4].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=10,criterion="entropy",random_state=0)

clf.fit(X_train,y_train)
pred=clf.predict(X_test)

from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix
print("accuracy is ", metrics.accuracy_score(y_test,pred))
print(metrics.confusion_matrix(y_test,pred))
print(metrics.recall_score(y_test,pred,average="weighted"))
print(metrics.recall_score(y_test,pred,average="weighted"))
