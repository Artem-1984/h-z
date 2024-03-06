import abc
from typing import List, Deque,Dict
import logging
import random
import re




class ICommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def positive(self):
        pass

    @abc.abstractmethod
    def negative(self):
        pass


class Conveyor:
    def on(self):
        print("Конвейер запущен ")

    def off(self):
        print('Конвейер остановлен ')

    def speed_increase(self):
        print("Увеличина скорость конвейра")

    def speed_decrease(self):
        print("Уменьшина скорость конвейра")


class ConveyorWorkCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.on()

    def negative(self):
        self.conveyor.off()


class ConveyerAdjustCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.speed_increase()

    def negative(self):
        self.conveyor.speed_decrease()


class Multipult:
    def __init__(self):
        self.__comands: List[ICommand] = [None, None]
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command: ICommand):
        self.__comands[button] = command

    def press_on(self, button: int):
        self.__comands[button].positive()
        self.__history.append(self.__comands[button])

    def press_cancel(self):
        if len(self.__history) != 0:
            self.__history.pop().negative()


if __name__ == '__main__':
    conveyor = Conveyor()
    multipult = Multipult()

    multipult.set_command(0, ConveyorWorkCommand(conveyor))
    multipult.set_command(1, ConveyerAdjustCommand(conveyor))
    multipult.press_on(0)
    multipult.press_on(1)
    multipult.press_cancel()
    multipult.press_cancel()
    multipult.press_cancel()


class ICount(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def amount(self, num):
        pass

    @abc.abstractmethod
    def maximum(self):
        pass

    @abc.abstractmethod
    def minimum(self):
        pass


class Count(ICount):
    def __init__(self, ):
        self.datas = []
        self.count = 1
        self.lst = [ ]


    def get_data(self):
        with open("random_number", 'r', encoding='utf-8') as f:
            num = f.read()
        match = re.findall(r'\b\d{1,3}\b', num)
        for _ in range(5):
            self.datas.append(match[random.randint(1,300)])
        return self.datas

    def amount(self):

        for i in (self.datas):
            self.count += int(i)
        self.lst.append(self.count)
        return self.count


    def maximum(self):
        cnt = 0
        for i in (self.datas):
            if cnt < int(i):
                cnt = int(i)
        self.lst.append(cnt)
        return cnt




    def minimum(self):
        cnt = 1000

        for i in (self.datas):
            if cnt > int(i):
                cnt = int(i)
        self.lst.append(cnt)
        return cnt



class CountProxy(Count):


    def logging(self):
        logging.basicConfig(level=logging.DEBUG,encoding='utf-8', filename='new_fail.log', format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
        logging.info('Операция выполнена')

    def amount1(self):
        return self.lst

a1 = CountProxy ()
a1.get_data()
a1.amount()
a1.maximum()
a1.minimum()
a1.logging()
print(a1.amount1())
