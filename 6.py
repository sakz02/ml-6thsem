# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:28:33 2023

@author: saksh
"""

import pandas as pd

data=pd.read_csv("6pima_indian.csv")
feature_col_names=['num_preg','glucose_conc','diastolic_bp','thickness','insulin','bmi','diab_pred','age']
target_class_names=['diabetes']
X=data[feature_col_names].values
y=data[target_class_names].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33)
print("\n training instances:",y_train.shape)
print("\n testing instances:",y_test.shape)


from sklearn.naive_bayes import GaussianNB
model=GaussianNB()

model.fit(X_train,y_train.ravel())
pred=model.predict(X_test)
pred_data=model.predict([[6,148,75,33.6,0,35,0.652,50]])

from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix
print(metrics.accuracy_score(y_test, pred))
print(metrics.confusion_matrix(y_test, pred))
print(metrics.recall_score(y_test,pred))
print(metrics.recall_score(y_test,pred))
print("predicted value:",pred_data)

