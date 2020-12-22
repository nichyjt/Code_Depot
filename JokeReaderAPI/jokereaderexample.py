import jokereader as joke

# Debug script
# Simulating a bored programmer using jokereader.py

joke.setJokeFilters(no_nsfw=True, no_political=True)
joke.getJoke(joke.JOKE_CAT_PROGRAMMING)