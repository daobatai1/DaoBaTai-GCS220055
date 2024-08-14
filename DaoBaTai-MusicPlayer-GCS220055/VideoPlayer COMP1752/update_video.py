import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Delete current text
    text_area.insert(tk.END, content)  # Insert new content

class UpdateVideos:
    def __init__(self, window):
        window.geometry("750x400")  # Increase the window height to 400
        window.title("Update Video Rating")
        window.configure(bg="#323232")  # Set the background color to a dark gray

        # Label and entry for video number input
        enter_lbl = tk.Label(window, text="Enter Video Number", bg="#323232", fg="#FFFFFF", font=("Helvetica", 12))
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.input_txt = tk.Entry(window, width=3, font=("Helvetica", 12))
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # Label and entry for new rating input
        rating_lbl = tk.Label(window, text="Enter New Rating", bg="#323232", fg="#FFFFFF", font=("Helvetica", 12))
        rating_lbl.grid(row=0, column=2, padx=10, pady=10)
        self.rating_txt = tk.Entry(window, width=3, font=("Helvetica", 12))
        self.rating_txt.grid(row=0, column=3, padx=10, pady=10)

        # "Update Rating" button
        update_rating_btn = tk.Button(window, text="Update Rating", command=self.update_rating_clicked, bg="#555555", fg="#FFFFFF", font=("Helvetica", 12))
        update_rating_btn.grid(row=0, column=4, padx=10, pady=10)

        # Text area for displaying update status
        self.status_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", bg="#555555", fg="#FFFFFF", font=("Helvetica", 12))
        self.status_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        # Status Label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="#323232", fg="#FFFFFF")
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)

    # Handle "Update Rating" button click
    def update_rating_clicked(self):
        key = self.input_txt.get()  # Get video number
        new_rating = self.rating_txt.get()  # Get new rating

        if not new_rating.isdigit() or not (1 <= int(new_rating) <= 5):
            set_text(self.status_txt, "Invalid rating. Please enter a number between 1 and 5.")
            return

        info = lib.get_info(key)
        if info:
            lib.set_rating(key, int(new_rating))  # Only update the rating
            updated_info = lib.get_info(key)  # Get updated info
            video_details = (f"{updated_info['name']}\n"
                             f"New rating: {updated_info['rating']}\n"
                             f"plays: {updated_info['play_count']}")
            set_text(self.status_txt, video_details)
        else:
            set_text(self.status_txt, f"Video {key} not found")

        self.status_lbl.configure(text="Update Rating button was clicked!")

# Main program execution
if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()  # Assuming fonts.configure() sets up necessary fonts
    UpdateVideos(window)
    window.mainloop()
