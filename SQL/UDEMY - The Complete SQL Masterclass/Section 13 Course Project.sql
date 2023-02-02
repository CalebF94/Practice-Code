/*
Section 13: Course Project
*/

/*
Task 1
*/

	DROP TABLE employees;
	-- Task 1.1
	-- Create a table called employees
		CREATE TABLE IF NOT EXISTS employees(
			emp_id SERIAL PRIMARY KEY,
			first_name VARCHAR(20) NOT NULL,
			last_name VARCHAR(20) NOT NULL,
			job_position VARCHAR(20) NOT NULL,
			salary numeric(8,2),
			start_date date NOT NULL,
			birth_date date NOT NULL,
			store_id integer , 
			department_id integer,
			manager_id integer
		);
	
	DROP TABLE departments;
	-- Task 1.2
	-- Set up another table called departments
		CREATE TABLE IF NOT EXISTS departments(
			department_id SERIAL PRIMARY KEY,
			department VARCHAR(30) NOT NULL,
			division VARCHAR(30) NOT NULL
		);

/*
Task 2

Alter the employees table in the following ways:
	-- set department_id to not null
	-- add a default value of CURRENT_DATE to the start_date column
	-- Add the the column end_date with an appropriate data type
	-- Add constraint called birth_check that doesn't allow birth dates that are in the future
	-- rename job_position to position_title
*/
	ALTER TABLE employees
		ALTER COLUMN department_id SET NOT NULL,
		ALTER COLUMN start_date SET DEFAULT CURRENT_DATE,
		ADD COLUMN end_date DATE,
		ADD CONSTRAINT birth_check CHECK(birth_date <= CURRENT_DATE); --had to add CHECK()
		
	-- had to add an additional alter table statement to rename columns
	ALTER TABLE employees
		RENAME COLUMN job_position TO position_title;


/*
Task 3.1:
	--Try to insert values into employees table. There will be an error; fix error
*/

	INSERT INTO employees
		(emp_id,first_name,last_name,position_title,salary,start_date,birth_date,store_id,department_id,manager_id,end_date)
	VALUES
		(1,'Morrie','Conaboy','CTO',21268.94,'2005-04-30','1983-07-10',1,1,NULL,NULL),
		(2,'Miller','McQuarter','Head of BI',14614.00,'2019-07-23','1978-11-09',1,1,1,NULL),
		(3,'Christalle','McKenny','Head of Sales',12587.00,'1999-02-05','1973-01-09',2,3,1,NULL),
		(4,'Sumner','Seares','SQL Analyst',9515.00,'2006-05-31','1976-08-03',2,1,6,NULL),
		(5,'Romain','Hacard','BI Consultant',7107.00,'2012-09-24','1984-07-14',1,1,6,NULL),
		(6,'Ely','Luscombe','Team Lead Analytics',12564.00,'2002-06-12','1974-08-01',1,1,2,NULL),
		(7,'Clywd','Filyashin','Senior SQL Analyst',10510.00,'2010-04-05','1989-07-23',2,1,2,NULL),
		(8,'Christopher','Blague','SQL Analyst',9428.00,'2007-09-30','1990-12-07',2,2,6,NULL),
		(9,'Roddie','Izen','Software Engineer',4937.00,'2019-03-22','2008-08-30',1,4,6,NULL),
		(10,'Ammamaria','Izhak','Customer Support',2355.00,'2005-03-17','1974-07-27',2,5,3,'2013-04-14'),
		(11,'Carlyn','Stripp','Customer Support',3060.00,'2013-09-06','1981-09-05',1,5,3,NULL),
		(12,'Reuben','McRorie','Software Engineer',7119.00,'1995-12-31','1958-08-15',1,5,6,NULL),
		(13,'Gates','Raison','Marketing Specialist',3910.00,'2013-07-18','1986-06-24',1,3,3,NULL),
		(14,'Jordanna','Raitt','Marketing Specialist',5844.00,'2011-10-23','1993-03-16',2,3,3,NULL),
		(15,'Guendolen','Motton','BI Consultant',8330.00,'2011-01-10','1980-10-22',2,3,6,NULL),
		(16,'Doria','Turbat','Senior SQL Analyst',9278.00,'2010-08-15','1983-01-11',1,1,6,NULL),
		(17,'Cort','Bewlie','Project Manager',5463.00,'2013-05-26','1986-10-05',1,5,3,NULL),
		(18,'Margarita','Eaden','SQL Analyst',5977.00,'2014-09-24','1978-10-08',2,1,6,'2020-03-16'),
		(19,'Hetty','Kingaby','SQL Analyst',7541.00,'2009-08-17','1999-04-25',1,2,6,NULL),
		(20,'Lief','Robardley','SQL Analyst',8981.00,'2002-10-23','1971-01-25',2,3,6,'2016-07-01'),
		(21,'Zaneta','Carlozzi','Working Student',1525.00,'2006-08-29','1995-04-16',1,3,6,'2012-02-19'),
		(22,'Giana','Matz','Working Student',1036.00,'2016-03-18','1987-09-25',1,3,6,NULL),
		(23,'Hamil','Evershed','Web Developper',3088.00,'2022-02-03','2012-03-30',1,4,2,NULL),
		(24,'Lowe','Diamant','Web Developper',6418.00,'2018-12-31','2002-09-07',1,4,2,NULL),
		(25,'Jack','Franklin','SQL Analyst',6771.00,'2013-05-18','2005-10-04',1,2,2,NULL),
		(26,'Jessica','Brown','SQL Analyst',8566.00,'2003-10-23','1965-01-29',1,1,2,NULL);

/*
Task 3.2:
	-- Insert values into departments table
*/
	INSERT INTO departments 
		(department_id, department, division)
	VALUES
		(1, 'Analytics', 'IT'),
		(2, 'Finance', 'Administration'),
		(3, 'Sales', 'Sales'),
		(4, 'Website', 'IT'),
		(5, 'Back Office', 'Administration');


/*
TASK 4.1:
	-- Jack Franklin gets promoted to 'Senior SQL Analyst' and salary raises to 72000
	-- update values accordingly
*/

	UPDATE employees
	SET position_title = 'Senior SQL Analyst',
		salary = 72000
	WHERE first_name = 'Jack' AND last_name = 'Franklin';

	--Checking update
	SELECT * FROM employees WHERE first_name = 'Jack' AND last_name = 'Franklin';


/*
TASK 4.2:
	-- rename the position 'Customer Support' to 'Customer Specialist'
	-- update values accordingly
*/
	UPDATE employees
	SET position_title = 'Customer Specialist'
	WHERE position_title = 'Customer Support'
	
	SELECT * FROM employees WHERE position_title = 'Customer Specialist'


/*
TASK 4.3:
	-- Give SQL analyst a raise of 6%
*/

	UPDATE employees 
	SET salary = salary*1.06
	WHERE position_title IN ('Senior SQL Analyst', 'SQL Analyst');


/*
TASK 4.4:
	-- What is average salary of SQL analyst in company(exclude senior SQL analyst)
*/
	SELECT 
		ROUND(AVG(salary), 2)
	FROM employees
	WHERE position_title = 'SQL Analyst';


/*
Task 5.1
-- write a query that adds a column called manager that contains first_name and last_name
-- secondly, add a column called is_active with false if the employee has left the company
   already, otherwise the value is 'true'
*/
SELECT 
	e1.*,
	e2.first_name ||' '|| e2.last_name as manager,
	CASE WHEN e1.end_date IS NULL THEN 'true' ELSE 'false' END as is_active
FROM 
	employees as e1
	LEFT JOIN employees as e2
		ON e1.manager_id = e2.emp_id;


/*
Task 5.2
-- Create a view from the previous query
*/
	DROP VIEW v_employees_info;

	CREATE VIEW v_employees_info AS
		SELECT 
			e1.*,
			e2.first_name ||' '|| e2.last_name as manager,
			CASE WHEN e1.end_date IS NULL THEN 'true' ELSE 'false' END as is_active
		FROM 
			employees as e1
			LEFT JOIN employees as e2
				ON e1.manager_id = e2.emp_id;

	SELECT * FROM v_employees_info;
	
	
/*
Task 6
-- Write a query that returns the average salaries for each positions with appropriate roundings
*/
	SELECT 
		position_title,
		ROUND(AVG(salary), 2) as avg_sal
	FROM employees
	GROUP BY position_title;
	
		
/*
Task 7
-- Write a query that returns the average salaries per division
*/
	SELECT 
		d.division,
		ROUND(AVG(salary), 2) as avg_salary
	FROM 
		employees as e 
		LEFT JOIN departments as d
			ON e.department_id = d.department_id
	GROUP BY d.division;


/*
Task 8.1
-- Write a quere that returns emp_id, first_name, last_name, position_title, salary
-- add a column that returns the aveg salary for every job position
*/
	SELECT 
		emp_id,
		first_name,
		last_name,
		position_title,
		salary,
		ROUND(AVG(salary) OVER(PARTITION BY position_title), 2)
	FROM 
		v_employees_info
	ORDER BY emp_id;



/*
Task 8.2
-- How many people earn less than their avg_position_salary
*/

SELECT 
	*
FROM
	(SELECT 
			emp_id,
			first_name,
			last_name,
			position_title,
			salary,
			ROUND(AVG(salary) OVER(PARTITION BY position_title), 2) as pos_avg
		FROM 
			v_employees_info
		ORDER BY emp_id) as q1
WHERE
	pos_avg > salary;



/*
Task 9
-- Write a query that returns a running total of the salary development 
   ordered by start_date
*/
SELECT
	emp_id,
	salary,
	start_date,
	SUM(salary) OVER(ORDER BY start_date)
FROM 
	employees;


/*
Task 10
-- Create the same running total but now also consider the fact that people were
   leaving the company
*/
SELECT
	emp_id,
	start_date
	salary,
	
	SELECT 
	 	*,
	 	CASE WHEN end_date IS NULL THEN salary ELSE -salary END as contribution
	FROM employees
	ORDER BY start_date



