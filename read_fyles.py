# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
filename = '14_0_20200120.csv'
f = open(filename)
s = f.readlines()
all_codes = []
for i, item in enumerate(s):
    temp = item.split(';')
    s[i] = int(temp[1])
print(s)
f.close()

#'''