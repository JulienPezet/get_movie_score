This program uses two APIs: 
  - IMDbPY (https://imdbpy.github.io);
  - rotten_tomatoes_client (https://pypi.org/project/rotten_tomatoes_client/).

requirements.txt comprises rotten_tomatoes_client and the needed packages for imdbpy.

## Done
  - Retrieve score from IMDb
  - Retrieve score from Rotten Tomatoes
      - Handle exceptions: no Tomatometer, no movie referenced, many movies found...

## To Do
  - Propose choice within IMDb if proposed movie is incorrect;
  - Retrieve Rotten Tomatoes Audience score;
  - From a directory with a movie database, loop over all movies and check if more description is needed. For instance, I'd like on all my folders a name like that: Dont Look Up (2021) [1080p] RTm56 RTa77 IMDb73. If the score is not displayed, query the APIs to append the scores in folder name.

### Credits
I came to this script with ideas from Zaki mini-scripts (https://gist.github.com/ZakiRangwala).
Big thanks to IMDb for this amazing API, a lot to scrape still.
Thanks to Jae Bradley for creating this not Rotten API.
