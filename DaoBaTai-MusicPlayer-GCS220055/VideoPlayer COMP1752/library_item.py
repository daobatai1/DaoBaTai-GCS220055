class LibraryItem:
    def __init__(self, name, director, rating, genre, mp3_file, play_count=0):
        self.name = name
        self.director = director
        self.rating = rating
        self.genre = genre
        self.mp3_file = mp3_file  # Add this line to store the MP3 file path
        self.play_count = play_count

    def info(self):
        """Return a string with information about the library item."""
        return f"{self.name} by {self.director}, Rating: {self.rating}, Genre: {self.genre}, Plays: {self.play_count}"

    def stars(self):
        """Return a string of stars representing the rating."""
        # Limit the number of stars to 10 for readability
        max_stars = 10
        return '*' * min(self.rating, max_stars)
