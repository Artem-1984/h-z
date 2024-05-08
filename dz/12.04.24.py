import os
import os.path
import shutil
import threading
def preservation_directories():
    old_path = input('Введите директорию: ')
    if not os.path.exists(old_path):
        print("Директория не существует")
        return
    new_path = input("Введите новую директорию: ")


    shutil.copytree(old_path,new_path)
    print("Содержимое перенесено")



th1 = threading.Thread(target=preservation_directories)
th1.start()
