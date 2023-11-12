def movie_organizer(*args):
    resulting_string = ""
    genres_dict = {}
    for entry in args:
        movie = entry[0]
        genre = entry[1]
        if genre not in genres_dict:
            genres_dict[genre] = []
        genres_dict[genre].append(movie)
    arranged_movies = sorted(genres_dict.items(), key=lambda item: (-len(item[1]), item[0]))
    for current_genre, movies in arranged_movies:
        resulting_string += f"{current_genre} - {len(movies)}\n"
        for movie in sorted(movies):
            resulting_string += f"* {movie}\n"
    return resulting_string


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

