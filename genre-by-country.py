#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 14:34:04 2024

@author: brandonsun
"""
import country_converter as coco
import pandas as pd 
import plotly.express as px
cc = coco.CountryConverter()
og = pd.read_csv("data/artists.csv")
popularityByCountry = og.groupby("country_mb")['listeners_lastfm']
mostPopularGenreByCountry = og.loc[popularityByCountry.transform(max) == og['listeners_lastfm']]
fig = px.choropleth(
    locations=cc.pandas_convert(series=mostPopularGenreByCountry['country_mb'], to='ISO2', not_found=None),
    color=mostPopularGenreByCountry['listeners_lastfm'])
fig.show()
