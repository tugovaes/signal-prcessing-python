# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:04:01 2020

@author: Катя
"""

import pandas as pd
import numpy as np
s=[1, 2, 3, 2, 101, 25]
df = pd.DataFrame({dates : s})
#df = pd.Serias(s)
#s=({1, 2, 3, 2, 101, 25})
trend = df.rolling(2).sum()

#trend=s.pd.DataFrame.rolling(2)
print(trend)