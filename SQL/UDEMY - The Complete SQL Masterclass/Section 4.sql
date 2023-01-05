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

