# class Car():
#
#     def __init__(self, m, year, manufacturer, engine, color, price):
#         self.model = m
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     def fields(self,):
#         print('''1.название модели;
# 2.год выпуска;
# 3.производитель;
# 4.объем двигателя;
# 5.цвет машины;
# 6.цена.
# 7.Выход''')
#         while True:
#             a = (input("Что хотите узнать об автомобиле: "))
#             if a == '1':
#                 print(f"Модель:{self.model}")
#                 b=input('Хотите внести измениния?\n')
#                 if b=='нет'.lower():
#                     continue
#                 else:
#                     self.model=input("ведите новое значение:\n")
#             if a == '2':
#                 print(f"Год выпуска:{self.year}")
#                 b = input('Хотите внести измениния?\n')
#                 if b == 'нет'.lower():
#                     continue
#                 else:
#                     self.year = input("ведите новое значение:\n")
#             if a == '3':
#                 print(f'Производитель:{self.manufacturer}')
#                 b = input('Хотите внести измениния?\n')
#                 if b == 'нет'.lower():
#                     continue
#                 else:
#                     self.manufacturer = input("ведите новое значение:\n")
#             if a == '4':
#                 print(f'Обьем двигателя:{self.engine}')
#                 b = input('Хотите внести измениния?\n')
#                 if b == 'нет'.lower():
#                     continue
#                 else:
#                     self.engine = input("ведите новое значение:\n")
#             if a == '5':
#                 print(f'Цвет машины:{self.color}')
#                 b = input('Хотите внести измениния?\n')
#                 if b == 'нет'.lower():
#                     continue
#                 else:
#                     self.color = input("ведите новое значение:\n")
#             if a == '6':
#                 print(f'Цена:{self.price}')
#                 b = input('Хотите внести измениния?\n')
#                 if b == 'нет'.lower():
#                     continue
#                 else:
#                     self.price = input("ведите новое значение:\n")
#             if a == '7':
#                 break
#
#
#
#
#
# car1 = Car("Passat", 2008, 'Germany', 1.8, "silvery", "500 т.р", )
# car1.fields()


class Books():

    def __init__(self, name_books, year_of_issue, publisher, genre, author, price):
        self.name_books = name_books
        self.year_of_issue = year_of_issue
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def fields(self, ):
        print('''1.Название книги;
2.Год выпуска;
3.Издатель;
4.Жанр;
5.Автор;
6.Цена.
7.Выход''')
        while True:
            a = (input("Что хотите узнать о книги: "))
            if a == '1':
                print(f"Название книги:{self.name_books}")
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.name_books = input("ведите новое значение:\n")

            if a == '2':
                print(f"Год выпуска:{self.year_of_issue}")
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.year_of_issue= input("ведите новое значение:\n")
            if a == '3':
                print(f'Издатель:{self.publisher}')
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.publisher = input("ведите новое значение:\n")
            if a == '4':
                print(f'Жанр:{self.genre}')
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.genre= input("ведите новое значение:\n")
            if a == '5':
                print(f'Автор:{self.author}')
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.author = input("ведите новое значение:\n")
            if a == '6':
                print(f'Цена:{self.price}')
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.price = input("ведите новое значение:\n")
            if a == '7':
                break


books1 = Books("1984", 1948, 'Secker and Warburg', 'Научная фантастика', "Джордж Оруэлл", "1000", )
books1.fields()


class Stadium():

    def __init__(self, stadium_name, opening_date, country, city, capacity):
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def fields(self, ):
        print('''1.Название стадиона;
2.Дата открытия;
3.Страна;
4.Город;
5.Вместимость;
6.Выход''')
        while True:
            a = (input("Что хотите узнать о стадионе: "))
            if a == '1':
                print(f"Название стадиона:{self.stadium_name}")
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.stadium_name = input("ведите новое значение:\n")
            if a == '2':
                print(f"Дата открытия:{self.opening_date}")
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.opening_date = input("ведите новое значение:\n")

            if a == '3':
                print(f'Страна:{self.country}')
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.country = input("ведите новое значение:\n")
            if a == '4':
                print(f'Город:{self.city}')
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.city = input("ведите новое значение:\n")
            if a == '5':
                print(f'Вместимость:{self.capacity}')
                b = input('Хотите внести измениния?\n')
                if b == 'нет'.lower():
                    continue
                else:
                    self.capacity = input("ведите новое значение:\n")
            if a == '6':
                break


stadium1 = Stadium('Ростов-арена', 2018, 'Россия', 'Ростов', '50000')
stadium1.fields()
