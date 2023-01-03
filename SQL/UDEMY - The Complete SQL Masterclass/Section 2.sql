-- The Complete SQL Masterclass
-- Udemy Course Challenge/Practice Problems
-- Section 2: Filtering

-------------------------------------------------------------------------------
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
WHERE first_name = 'ERICA';


-------------------------------------------------------------------------------
-- Challenge: WHERE Operators
-- Notes: Options include =, >, <, <=, >=, !=, is null, is not null
-- How many rentals have not been returned yet (return_date is null)(183)
SELECT COUNT(*) 
FROM rental
WHERE return_date is null;

-- List of all payment_ids with an amount less than or equal to $2. (3644 rows)
SELECT payment_id, amount
FROM payment
WHERE amount <= 2.00;

-------------------------------------------------------------------------------
-- Challenge: Where with AND/OR
-- Notes:
-- list of payments for customer 322, 346, and 354 where the amount is either
--   less than $2 or greater than $10
--   Order by customer first then amount descending

SELECT *
FROM payment
WHERE customer_id IN (322, 346, 354)
	AND (amount < 2 OR amount > 10)
ORDER BY 
	customer_id, amount DESC;

-------------------------------------------------------------------------------
-- Challenge: BETWEEN
-- Notes: When using dates in the format "yyyy-mm-dd" the timestamp is assigned
-- to midnight (00:00).

-- How many payments have been made on Jan 26th and 27th 2020 with an amount
-- between 1.99 and 3.99 (101)
SELECT COUNT(*)
FROM payment
WHERE (payment_date BETWEEN '2020-01-26 00:00' AND '2020-01-27 23:59')
	AND (amount BETWEEN 1.99 AND 3.99);


-------------------------------------------------------------------------------
-- Challenge: IN
-- Notes: The IN clause can be used to replace multiple OR conditions

-- Find payments for customers 12, 25, 67, 93, 124, and 234 that occured in
-- January 2022 with the amounts of 4.99, 7.99, and 9.99
SELECT customer_id, payment_id
FROM payment
WHERE (customer_id IN (12, 25, 67, 93, 124, 234))
	   AND (payment_date BETWEEN '2020-01-01' AND '2020-01-31 23:59')
	   AND (amount IN (4.99, 7.99, 9.99));

-------------------------------------------------------------------------------
-- Challenge: LIKE
-- Notes: '_' matches any single character. '%' matches any number of chars
--        Like is case sensitive. ILIKE is case insensitive

-- How many movies are there that contain 'Documentary' in the description (101)
SELECT COUNT(*)
FROM film
WHERE description LIKE '%Documentary%';

-- How many customers have first_name that is 3 letters long with an 'X' or 'Y' as
-- the last letter? (3)
SELECT COUNT(*)
FROM customer
WHERE (first_name LIKE '___')
	AND (last_name LIKE '%Y' OR last_name LIKE '%X');


-------------------------------------------------------------------------------
-- Final Challenges
-- 
-- How many movies contain 'Saga' in the description and the title starts with 
-- either 'A' or end with 'R'? Use the alias 'No_of_Movies' (14)
SELECT COUNT(*) AS no_of_movies
FROM film
WHERE (description LIKE '%Saga%')
	AND (TITLE LIKE 'A%' OR title LIKE '%R');

-- List of customers where first name contains 'ER' and has an 'A' as the 2nd
-- letter. Order results by the last name descending. (5 rows)
SELECT * 
FROM customer
WHERE (first_name LIKE '%ER%') AND (first_name LIKE '_A%')
ORDER BY last_name DESC;

-- How many payments with amount of either 0 or between 3.99 and 7.99 and occurred
-- on 2020-05-01?
SELECT *
FROM payment
WHERE ((amount = 0) OR (amount BETWEEN 3.99 AND 7.99)) 
	AND (payment_date BETWEEN '2020-05-01' AND '2020-05-02');



