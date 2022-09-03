# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 20:10:23 2022

@author: bande
"""

import pandas as pd

def_csv = pd.read_excel('https://github.com/diasctiago/pandas/blob/main/leads.xlsx?raw=true')
print(def_csv.head(10))