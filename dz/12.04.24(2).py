import os
import shutil
import threading
import re
while True:
    search_path = input("Введите директория для поиска: ")
    if search_path in os.listdir():
        print("Нашел директорию")
        break
    else:
        print("Такой дериктории нет")
search_word = input("Введите слово для поиска:")
with open("mat", 'r', encoding='utf-8') as f1:
    file = f1.read().split()
def cutting_mats(search_word):


    for i in os.listdir():
        if i == "new_faile.txt":
            break
        else:
            with open(i, 'r', encoding='utf-8') as f:
                text = f.read().split()
        for i in text:
            for j in file:
                if i == j:
                    text.remove(i)
    with open(search_path, 'a', encoding='utf-8') as f:
            f.write(str(text))
            f.write('\n')

def file_search(search_word):
    os.chdir(search_path)
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
        f.write('\n')


th1 = threading.Thread(target=file_search, args=[search_word])
th1.start()
th1.join()
th2 = threading.Thread(target=cutting_mats, args=[search_path])
th2.start()


