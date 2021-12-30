#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:16:21 2021

@author: julienpezet

Simple IMDb and Rotten Tomatoes score parser.
Found my inspiration thanks to https://gist.github.com/ZakiRangwala
You can find IMDb API here: https://imdbpy.github.io

"""

from getScore import *

# USER INPUT
query = "Harry Potter Secrets Chamber"                         # This is where you can search


tomatometer = find_RottenTomatoes(query)
IMDbscore = find_IMDb(query)
print(f"IMDB Score:  {IMDbscore}")
if not tomatometer:                             # Not so sexy coding, but it diplays things better
    print("This movie has no Rotten Tomatometer score yet.")
else:
    print(f"Tomatometer: {tomatometer}\n")