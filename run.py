import os
import shutil
from datetime import datetime
from settings import back_up_config

def delete_backup_folder(source_folder, backup_folder_name):
    print(source_folder)
    if os.path.exists(source_folder):
        try:
            shutil.rmtree(source_folder)
            print("Backup folder successfully deleted.\n")
            return True
        except Exception as e:
            print(f"An error occurred while deleting the backup folder: {e}\n")
            return False
    else:
        print("Backup folder not found.\n")
        return False


def zip_backup_folder(source_folder, backup_folder_name):
    try:
        backup_folder_path = os.path.join(os.path.dirname(source_folder), backup_folder_name)
        print(f"Zipping folder: {backup_folder_path}")
        shutil.make_archive(backup_folder_path, 'zip', source_folder)
        print("Folder successfully zipped.")

        zip_file_path = backup_folder_path + '.zip'
        if os.path.exists(zip_file_path):
            print(f"Backup folder zipped to: {zip_file_path}\n")
            delete_backup_folder(backup_folder_path, backup_folder_name)
            return zip_file_path
        else:
            print("Backup folder zipping failed.\n")
            return None
    except Exception as e:
        print(f"An error occurred: {e}\n")
        return None


def copy_folder(source_folder, destination_folder):
    try:
        backup_folder_name = os.path.basename(source_folder) + "_backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        destination_folder = os.path.join(destination_folder, backup_folder_name)

        print(f"Copying from: {source_folder}")
        print(f"Saving to: {destination_folder}")

        shutil.copytree(source_folder, destination_folder)
        print("Folder successfully copied.\n")

        zip_file_path = zip_backup_folder(destination_folder, backup_folder_name)
        if zip_file_path:
            return zip_file_path
        else:
            return None

    except FileExistsError:
        print("Destination folder already exists.\n")
        return None
    except Exception as e:
        print(f"An error occurred: {e}\n")
        return None


source_path, destination_path = back_up_config()
compressed_file_path = copy_folder(source_path, destination_path)
if compressed_file_path:
    print(f"Compressed file created: {compressed_file_path}")
else:
    print("Backup folder zipping failed.")
