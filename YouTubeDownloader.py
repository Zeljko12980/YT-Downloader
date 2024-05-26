import tkinter as tk
from pytube import YouTube

def download_video():
    link = url_entry.get()
    video = YouTube(link)
    high_res_stream = video.streams.get_highest_resolution()
    file_path = high_res_stream.download()
    status_label.config(text="Downloaded successfully: " + file_path)

# Kreiranje GUI prozora
root = tk.Tk()
root.title("YouTube Downloader")

# Unos URL-a
url_label = tk.Label(root, text="Paste the URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Dugme za preuzimanje
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Statusna poruka
status_label = tk.Label(root, text="")
status_label.pack()

# Pokretanje GUI petlje
root.mainloop()
