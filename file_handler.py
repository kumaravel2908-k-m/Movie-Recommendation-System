import json

def load_movies():
    with open("movies.json", "r", encoding="utf-8") as file:
        movies = json.load(file)
        return movies
    
def save_movies(movies):
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)