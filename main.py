import threading
import requests
from ttkbootstrap import Window, Label, Entry, Button
from ttkbootstrap.dialogs import Messagebox

window = Window(title="Download Manager")
window.grid_columnconfigure(1, weight=1)

url_label = Label(window, text="URL")
url_label.grid(row=0, column=0, pady=10, padx=10, sticky="e")

url_entry = Entry(window, width=100)
url_entry.grid(row=0, column=1, pady=10, padx=(0, 20), sticky="ew")


def download(url):
    response = requests.get(url)
    if response.ok:
        with open(r"C:\Users\ASUS\Downloads\Sematec.mp4", mode="wb") as video_file:
            video_file.write(response.content)



def download_button_clicked():
    url = url_entry.get()
    download_thread = threading.Thread(target=download, args=(url,))
    download_thread.start()
    download_thread.join()  # wait until the thread do its job, then show this message box
    Messagebox.show_info(title="Info", message="Has been Downloaded.")


download_button = Button(window, text="Download", command=download_button_clicked)

download_button.grid(row=1, column=1, pady=(0, 10), sticky="w")
window.mainloop()
