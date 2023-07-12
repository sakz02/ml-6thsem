# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:44:29 2023

@author: saksh
"""

import pandas as pd

data=pd.read_csv("1weather_dataset.csv")
print(data)

def package_hypothesis(hypothesis,outcome):
    ln=dict()
    ln['hypothesis']=hypothesis
    ln['outcome']=outcome
    return ln

h1=package_hypothesis(['?','?','normal','?','?'],'yes')

h2=package_hypothesis(['sunny','high','?','?','?'],'yes')

h3=package_hypothesis(['rainy','?','ok','?','?'],'no')

h4=package_hypothesis(['sunny','warm','high','?','?'],'yes')

h5=package_hypothesis(['?','cold','?','cool','?'],'no')

h6=package_hypothesis(['?','?','?','cool','?'],'yes')

def compare(values,hypo):
    for i in range(len(values)):
        if hypo[i]!='?':
            if values[i]!=hypo[i]:
                return False
    return True
        

def list_then_eliminate(data,*hypothesis):
    in_space=[]
    con_space=[]
    
    for hyp in hypothesis:
        state=True
        for i in range(data.shape[0]):
            if hyp['outcome']==data.iloc[i,-1]:
                if (not compare(hypo=hyp['hypothesis'],values=list(data.iloc[i,:-1][:-1]))):
                    in_space.append(hyp)
                    state=False
                    break
        if (state):
            con_space.append(hyp)
    
            
    return in_space,con_space

print(list_then_eliminate(data, h1,h2,h3,h4,h5,h6))


