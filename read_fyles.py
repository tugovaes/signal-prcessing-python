# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import pandas as pd
import numpy as np
#Ввeдите имя файла
filename = '14_0_20200120.csv'


f = open(filename)
s = f.readlines()
all_codes = []
for i, item in enumerate(s):
    temp = item.split(';')
    s[i] = int(temp[1])
print(s)
f.close()

df = pd.DataFrame({dates : s})
#df = pd.Serias(s)
#s=({1, 2, 3, 2, 101, 25})
trend = df.rolling(100).sum()

#trend=s.pd.DataFrame.rolling(2)
print(trend)

#'''