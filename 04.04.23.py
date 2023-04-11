import random
import time
def chek_time(f):
    def wrapper(list):
        start = time.time()
        f(list)
        end = time.time() - start
        print(end)
    return wrapper
@chek_time
def foo1(array):
    for i in array:
        print(i,end=' ')
    print()
@chek_time
def foo2(array):
     for i in range(0,len(array),2):
         print(array[i],end=' ')
     print()
if __name__ == '__main__':
    list=[random.randint(1,9) for i in range(100)]
    foo1(list)
    foo2(list)

    chek_time(foo1)
    chek_time(foo2)
def hashKog(f):
    def wrapper(self):
        print(self.__hash__())
        f(self)

    return wrapper


class Stydent:

    def __init__(self, name, group):
        self.name = name
        self.group = group

    @hashKog
    def show(self):
        print(self.name, self.group)


if __name__ == '__main__':
    f = Stydent('za', '1a')
    f.show()

import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def getS(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Figure):
    def __init__(self, r):
        self.__radius = r

    def getS(self):
        return math.pi * self.__radius * 2

    def draw(self):
        print('circle')


class Retembel(Figure):
    def __init__(self, w, h):
        self.__width = w
        self.__heigt = h

    def getS(self):
        return self.__heigt * self.__width

    def drow(self):
        print("Retembel")


if __name__ == '__main__':
    f = Retembel(2, 5)
    f2 = Circle(3)
    f.draw()
    print(f.getS())
    f2.draw()
    print(f2.getS())



from abc import ABC, abstractmethod


class Vegetables(ABC):
    def __init__(self, weight):
        self.__weight = weight

    @staticmethod
    def wash():
        print("МЫТЬ")
    @abstractmethod
    def cook(self):
        pass

class Сucumbers(Vegetables):




    def cook(self):
        print(f'вес {self.__weight}')


class Tomatoes(Vegetables):




    def cook(self):
        print(f'вес {self.__weight}')


if __name__ == '__main__':
    o1 = Сucumbers(123)
    o = Tomatoes(177)
    o.cook()
    o1.cook()
    print(o1.cook())
    print(o.cook())
