# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:45:06 2023

@author: saksh
"""

import pandas as pd

msg=pd.read_csv("7naivetext.csv", names=['message','label'])
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
X=msg.message
y=msg.labelnum
print(X)
print(y)


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y)

print(y_train.shape)
print(y_test.shape)

from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
Xtrain_dtm=count_vect.fit_transform(X_train)
Xtest_dtm=count_vect.transform(X_test)

print("the tokens or words present are")
print(count_vect.get_feature_names())

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB()
clf.fit(Xtrain_dtm,y_train)

pred=clf.predict(Xtest_dtm)

from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix

print(metrics.accuracy_score(y_test, pred))
print(metrics.confusion_matrix(y_test,pred))
print(metrics.recall_score(y_test,pred))
print(metrics.recall_score(y_test,pred))