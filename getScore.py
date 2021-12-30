#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:38:11 2021

@author: julienpezet
"""

from rotten_tomatoes_client import RottenTomatoesClient
import imdb


def find_RottenTomatoes(query):
    result = RottenTomatoesClient.search(term=query, limit=5)   # Query the search results
    if result["movieCount"] >> 1:
        print("More than 1 result found, please be more specific or select one result below (list limited to 5).")
        print(f"For '{query}', I found the following results:")
        for i in range(0,len(result["movies"])):
            name = result['movies'][i]['name']
            year = result['movies'][i]['year']
            # if result['movies'][i]['castItems']:     # Catch issue if nobody in cast (terrible movie)
            try:
                homie1 = result['movies'][i]['castItems'][0]['name']
                if len(result['movies'][i]['castItems']) >= 2:  # Print casting up to 2 if possible
                    homie2 = result['movies'][i]['castItems'][1]['name']
                    print(f"{i+1}: {name} ({year}), with {homie1} and {homie2} in the cast.")
                else:
                    print(f"{i+1}: {name} ({year}), with {homie1} in the cast.")
            except:
                print(f"{i+1}: {name} ({year})")
        selectedMovie = input("Enter number of wanted movie: ")
    elif result["movieCount"] == 1:                             # The perfect case, one result
        selectedMovie = 1
    else:
        print("Could not find any matching result in Tomato search engine.")
        return []
    
    tomatometer = result["movies"][int(selectedMovie)-1];
    
    if "meterScore" in tomatometer:                       # Now we extract the score from the selected movie
        tomatometer2 = tomatometer["meterScore"]
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
    print(f"\nIMDb found the following: {title} ({year}), by {directors} with {casting}\n")
    return rating