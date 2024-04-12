import pymongo

# Задание 1
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#
# mydb = myclient['mydb']
# mycol = mydb['users']
#
# # mydict = [
# #     {"name": "John", "age": "22", "city": "Rostov", "interests": ["football"]},
# #     {"name": "Artem", "age": "18", "city": "Moscow", "interests": ["reading"]},
# #     {"name": "Mike", "age": "37", "city": "Kiew", "interests": ["sumo"]},
# #     {"name": "Catherine", "age": "22", "city": "Rostov", "interests": ["golf"]},
# #     {"name": "Antony", "age": "26", "city": "Seoul", "interests": ["eat"]},
# #     {"name": "Maks", "age": "29", "city": "Tokio", "interests": ["tennis"]}
# #
# # ]
# #
# #
# # x = mycol.insert_many(mydict)
# # print(x.inserted_ids)
#
def task1():
        a = input("Введите имя: ")
        b = int(input("Введите возраст: "))
        myquery = {"name" : a}
        new = {"$inc" : {"age" : b}}
        mycol.update_one(myquery, new)
        for i in mycol.find():
                print(i)



def task2():
        a = input("Введите имя: ")
        b = input("Введите что добавить в хобби : ")
        myquery = {"name": a}
        new = {"$push" : {"interests" : b}}
        mycol.update_one(myquery,new)
        for i in mycol.find():
                print(i)

def task3():
        a = input("Введите имя: ")
        b = (input("Введите город: "))
        myquery = {"name" : a}
        new = {"$set" : {"city" : b}}
        mycol.update_one(myquery, new)
        for i in mycol.find():
                print(i)

while True:
        print("""1.Обновление возвраста.
2.Добавление хобби.
3.Обновление города.
4.Выход из программы.
        """)
        choice = int(input("Введите что хотите исправить: "))
        if choice == 1:
                print(task1())
        elif choice == 2:
                print(task2())
        elif choice == 3:
                print(task3())
        elif choice == 4:
                break
        else:
                print("Нет такой функции")


# Задание 2
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['mydb_2']
mycol = mydb['film']

# myclient = [
#         {'title' : 'avengers', 'release_year' : 2007, 'durector' : 'Anthony Russo',
#          'genre' : 'fantastic','user_rating': 10},
#         {'title' : 'avatar', 'release_year' : 2009, 'durector' : 'James Cameron',
#          'genre' : 'fantastic','user_rating': 8},
#         {'title' : 'The Shawshank Redemption', 'release_year' : 1994, 'durector' : 'Frank Darabont',
#          'genre' : 'Thriller','user_rating': 10},
#         {'title' : 'serf', 'release_year' : 2019, 'durector' : 'Klim Shipenko',
#          'genre' : 'fantastic','user_rating': 3},
#         {'title' : 'Time', 'release_year' : 2011, 'durector' : 'Nikolay Lebedev',
#          'genre' : 'Sport','user_rating': 6},
#         {'title' : 'Legend No. 17', 'release_year' : 2012, 'durector' : 'Anthony Russo',
#          'genre' : 'Sport','user_rating': 7},
#         {'title' : 'Legend No. 17', 'release_year' : 2012, 'durector' : 'Anthony Russo',
#          'genre' : 'Sport','user_rating': 7},
#         {'title' : 'Green Mile', 'release_year' : 1999, 'durector' : 'Frank Darabont',
#          'genre' : 'fantastic','user_rating': 9},
# ]
#
#
# y = mycol.insert_many(myclient)
# print(y.inserted_ids)


def task1():
        f = []
        a = input('Введите жанр: ')
        b = int(input('Введите оценку: '))
        c = int(input('Год выпуска: '))
        myquery = {'genre' : a,'user_rating' :{ '$gt' : b}, 'release_year' : {'$gt' : c}}
        mydoc = mycol.find(myquery)
        for x in mydoc:
                print(x)



print(task1())


# x = mycol.delete_many({})
#
# print(x.deleted_count, " documents deleted.")

