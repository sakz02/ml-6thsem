# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:05:59 2023

@author: saksh
"""

import pandas as pd
data=pd.read_csv("3iris.csv",header=None)

dups=data.duplicated()
print(dups.any())
print(data[dups])

print(data.shape)
data.drop_duplicates(inplace=True)
print(data.shape)
