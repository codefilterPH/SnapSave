import os
import shutil
import tkinter as tk
from datetime import datetime
from settings import back_up_config


def delete_backup_folder(source_folder, message_text):
    message_text.insert(tk.END, f"Source Folder: {source_folder}\n")
    if os.path.exists(source_folder):
        try:
            shutil.rmtree(source_folder)
            message_text.insert(tk.END, "Backup folder successfully deleted.\n")
            return True
        except Exception as e:
            message_text.insert(tk.END, f"An error occurred while deleting the backup folder: {e}\n")
            return False
    else:
        message_text.insert(tk.END, "Backup folder not found.\n")
        return False


def zip_backup_folder(source_folder, backup_folder_name, message_text):
    try:
        backup_folder_path = os.path.join(os.path.dirname(source_folder), backup_folder_name)
        message_text.insert(tk.END, f"Zipping folder: {backup_folder_path}\n")
        shutil.make_archive(backup_folder_path, 'zip', source_folder)
        message_text.insert(tk.END, "Folder successfully zipped.\n")

        zip_file_path = backup_folder_path + '.zip'
        if os.path.exists(zip_file_path):
            message_text.insert(tk.END, f"Backup folder zipped to: {zip_file_path}\n")
            delete_backup_folder(backup_folder_path, message_text)
            return zip_file_path
        else:
            message_text.insert(tk.END, "Backup folder zipping failed.\n")
            return None
    except Exception as e:
        message_text.insert(tk.END, f"An error occurred: {e}\n")
        return None


def copy_folder(message_text):
    try:
        source_path, destination_path = back_up_config()
        backup_folder_name = os.path.basename(source_path) + "_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        destination_folder = os.path.join(destination_path, backup_folder_name)

        message_text.insert(tk.END, f"Copying from: {source_path}\n")
        message_text.insert(tk.END, f"Saving to: {destination_folder}\n")

        shutil.copytree(source_path, destination_folder)

        if os.path.exists(destination_folder):
            message_text.insert(tk.END, "Folder successfully copied.\n")

            zip_file_path = zip_backup_folder(destination_folder, backup_folder_name, message_text)
            if zip_file_path:
                message_text.insert(tk.END, f"Compressed file created: {zip_file_path}\n")
            else:
                message_text.insert(tk.END, "Backup folder zipping failed.\n")
        else:
            message_text.insert(tk.END, "Folder copy failed.\n")

    except FileExistsError:
        message_text.insert(tk.END, "Destination folder already exists.\n")
        return None
    except Exception as e:
        message_text.insert(tk.END, f"An error occurred: {e}\n")
        return None
