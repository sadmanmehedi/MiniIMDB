class Movie:
    def __init__(self, title, release_year, genre, synopsis, ratings=[]):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.synopsis = synopsis
        self.ratings = ratings

    def add_rating(self, rating):
        self.ratings.append(rating)

    def calculate_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class MovieDatabase:
    def __init__(self):
        self.movies = {}

    def insert_movie(self, movie):
        self.movies[movie.title] = movie

    def find_movie_by_title(self, title):
        return self.movies.get(title)

    def update_movie_ratings(self, title, ratings):
        movie = self.movies.get(title)
        if movie:
            movie.ratings = ratings
        else:
            print("Movie not found!")

    def delete_movie(self, title):
        if title in self.movies:
            del self.movies[title]
        else:
            print("Movie not found!")

def main():
    movie_db = MovieDatabase()

    while True:
        print("\n===== Movie Database =====")
        print("1. Add Movie")
        print("2. Find Movie")
        print("3. Update Ratings")
        print("4. Delete Movie")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter movie title: ")
            release_year = int(input("Enter release year: "))
            genre = input("Enter genre: ")
            synopsis = input("Enter synopsis: ")

            movie = Movie(title, release_year, genre, synopsis)
            movie_db.insert_movie(movie)
            print("Movie added successfully!")

        elif choice == "2":
            title = input("Enter movie title to find: ")
            movie = movie_db.find_movie_by_title(title)
            if movie:
                print("\nMovie Details:")
                print("Title:", movie.title)
                print("Release Year:", movie.release_year)
                print("Genre:", movie.genre)
                print("Synopsis:", movie.synopsis)
                print("Ratings:", movie.ratings)
            else:
                print("Movie not found!")

        elif choice == "3":
            title = input("Enter movie title to update ratings: ")
            ratings = [float(rating) for rating in input("Enter ratings (comma-separated): ").split(",")]
            movie_db.update_movie_ratings(title, ratings)
            print("Ratings updated successfully!")

        elif choice == "4":
            title = input("Enter movie title to delete: ")
            movie_db.delete_movie(title)
            print("Movie deleted successfully!")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
