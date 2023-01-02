-- The Complete SQL Masterclass
-- Udemy Course Challenge/Practice Problems
-- Section 2: Filtering

-- Challenge: WHERE
-- Notes: Clause directly follows the FROM clause
-- How many payments were made by the customer with customer_id = 100 (24)
SELECT COUNT(*)
FROM payment
where customer_id = 100;

-- What is the last name of our customer with first name 'ERICA'
-- MATTHEWS
SELECT first_name, last_name
FROM customer
WHERE first_name = 'ERICA'