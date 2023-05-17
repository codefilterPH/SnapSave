
def unzip_config():
    destination_path = r'D:\InventoryMS\RestoredFolder'
    folder_name = 'CommonSql'
    return destination_path, folder_name

def back_up_config():
    source_path = r'\\server\CommonSql'
    destination_path = r'D:\InventoryMS\Backup'
    return source_path, destination_path
