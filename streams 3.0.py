import os
import shutil
import threading
import re

search_path = input("Введите директория для поиска: ")
search_word = input("Введите слово для поиска:")

os.chdir(search_path)


def file_search(search_word):
    lst = []
    for file_path in os.listdir():
        if file_path == "new_faile.txt":
            break
        else:
            with open(file_path, 'r',encoding='utf-8') as f:
                text = f.read()


        res = str(re.findall(search_word, str(text)))
        lst.append(f'Файл {file_path}:{res}')

    with open("new_faile.txt", 'a',encoding='utf-8') as f:
        f.write(str(lst))

th1 = threading.Thread(target=file_search, args=[search_word])
th1.start()
th1.join()



