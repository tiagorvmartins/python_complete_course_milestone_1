movies = []

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit.")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command-please try again.')

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit: ")

def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the movie director: ')
    year = int(input('Enter the movie release year: '))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })

def show_movies():
    for movie in movies:
        show_movie_details(movie)

def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


menu()

print(movies)