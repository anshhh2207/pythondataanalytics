use dd1;

CREATE TABLE employzz (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(30),
    city VARCHAR(30),
    salary DECIMAL(10,2),
    experience INT,
    age INT
);
INSERT INTO employzz 
(employee_id, employee_name, department, city, salary, experience, age)
VALUES
(1, 'Arun Kumar', 'IT', 'Kochi', 55000, 3, 25),
(2, 'Anjali Nair', 'HR', 'Calicut', 42000, 2, 24),
(3, 'Rahul Das', 'IT', 'Bangalore', 75000, 6, 30),
(4, 'Sneha Thomas', 'Finance', 'Kochi', 62000, 5, 28),
(5, 'Vishnu Raj', 'IT', 'Calicut', 68000, 4, 27),
(6, 'Fathima Ali', 'HR', 'Kochi', 48000, 3, 26),
(7, 'Nikhil Menon', 'Finance', 'Bangalore', 80000, 7, 32),
(8, 'Amal Dev', 'IT', 'Kochi', 59000, 4, 26),
(9, 'Meera Joseph', 'HR', 'Bangalore', 51000, 5, 29),
(10, 'Sanjay Kumar', 'Finance', 'Calicut', 57000, 3, 25),
(11, 'Anu Krishnan', 'IT', 'Bangalore', 72000, 5, 29),
(12, 'Ramesh Babu', 'HR', 'Kochi', 45000, 2, 23),
(13, 'Akhil Raj', 'Finance', 'Kochi', 67000, 4, 27),
(14, 'Neha Suresh', 'IT', 'Calicut', 63000, 3, 25),
(15, 'Manu Mohan', 'HR', 'Calicut', 46000, 2, 24);

SELECT * FROM employzz ;

SELECT COUNT(*)  FROM employzz;

SELECT SUM(salary)  FROM employzz;

SELECT AVG(salary) FROM employzz;

SELECT MAX(salary) FROM employzz;

SELECT MIN(salary) FROM employzz;

SELECT *FROM employzz WHERE department IN ('IT', 'HR');

SELECT *FROM employzz WHERE city IN ('Kochi', 'Calicut');

SELECT * FROM employzz WHERE salary IN (55000, 62000, 75000);

SELECT *FROM employzz WHERE employee_name LIKE 'A%';

SELECT *FROM employzz WHERE employee_name LIKE '%n';

SELECT *FROM employzz WHERE employee_name LIKE '%ar%';

SELECT *FROM employzz WHERE city LIKE 'K%';

SELECT *FROM employzz WHERE employee_name LIKE 'A___';

SELECT *FROM employzz WHERE employee_name LIKE '_____';

SELECT DISTINCT city FROM employzz WHERE city LIKE '_o%';

