/*
CHALLENGE: UPPER,LOWER, and LENGTH
*/
-- Create a list where first_name or last_name is longer than 10 characters
-- make list of names all lower case

SELECT
	LOWER(first_name) as firstname,
	LOWER(last_name) as lastname,
	LOWER(email) as email
FROM customer
WHERE LENGTH(first_name)>10 OR LENGTH(last_name)>10;

/*
CHALLENGE: LEFT and RIGHT
*/
--Extract the last five characters of the email address
SELECT 
	email,
	RIGHT(email, 5) as "Last 5"
FROM
	customer;

-- Extract the . from the email address
SELECT 
	email,
	LEFT(RIGHT(email, 4), 1) as dot
FROM
	customer;

/*
CHALLENGE: CONCATENATE
*/
-- Create an anonymized version of the email address
-- make it of the form M***@sakilacustomer.org (all emails will a have 
-- sakilacustomer.org)
SELECT
	LEFT(first_name, 1) || '***@sakilacustomer.org' as anonymized_email
FROM customer;


/*
CHALLENGE: POSITION
*/
--Only the email and last name columns are to be used
-- extract the first name from the email address and contaenate it with
-- the last name. Put in form "Last name, first name"
SELECT 
	last_name || ', ' || LEFT(email, POSITION('.' IN email)-1) as Name
FROM
	customer;


/*
CHALLENGE: SUBSTRING
*/
-- Create an anonymized version of the email address
-- create one of the form M***.S***@sakilacustomer.org
SELECT
	RIGHT(email, 1) || '***.' || SUBSTRING(email FROM POSITION('.' in email)+1 for 1) || '***' || RIGHT(email, LENGTH(email)-POSITION('@' in email)+1)
FROM
	customer;


-- Create another of the form ***Y.S***@sakilacustomer.org
SELECT 
	'***' || 
	SUBSTRING(email from POSITION('.' IN email)-1 for 3) ||
	'***' || 
	RIGHT(email, LENGTH(email)-POSITION('@' in email)+1)
FROM
	customer


/*
CHALLENGE: EXTRACT
*/
-- What's the month with highest total payment amount? (april)
SELECT
	EXTRACT(month from payment_date) as month,
	SUM(amount) as Amount
FROM 
	payment
GROUP BY month
ORDER BY Amount DESC;

-- What day of week has highest total payment (wednesday)
SELECT
	EXTRACT(dow from payment_date) as day_of_week,
	SUM(amount) as Amount
FROM 
	payment
GROUP BY day_of_week
ORDER BY Amount DESC;


-- What's the highest amount one customer has spent in a week (73.88)
SELECT
	customer_id,
	EXTRACT(week from payment_date) as week,
	SUM(amount) as Amount
FROM 
	payment
GROUP BY customer_id, week
ORDER BY Amount DESC
LIMIT 1;


/*
CHALLENGE: TO CHAR
*/
--Aggregate payments and group by day format day, dd/mm/yyyy
SELECT 
	TO_CHAR(payment_date, 'Dy, dd/mm/yyyy') as "Date",
	SUM(amount) as Amount
FROM payment
GROUP BY "Date";


--Aggregate payments and group by day format month, yyyy
SELECT 
	TO_CHAR(payment_date, 'Mon, yyyy') as "Month",
	SUM(amount) as Amount
FROM payment
GROUP BY "Month";

--Aggregate payments and group by day format dy, hh:mm
SELECT 
	TO_CHAR(payment_date, 'Dy, hh:mi') as "Date",
	SUM(amount) as Amount
FROM payment
GROUP BY "Date";


/*
CHALLENGE: INTERVALS and TIMESTAMPS
*/
--Create a list for all rental durations of customer with id 35
SELECT 
	customer_id,
	return_date-rental_date as rental_length
FROM
	rental
WHERE 
	customer_id = 35;
	
	
-- Find which customer has the longest average rental duration
SELECT
	customer_id,
	AVG(return_date-rental_date) as rental_length,
	COUNT(*) as rentals
FROM rental
GROUP BY customer_id
ORDER BY rental_length;







