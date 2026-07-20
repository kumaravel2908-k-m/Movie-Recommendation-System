from file_handler import save_movies

def add_movie(movies):
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")
    rating = float(input("Enter rating: "))
    year = int(input("Enter year: "))

    movies[title] = {
        "genre": genre,
        "rating": rating,
        "year": year
    }
    save_movies(movies)
    print("Movie added successfully!")


def view_movies(movies):
    if len(movies) == 0:
        print("No movies available.")
        return

    for title, details in movies.items():
        print(f"""
    Title : {title}
    Genre : {details['genre']}
    Rating: {details['rating']}
    Year  : {details['year']}
    """)
        
def search_movie(movies):
    search_title = input("Enter movie title: ")

    if search_title in movies:
        details = movies[search_title]
        print(f"""
    Title : {search_title}
    Genre : {details['genre']}
    Rating: {details['rating']}
    Year  : {details['year']}
    """)
    else:
        print("Movie not found!")

def delete_movie(movies):
    search_title = input("Enter movie title to delete: ")

    if search_title in movies:
        del movies[search_title]
        save_movies(movies)
        print("Movie deleted successfully!")
    else:
        print("Movie not found!")

def update_movie(movies):
    mov_title = input("Enter movie title: ")

    if mov_title not in movies:
        print("Movie not found!")
        return

    print("""
    1. Update Genre
    2. Update Rating
    3. Update Year
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        movies[mov_title]["genre"] = input("Enter new genre: ")
    elif choice == "2":
        movies[mov_title]["rating"] = float(input("Enter new rating: "))
    elif choice == "3":
        movies[mov_title]["year"] = int(input("Enter new year: "))
    else:
        print("Invalid choice")
        return
    save_movies(movies)
    print("Movie updated successfully!")

def top_rated_movie(movies):
    if len(movies) == 0:
        print("No movies available.")
        return

    high_rating = 0
    top_movie = ""

    for key, val in movies.items():
        if val["rating"] > high_rating:
            high_rating = val["rating"]
            top_movie = key

    details = movies[top_movie]

    print(f"""Top Rated Movie
    Title : {top_movie}
    Genre : {details['genre']}
    Rating: {details['rating']}
    Year  : {details['year']}
    """)

def recommend_by_genre(movies):
    genre_search = input("Enter genre: ")
    found = False

    for key, val in movies.items():
        if val["genre"].lower() == genre_search.lower():
            print(f"{key} ⭐ {val['rating']}")
            found = True

    if not found:
        print("No movies found.")

def filter_by_rating(movies):
    minimum = float(input("Enter minimum rating: "))
    found = False

    for key, val in movies.items():
        if val["rating"] >= minimum:
            print(f"{key} ⭐ {val['rating']}")
            found = True

    if not found:
        print("No movies found.")