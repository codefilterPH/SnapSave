import tkinter as tk
from create_backup import copy_folder
from unzip import run_unzip


def create_app_window():
    window = tk.Tk()
    window.title("Snap Unzipper")

    label = tk.Label(window, text="Click the button to run a backup or restore a backup.")
    label.pack(pady=10)

    button = tk.Button(window, text="Run Quick Backup", command=lambda: copy_folder(message_text))
    button.pack(pady=10)

    button = tk.Button(window, text="Select Backup Zip", command=lambda: run_unzip(message_text))
    button.pack(pady=10)

    global message_text
    message_text = tk.Text(window, height=10, width=60)
    message_text.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    create_app_window()
