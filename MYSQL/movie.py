import json
import mysql.connector

class Movie:
    def __init__(self, title, year, movie_id=None):
        self.title = title
        self.year = year
        self.id = movie_id

class DBConnection:
    def __init__(self, config_path):
        self.config_path = config_path
        self.connection = None
        self.cursor = None

    def connect(self):
        with open(self.config_path) as f:
            config = json.load(f)["database"]
            
        self.connection = mysql.connector.connect(
            host=config["host"],
            port=config["port"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.cursor.close()

class MovieDatabase:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_movie_table(self):
        self.db_connection.cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), year INT)")

    def create_movie(self, movie):
        sql = "INSERT INTO movies (title, year) VALUES (%s, %s)"
        val = (movie.title, movie.year)
        self.db_connection.cursor.execute(sql, val)
        self.db_connection.connection.commit()
        movie.id = self.db_connection.cursor.lastrowid
        print("Movie added successfully")

    def read_movies(self):
        self.db_connection.cursor.execute("SELECT * FROM movies")
        movies = self.db_connection.cursor.fetchall()
        for movie in movies:
            print(movie)

    def update_movie(self, movie):
        sql = "UPDATE movies SET title = %s, year = %s WHERE id = %s"
        val = (movie.title, movie.year, movie.id)
        self.db_connection.cursor.execute(sql, val)
        self.db_connection.connection.commit()
        print("Movie updated successfully")

    def delete_movie(self, movie_id):
        sql = "DELETE FROM movies WHERE id = %s"
        val = (movie_id,)
        self.db_connection.cursor.execute(sql, val)
        self.db_connection.connection.commit()
        print("Movie deleted successfully")

# Example usage
db_connection = DBConnection(config_path="config.json")
db_connection.connect()

movie_db = MovieDatabase(db_connection)
movie_db.create_movie_table()

inception = Movie("Inception", 2010)
dark_knight = Movie("The Dark Knight", 2008)

movie_db.create_movie(inception)
movie_db.create_movie(dark_knight)

movie_db.read_movies()

inception.title = "Inception Updated"
movie_db.update_movie(inception)

movie_db.delete_movie(dark_knight.id)

movie_db.read_movies()

db_connection.disconnect()