import threading
import random
import re
import math

flag = True
while flag:
    path = input("Введите путь к файлу: ")
    if re.findall(r"\.txt$", path):
        text_fail = path
        flag = False
    else:
        print("Файла не существует")


def random_num(text_fail):
    print("Старт первого потока")
    with open(text_fail, "w") as f:
        for _ in range(random.randint(10, 20)):
            num = random.randint(1, 10)
            f.write(str(num) + "\t")
        f.write("\n")
    print("Завершение первого потока")


data = []


def simple(text_fail, data):
    print("Старт второго поток")
    k = 0
    data_fail = []

    with open(text_fail, "r") as f:

        for line in f:
            data.append([int(i) for i in line.split()])
        for _ in data:
            for a in _:
                k = 0
                for i in range(2, a // 2 + 1):
                    if a % i == 0:
                        k = k + 1
                if k <= 0:
                    if a == 1:
                        continue
                    else:
                        data_fail.append(a)
                        k = 0
    with open(text_fail, "a") as f:
        for i in data_fail:
            f.write(str(i) + "\t")
        f.write("\n")
    print("Завершение второго потока")


data_fact = []


def fact(text_fail):
    print("Старт третьего потока")
    with open(text_fail, "r") as f:
        for line in f.readlines(1):
            data_fact.append([int(i) for i in line.split()])
        for _ in data_fact:
            for i in _:
                with open(text_fail, "a") as f:
                    f.write(str(math.factorial(i)) + "\t")
    print("Завершение третьего потока")


t = threading.Thread(target=random_num, args=(text_fail,), daemon=True)
t.start()
t.join()
t1 = threading.Thread(target=simple, args=(text_fail, data))
t1.start()
t1.join()
t2 = threading.Thread(target=fact, args=(text_fail,))
t2.start()
