-- Задача 1
1. Создайте таблицу с мобильными телефонами, используя графический интерфейс. Необходимые поля таблицы: product_name (название товара), manufacturer (производитель), 
product_count (количество), price (цена). Заполните БД произвольными данными.
CREATE SCHEMA `mobile_phone` ;
CREATE TABLE `mobile_phone`.`new_table` (
  `product_name` VARCHAR(45) NOT NULL,
  `manufacturer` VARCHAR(45) NOT NULL,
  `product_count` INT NOT NULL,
  `price` INT NULL,
  PRIMARY KEY (`product_name`));
INSERT INTO `mobile_phone`.`new_table` (`product_name`, `manufacturer`, `product_count`, `price`) VALUES ('Xr', 'Iphone', '3', '30000');
INSERT INTO `mobile_phone`.`new_table` (`product_name`, `manufacturer`, `product_count`, `price`) VALUES ('15', 'Iphone', '1', '100000');
INSERT INTO `mobile_phone`.`new_table` (`product_name`, `manufacturer`, `product_count`, `price`) VALUES ('S22', 'Samsung', '5', '40000');
INSERT INTO `mobile_phone`.`new_table` (`product_name`, `manufacturer`, `product_count`, `price`) VALUES ('S23', 'Samsung', '3', '70000');
INSERT INTO `mobile_phone`.`new_table` (`product_name`, `manufacturer`, `product_count`, `price`) VALUES ('A10', 'Honor', '7', '20000');
INSERT INTO `mobile_phone`.`new_table` (`product_name`, `manufacturer`, `product_count`, `price`) VALUES ('8', 'Iphone', '9', '15000');
INSERT INTO `mobile_phone`.`new_table` (`product_name`, `manufacturer`, `product_count`, `price`) VALUES ('Techo 10', 'Poco', '6', '35000');



-- Задача 2
-- Напишите SELECT-запрос, который выводит название товара, производителя и цену для товаров, количество которых превышает 2
SELECT product_name,manufacturer,price 
FROM mobile_phone.new_table
WHERE product_count > 2;

-- Задача 3
-- Выведите SELECT-запросом весь ассортимент товаров марки “Samsung”
SELECT * 
FROM mobile_phone.new_table
WHERE  manufacturer = 'Samsung';
-- Задача 4
-- Товары, в которых есть упоминание "Iphone"
SELECT * 
FROM mobile_phone.new_table
WHERE manufacturer LIKE 'Iphone';


-- Задача 5
-- Товары, в которых есть упоминание "Samsung"
SELECT *
FROM mobile_phone.new_table
WHERE manufacturer LIKE 'Samsung';

-- Задача 6
-- Товары, в названии которых есть ЦИФРЫ
SELECT * 
FROM mobile_phone.new_table
WHERE product_name REGEXP  '[A-Z a-z] [0-9]';
-- Задача 7
-- Товары, в названии которых есть ЦИФРА "8"
SELECT *
FROM mobile_number.new_table
WHERE product_name LIKE '%8%';