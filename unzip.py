import os
import shutil
import tkinter as tk
from settings import unzip_config
from tkinter import Tk, filedialog

def unzip_backup_folder(to_path, dir_name, message_text):
    try:
        Tk().withdraw()
        zip_path = filedialog.askopenfilename(title="Select Backup Zip File")

        extraction_path = os.path.join(to_path, dir_name)

        message_text.insert(tk.END, f"Creating extraction folder: {extraction_path}\n")

        os.makedirs(extraction_path, exist_ok=True)

        message_text.insert(tk.END, f"Unzipping folder: {zip_path}\n")

        # Remove existing files before extraction
        for file_name in os.listdir(extraction_path):
            file_path = os.path.join(extraction_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        shutil.unpack_archive(zip_path, extraction_path)

        message_text.insert(tk.END, "Folder successfully unzipped.\n")
        return True
    except Exception as e:
        message_text.insert(tk.END, f"An error occurred: {e}\n")
        return False


def run_unzip(message_text):
    destination_path, folder_name = unzip_config()
    if unzip_backup_folder(destination_path, folder_name, message_text):
        message_text.insert(tk.END, f"Backup folder unzipped to: {os.path.join(destination_path, folder_name)}\n")
    else:
        message_text.insert(tk.END, "Backup folder unzipping failed.\n")
