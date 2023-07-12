# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:33:34 2023

@author: saksh
"""
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

iris=datasets.load_iris()

X=pd.DataFrame(iris.data)
X.columns=['sepal_length','sepal_width','petal_length','petal_width']
y=pd.DataFrame(iris.target)
y.columns=['target']

plt.figure(figsize=(14,7))
colormap=np.array(['red','lime','black'])

plt.subplot(2,2,1)
plt.scatter(X.sepal_width,X.sepal_length,c=colormap[y.target],s=40)
plt.title("sepal")

plt.subplot(2,2,2)
plt.scatter(X.petal_width,X.petal_length,c=colormap[y.target],s=40)
plt.title("petal")

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(X)
xsa=sc.transform(X)
xs=pd.DataFrame(xsa,columns=X.columns)

print(xs.head())

from sklearn.mixture import GaussianMixture
gmm=GaussianMixture(n_components=3)

gmm.fit(xs)
y_cluster_gmm=gmm.predict(xs)

plt.subplot(2,2,3)
plt.scatter(X.petal_width,X.petal_length,c=colormap[y_cluster_gmm],s=40)
plt.title("GaussianMixture")

from sklearn import metrics 
from sklearn.metrics import accuracy_score,confusion_matrix
print(metrics.accuracy_score(y, y_cluster_gmm))
print(metrics.confusion_matrix(y, y_cluster_gmm))