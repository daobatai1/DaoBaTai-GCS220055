import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Delete current text
    text_area.insert(tk.END, content)  # Insert new content

class CheckVideos:
    def __init__(self, window):
        window.geometry("750x400")  # Increase the window height to 400
        window.title("Check Videos")
        window.configure(bg="#323232")  # Set the background color to a dark gray

        # "List All Videos" button
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked, bg="#555555", fg="#FFFFFF", font=("Helvetica", 12))
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label and entry for video number input
        enter_lbl = tk.Label(window, text="Enter Video Number", bg="#323232", fg="#FFFFFF", font=("Helvetica", 12))
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        self.input_txt = tk.Entry(window, width=3, font=("Helvetica", 12))
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # "Check Video" button
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked, bg="#555555", fg="#FFFFFF", font=("Helvetica", 12))
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # Text areas for listing videos and displaying video details
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", bg="#555555", fg="#FFFFFF", font=("Helvetica", 12))
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        self.video_txt = tk.Text(window, width=24, height=6, wrap="none", bg="#555555", fg="#FFFFFF", font=("Helvetica", 12))  # Increased height to 6
        self.video_txt.grid(row=1, column=3, columnspan=2, sticky="NW", padx=10, pady=10)

        # Status Label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="#323232", fg="#FFFFFF")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_videos_clicked()  # Automatically list videos on startup

    # Handle "Check Video" button click
    def check_video_clicked(self):
        key = self.input_txt.get()  # Get video number
        info = lib.get_info(key)
        if info:
            video_details = (f"{info['name']}\n"
                             f"{info['director']}\n"
                             f"type: {info['genre']}\n"
                             f"rating: {info['rating']}\n"
                             f"plays: {info['play_count']}")
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    # Handle "List All Videos" button click
    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

# Main program execution
if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()  # Assuming fonts.configure() sets up necessary fonts
    CheckVideos(window)
    window.mainloop()
