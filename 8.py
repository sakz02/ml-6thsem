# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:57:29 2023

@author: saksh
"""

import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianNetwork

data=pd.read_csv("8heartdiseasedata.csv",names=['age','Gender','Family','diet','Lifestyle','cholestrol', 'heartdisease'])

heartDisease=pd.DataFrame(data)

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
for col in heartDisease.columns:
    heartDisease[col]=lb.fit_transform(heartDisease[col])

print(heartDisease.head())
print(heartDisease.dtypes)

model=BayesianNetwork([('age','heartdisease'),('Gender','heartdisease'),('Family','heartdisease'),('diet','cholestrol'),('Lifestyle','diet'),('heartdisease','cholestrol')])

print("\n training instances")
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)
print("inferencing the data")
heartDis_infer=VariableElimination(model)


print('For age enter {SSC:0, SC:1, MA:2, Y:3, T:4}')
print('For gender enter {female:1, male:0}')
print('for family history enter {yes:1,no:0}')
print('for diet enter {high:1,low:0}')
print('for lifestyle enter {athlete:0, active:1, normal:2, sedentary:3}')
print('for cholestrol enter {high:0, borderline:1, normal:2}')

print("probability given evidence=age")
q1=heartDis_infer.query(variables=['heartdisease'],evidence={'age': int(input('enter age'))})
print(q1)

print("probability given evidence=cholestrol")
q2=heartDis_infer.query(variables=['heartdisease'],evidence={'cholestrol': int(input('enter cholestrol'))})
print(q2)
