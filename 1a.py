# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 12:16:23 2023

@author: saksh
"""

import pandas as pd

data=pd.read_csv("1finds.csv")

concepts=data.iloc[:,0:-1].values
print(concepts)
print("-------------------------------")
target=data.iloc[:,-1].values
print(target)
print("-------------------------------")


def train(concepts,target):
    count=0
    specific_h=concepts[0]
    for i,h in enumerate(concepts):
        print(i)
        print(h)
        if target[i]==1:
            for x in range(len(specific_h)):
                if h[x]==specific_h[x]:
                    pass
                else:
                    specific_h[x]="?"
                    
            count=count+1
            print(f'positive hypothesis : {count} processed :{specific_h}')
        else:
            pass
        
            count=count+1
            print(f'negative hypothesis : {count} processed :{specific_h}')
        
    return specific_h

specific_h=train(concepts,target)


