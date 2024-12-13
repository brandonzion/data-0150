#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:39:38 2024

@author: brandonsun
"""
import pandas as pd 
import plotly.express as px
df = pd.read_csv('data/top50.csv', parse_dates=['snapshot_date', 'album_release_date'])
plot(df, 'country', 'is_explicit')

