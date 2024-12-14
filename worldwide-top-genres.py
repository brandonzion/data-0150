#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:12:17 2024

@author: brandonsun
"""
import pandas as pd 
import matplotlib.pyplot as plt

def extractGenre(genres):
    return genres.split(";")[0]

og = pd.read_csv("data/artists.csv")
top_100_artists = og.nlargest(100, 'listeners_lastfm')
top_100_artists["tags_lastfm"] = top_100_artists['tags_lastfm'].apply(extractGenre)
top_100_genres = top_100_artists['tags_lastfm']
genreCounts = top_100_genres.value_counts()
genreCounts.plot(kind='bar', xlabel='genre', ylabel='frequency')
plt.show()

