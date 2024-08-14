from library_item import LibraryItem

# Initialize the library dictionary
library = {
    "01": LibraryItem("amalgam", "Alan", 5, "Electronic", "amalgam_rockot_electronic.mp3"),
    "02": LibraryItem("chasinghorizons", "Justin", 4, "R&B", "chasinghorizons.mp3"),
    "03": LibraryItem("etheralhorizons", "Maroon 5", 6, "Pop", "etherealhorizons.mp3"),
    "04": LibraryItem("flowloki", "Travis Scott", 5, "Rap", "flow_loki_emotional.mp3"),
    "05": LibraryItem("movement", "Ed Sheeran", 3, "Pop", "movement_soulprodmusic_breakthrough.mp3"),
    "06": LibraryItem("titanium", "Hozier", 2, "Rock", "titanium_alisiabeats_trap.mp3"),
    "07": LibraryItem("trap", "Ed Sheeran", 1, "Pop", "trapfuturebass_royaltyfreemusic_advertisement.mp3")
}

# Function to list all items in the library
def list_all():
    output = ""
    for key, item in library.items():
        output += f"{key}: {item.info()}\n"
    return output

# Function to get the name of a library item
def get_name(key):
    item = library.get(key)
    if item:
        return item.name
    return None

# Function to get the MP3 file of a library item
def get_mp3_file(key):
    item = library.get(key)
    if item:
        return item.mp3_file
    return None

# Function to get information about an individual library item
def get_info(key):
    item = library.get(key)
    if item:
        return {
            "name": item.name,
            "director": item.director,
            "rating": item.rating,
            "genre": item.genre,
            "play_count": item.play_count
        }
    return None

# Function to update the information of a library item
def update_video(key, name, director, genre, rating):
    item = library.get(key)
    if item:
        item.name = name
        item.director = director
        item.genre = genre
        item.rating = rating
        return True
    return False

# Function to set the rating of a library item
def set_rating(key, rating):
    item = library.get(key)
    if item:
        item.rating = rating

# Function to increment the play count of a library item
def increment_play_count(key):
    item = library.get(key)
    if item:
        item.play_count += 1

# Function to reset the play count for all library items
def reset_play_counts():
    for item in library.values():
        item.play_count = 0

# Function to reset the play count for a specific library item
def reset_play_count(key):
    item = library.get(key)
    if item:
        item.play_count = 0

# Function to reset the library to its initial state
# Assuming this method is part of a class with GUI elements
def reset_video_clicked(self):
    key = self.input_txt.get()
    reset_play_count(key)
    self.check_video_clicked()  # Refresh the video details
    self.status_lbl.configure(text=f"Video {key} play count reset!")

if __name__ == "__main__":
    # Example usage
    print(list_all())
    set_rating("01", 7)
    increment_play_count("01")
    print(get_info("01"))
    reset_play_counts()
    print(list_all())
