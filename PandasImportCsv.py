# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 20:07:44 2022

@author: bande
"""


import pandas as pd

def_csv = pd.read_csv('https://raw.githubusercontent.com/diasctiago/pandas/main/leads.txt', delimiter='|')
print(def_csv.head(10))
