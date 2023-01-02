-- The Complete SQL Masterclass
-- Udemy Course Challenge/Practice Problems
-- Section 1

-- Challenge: Order By
-- Select all customer first and last names and emails
-- Sort the results by desc last name and desc first name
SELECT 
	first_name,
	last_name,
	email
FROM customer
ORDER BY last_name desc, first_name desc;


-- Challenge: DISTINCT
-- Notes: this statement means distinct across all columns
-- Get a list of all amounts that have been paid
-- sort results from high to low
SELECT DISTINCT
	amount
FROM payment
ORDER BY amount DESC;


-- Challenges For Section 1
-- 1) Create a list of all the distinct districts customers are from
SELECT DISTINCT district
FROM address;

-- 2) What is the latest rental date?
SELECT rental_date
FROM rental
ORDER BY rental_date DESC
LIMIT 1;

-- 3) How many films does the company have?
SELECT COUNT(*), COUNT(film_id)
FROM film;

-- 4) How many distinct last names of the customers are there
SELECT COUNT(DISTINCT last_name)
FROM customer;