import threading
import random



lst = []

def random_lst():
    lst.append(random.randint(1, 100))
    print(lst)


for i in range(random.randint(1, 20)):
    t = threading.Thread(target=random_lst)
    t.start()
    t.join()


def sum_lst(lst):
    sum_num = 0
    for _ in lst:
        sum_num += _
    print(sum_num)


def sr_lst(lst):
    num = map(int, lst)
    sr = sum(num) / len(lst)
    print(sr)


t1 = threading.Thread(target=sum_lst, args=(lst,))
t1.start()
t1.join()

t2 = threading.Thread(target=sr_lst, args=(lst,))
t2.start()