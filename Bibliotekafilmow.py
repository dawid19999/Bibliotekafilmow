
# Zadanie 7.4

import random

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = 0

    def play(self, step=1):
        self.plays += step

    def __str__(self):
        return f"{self.title} ({self.year})"


class Series(Movie):  
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"



library = []


def get_movies():
    return sorted(
        [item for item in library if isinstance(item, Movie) and not isinstance(item, Series)],
        key=lambda x: x.title
    )

def get_series():
    return sorted(
        [item for item in library if isinstance(item, Series)],
        key=lambda x: x.title
    )

def search(title):
    return [item for item in library if title.lower() in item.title.lower()]


def generate_views():
    item = random.choice(library)
    views = random.randint(1, 100)
    item.play(views)

def run_generate_views():
    for _ in range(10):
        generate_views()



def top_titles(n=3, content_type=None):
    if content_type == "movie":
        items = get_movies()
    elif content_type == "series":
        items = get_series()
    else:
        items = library

    return sorted(items, key=lambda x: x.plays, reverse=True)[:n]


library.append(Movie("Pulp Fiction", 1994, "Crime"))
library.append(Movie("The Matrix", 1999, "Sci-Fi"))
library.append(Movie("Inception", 2010, "Thriller"))
library.append(Series("Friends", 1994, "Comedy", 1, 1))
library.append(Series("Breaking Bad", 2008, "Drama", 2, 3))
library.append(Series("The Office", 2005, "Comedy", 3, 5))


run_generate_views()

print("Najpopularniejsze tytuły:")
for item in top_titles(3):
    print(f"{item} - {item.plays} odtworzeń")

print("\nWszystkie filmy:")
for movie in get_movies():
    print(movie)

print("\nWszystkie seriale:")
for series in get_series():
    print(series)

print("\nWyniki wyszukiwania dla 'Friends':")
for match in search("Friends"):
    print(match)
