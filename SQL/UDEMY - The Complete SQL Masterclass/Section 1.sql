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
