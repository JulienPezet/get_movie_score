#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:16:21 2021

@author: julienpezet

Simple IMDb and Rotten Tomatoes score parser.
Found my inspiration thanks to https://gist.github.com/ZakiRangwala
You can find IMDb API here: https://imdbpy.github.io

"""

from rotten_tomatoes_client import RottenTomatoesClient
from bs4 import BeautifulSoup
import imdb



def find_RottenTomatoes(query):
    result = RottenTomatoesClient.search(term=query, limit=5)   # Query the search results
    if result["movieCount"] >> 1:
        print("More than 1 result found, please be more specific or select one result below (list limited to 5).")
        print(f"For '{query}', I found the following results:")
        for i in range(1,len(result["movies"])):
            name = result['movies'][i]['name']
            year = result['movies'][i]['year']
            homie1 = result['movies'][i]['castItems'][0]['name']
            if len(result['movies'][i]['castItems']) >= 2:      # Print casting up to 2 if possible
                homie2 = result['movies'][i]['castItems'][1]['name']
                print(f"{i}: {name} ({year}), with {homie1} and {homie2} in the cast.")
            else:
                print(f"{i}: {name} ({year}), with {homie1} in the cast.")
        selectedMovie = input("Enter number of wanted movie: ")
              
    tomatometer = result["movies"][int(selectedMovie)];
    
    if "meterScore" in tomatometer:
        tomatometer2 = tomatometer["meterScore"]
        # print(f"Tomatometer: {tomatometer2}\n")
        return tomatometer2
    else:
        return []
        print("This movie has no Rotten Tomatometer score yet.")
    
def find_IMDb(query):
    moviesDB = imdb.IMDb()
    movies = moviesDB.search_movie(query)       # Query the search results
    id = movies[0].getID()                      # Take the first one (IMDb API is quite good so far)
    movie = moviesDB.get_movie(id)              # Get data with ID
    title = movie['title']
    year = movie['year']
    rating = int(movie['rating']*10)
    directors = movie['directors'][0]['name']
    casting = movie['cast'][0]['name']
    print(f"\nIMDb found the following: {title} ({year}), by {directors} with {casting}\n\nIMDB Score: {rating}")
    return rating

query = "Cmon Cmon"
tomatometer = find_RottenTomatoes(query)
IMDbscore = find_IMDb(query)
if not tomatometer:                             # Not so sexy coding, but it diplays things better
    print("This movie has no Rotten Tomatometer score yet.")
else:
    print(f"Tomatometer: {tomatometer}\n")