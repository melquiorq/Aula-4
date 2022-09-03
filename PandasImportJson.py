# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 20:17:53 2022

@author: bande
"""

import pandas as pd
import json
from urllib import request

def_csv = pd.read_json('https://raw.githubusercontent.com/diasctiago/pandas/main/leads.json')
print(def_csv.head(10))
with request.urlopen('https://raw.githubusercontent.com/diasctiago/pandas/main/leads.json') as arquivo:
    dados_json = json.load(arquivo)