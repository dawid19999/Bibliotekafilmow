
# Zadanie 7.4

import random

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = 0

    def play(self, views):
        self.plays += views

    def __str__(self):
        return f"{self.title} ({self.year})"

class Series(Movie):
    def __init__(self, title, year, genre, season, episode):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"


def filter_and_sort(library, cls):
    return sorted([item for item in library if isinstance(item, cls)], key=lambda x: x.title)

def get_movies(library):
    return filter_and_sort(library, Movie)

def get_series(library):
    return filter_and_sort(library, Series)

def search(library, title):
    return [item for item in library if title.lower() in item.title.lower()]

def generate_views(library):
    item = random.choice(library)
    views = random.randint(1, 100)
    item.play(views)

def run_generate_views(library, times=10):
    for _ in range(times):
        generate_views(library)

def top_titles(library, n=3, content_type=None):
    if content_type == "movie":
        items = get_movies(library)
    elif content_type == "series":
        items = get_series(library)
    else:
        items = library

    return sorted(items, key=lambda x: x.plays, reverse=True)[:n]


if __name__ == "__main__":
    library = [
        Movie("Pulp Fiction", 1994, "Crime"),
        Movie("The Matrix", 1999, "Sci-Fi"),
        Movie("Inception", 2010, "Thriller"),
        Series("Friends", 1994, "Comedy", 1, 1),
        Series("Breaking Bad", 2008, "Drama", 2, 3),
        Series("The Office", 2005, "Comedy", 3, 5),
    ]

    run_generate_views(library)

    print("Najpopularniejsze tytuły:")
    for item in top_titles(library, 3):
        print(f"{item} - {item.plays} odtworzeń")

    print("\nWszystkie filmy:")
    for movie in get_movies(library):
        print(movie)

    print("\nWszystkie seriale:")
    for series in get_series(library):
        print(series)

    user_query = input("\nWpisz tytuł do wyszukania: ")
    results = search(library, user_query)

    if results:
        print("\nWyniki wyszukiwania:")
        for match in results:
            print(match)
    else:
        print("Nie znaleziono tytułu.")
