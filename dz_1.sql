-- Задача 1
1. Создайте таблицу с мобильными телефонами, используя графический интерфейс. Необходимые поля таблицы: product_name (название товара), manufacturer (производитель), 
product_count (количество), price (цена). Заполните БД произвольными данными.
Create Table: new_table
{product_name:VARCHAR(45),
manufacturer:VARCHAR(45),
product_count:INT
price:INT }
insert
{15 pro:iphone:10:150000,
8:iphone:11:20000,
A7:honor:100:25000,
S22:samsung:20:50000,
S23:samsung:35:70000,
Techo-10:LG:70:30000,
Xr:iphone:50:100000}



-- Задача 2
-- Напишите SELECT-запрос, который выводит название товара, производителя и цену для товаров, количество которых превышает 2
SELECT product_name, manufacturer,price,  product_count > 50 as count
FROM mobile_number.new_table;
-- Сделал 50,а не 2...


-- Задача 3
-- Выведите SELECT-запросом весь ассортимент товаров марки “Samsung”
SELECT *
FROM mobile_number.new_table
WHERE manufacturer = 'samsung';

-- Задача 4
-- Товары, в которых есть упоминание "Iphone"
SELECT *
FROM mobile_number.new_table
WHERE manufacturer LIKE 'iphone';

-- Задача 5
-- Товары, в которых есть упоминание "Samsung"
SELECT *
FROM mobile_number.new_table
WHERE manufacturer LIKE 'samsung';

-- Задача 6
-- Товары, в названии которых есть ЦИФРЫ
SELECT *
FROM mobile_number.new_table
WHERE product_name  REGEXP '[0-9]';
-- Задача 7
-- Товары, в названии которых есть ЦИФРА "8"
SELECT *
FROM mobile_number.new_table
WHERE product_name REGEXP '[8]';