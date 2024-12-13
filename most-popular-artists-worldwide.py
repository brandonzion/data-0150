#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:50:06 2024

@author: brandonsun
"""
import pandas as pd 
import plotly.express as px
rel_cols = ['rank', 'date', 'artist', 'region', 'streams']
og = pd.read_csv("data/charts.csv", usecols=rel_cols)

artist_counts = og['artist'].value_counts()

top_10 = artist_counts.iloc[:10]

top_10.plot(kind='bar')

print(top_10)