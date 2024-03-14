-- Задача 1
-- Необходимо создать базу данныхАкадемия (Academy),
-- которая будет содержать информацию о сотрудниках и
-- внутреннем устройстве академии.
-- Описание базыданных находится в конце этогофайла.
DROP DATABASE IF EXISTS Academy;
CREATE DATABASE Academy;
USE Table_1;
DROP TABLE IF EXISTS Departments;
CREATE TABLE Departments
(	
		Departments_id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
	Financing int NOT NULL DEFAULT 0,
    Departments_name  nvarchar(100) NOT NULL UNIQUE
);
INSERT Departments
values
	('1','100000','кафедра Финансового и HR менеджмент'),
	('2','20000','кафедра Общий и стратегический менеджмент'),
	('3','150000','кафедра Инновационный менеджмент и предпринимательство');
SELECT * from Departments; 
DROP TABLE IF EXISTS Faculties;
CREATE TABLE Faculties
(
		Faculties_id int auto_increment not null primary key,
        Dean nvarchar(100) not null ,
        Name_Faculties nvarchar(100) not null UNIQUE
);
INSERT Faculties
values
	('1','Матевосян','Торгового дела'),
	('2','Иванов','Computer Science'),
	('3','Сидоров','Экономики и финансов');
SELECT * from Faculties; 
DROP TABLE IF EXISTS groups_;
CREATE TABLE groups_
(
	groups_id int PRIMARY KEY not null AUTO_INCREMENT ,
    Name_groups nvarchar(10) not null  UNIQUE,
    Rating int not null CHECK(Rating >= 0 AND Rating <= 5),
	Year_groups int not null CHECK(Year_groups >= 1 AND Year_groups <= 5)
);
INSERT groups_
values
	('1','TOPOZ-2110','5.0','2'),
	('2','TOPOZ-2115','4.5','5'),
	('3','TOPOZ-2101','3.0','1');
SELECT * from groups_; 
DROP TABLE IF EXISTS Teachers;
CREATE TABLE Teachers
(
		Teachers_id int AUTO_INCREMENT not null primary key,
        EmploymentDate date not null ,
        IsAssistant bit(64) not null DEFAULT 0,
        IsProfessor bit(64) not null default 0,
        Name_Teachers nvarchar(100) not null,
        Position nvarchar(100) not null,
        Premium int not null check(Premium >= 0),
        Salary int not null check(Salary >= 0),
        Surname nvarchar(100) not null 
);
INSERT Teachers
values
	('1','1999.12.21','да','да','Олег','Профессор','500','1100','Попов'),
	('2','2007.04.12','да','нет','Сергей','Доцент','250','1000','Петров'),
	('3','2017.12.12','нет','нет','Артем','Аспирант','100','700','Сидоров');
SELECT * from Teachers; 


-- Задание 2
-- 1. Вывести таблицу кафедр, но расположить ее поля в
-- обратном порядке.
SELECT Departments_name 
FROM table_1.departments
order by Departments_name desc;
-- 2. Вывести названия групп и их рейтинги с уточнением
-- имен полей именем таблицы.
SELECT Name_groups as groups_Name_groups,Rating as groups_Rating
FROM table_1.groups_;


-- 3. Вывести для преподавателей их фамилию, процент
-- ставки по отношению к надбавке и процент ставки
-- по отношению к зарплате (сумма ставки и надбавки).
SELECT Surname, Salary / Premium * 100 - 100 as  'процент
ставки по отношению к надбавке и', ((Salary+Premium) / Salary) *
100 - 100 as 'процент ставки
по отношению к зарплате'
FROM table_1.teachers;


-- 5. Вывестифамилии преподавателей, которые являются
-- профессорами и ставка которых превышает 1050.
SELECT Surname 
FROM table_1.teachers
WHERE  Surname = 'Профессор' or Salary > 1050;


-- 6. Вывести названия кафедр, фонд финансирования
-- которых меньше 11000 или больше 25000.
SELECT Departments_name 
FROM table_1.Departments
WHERE  Financing <11000  or Financing > 25000;


-- 7. Вывести названия факультетов кроме факультета
-- “Computer Science”.
SELECT Name_Faculties 
FROM table_1.Faculties
WHERE Name_Faculties != 'Computer Science';


-- 8. Вывести фамилии и должности преподавателей,
--  которые не являются профессорами.
SELECT Surname,Position
FROM table_1.Teachers
WHERE Position != 'профессор';


-- 9. Вывести фамилии, должности, ставки и надбавки
-- ассистентов, у которых надбавка в диапазоне от 160
-- до 550.
SELECT Surname,Position,Salary,Premium
FROM table_1.Teachers
WHERE Premium > 160 and Premium <550;


-- 10. Вывести фамилии и ставки ассистентов.
SELECT Surname,Salary
FROM table_1.Teachers
WHERE IsAssistant = 3501510832;


-- 11. Вывести фамилии и должности преподавателей,
--  которые были приняты на работу до 01.01.2000.
SELECT Surname,Position
FROM table_1.Teachers
WHERE EmploymentDate < '2000.01.01';


-- 12. Вывести названия кафедр, которые в алфавитном поment”.
--  Выводимое поле должно иметь название “Nameof Department”
SELECT Departments_name
FROM table_1.Departments
WHERE Departments_name != 'Software Development'
order by Departments_name;


-- 13. Вывести фамилии ассистентов, имеющих зарплату
-- (сумма ставки и надбавки) не более 1200.
SELECT Surname
FROM table_1.Teachers
WHERE IsAssistant = '3501510832' and (Salary + Premium) > 1200;


-- 14. Вывести названия групп 5-го курса, имеющих рейтинг
-- в диапазоне от 2 до 4.
SELECT Name_groups
FROM table_1.groups_
WHERE Year_groups = 5 and 2 < Rating < 4;


-- 15. Вывестифамилии ассистентов со ставкой меньше 550
-- или надбавкой меньше 200.
SELECT Surname
FROM table_1.Teachers
WHERE IsAssistant = '3501510832' and (Salary < 550 or Premium < 200);
