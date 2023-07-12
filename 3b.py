# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:22:34 2023

@author: saksh
"""

import pandas as pd
import numpy as np

from numpy import unique

data=pd.read_csv("3oil-spill.csv", header=None)
print(data.nunique())

count=data.nunique()
print(data.shape)

to_del=[i for i,v in enumerate(count) if v==1]
print(to_del)

data.drop(to_del,axis=1,inplace=True)
print(data.shape)


