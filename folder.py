def exist_folder(folder_name):
    import os
    if folder_name in os.listdir():
        return True
    
    os.mkdir(folder_name)