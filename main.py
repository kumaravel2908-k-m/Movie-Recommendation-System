from file_handler import load_movies,save_movies
from movie_manager import (add_movie
                           ,view_movies
                           ,search_movie
                           ,delete_movie
                           ,update_movie
                           ,top_rated_movie,recommend_by_genre,filter_by_rating)

movies = load_movies()



while True:
    print("""
===== Movie Recommendation System =====

1. Add Movie
2. View Movies
3. Search Movie
4. Delete Movie
5. Update Movie
6. Top Rated Movie
7. Recommend by Genre
8. Filter by Minimum Rating
9. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie(movies)
    elif choice == "2":
        view_movies(movies)
    elif choice == "3":
        search_movie(movies)
    elif choice == "4":
        delete_movie(movies)
    elif choice == "5":
        update_movie(movies)
    elif choice == "6":
        top_rated_movie(movies)
    elif choice == "7":
        recommend_by_genre(movies)
    elif choice == "8":
        filter_by_rating(movies)
    elif choice == "9":
        print("Thank you for using Movie Recommendation System.")
        break
    else:
        print("Invalid choice!")
