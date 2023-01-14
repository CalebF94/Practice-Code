/*
SECTION 7 CHALLENGES: UNIONS AND SUBQUERIES

These challenges use the greencycles database
*/


/*
CHALLENGE: Subqueries in WHERE
*/
--Select all films where the length is longer than the average film length

SELECT title, length 
FROM film
WHERE length > (SELECT AVG(length) FROM film)
ORDER by length;

-- Return all the films that are available in the inventory in store 2 more than 
--  3 times
SELECT 
	film_id,
	title
FROM film
WHERE film_id IN (SELECT film_id
	 				FROM inventory
	 				WHERE store_id = 2
					GROUP BY film_id
					HAVING COUNT(*) > 3);


/*
CHALLENGE: More Challenges Subqueries in WHERE

--Return all customers first names and last names that have made a 
payment on 2020-01-25
*/
SELECT 
	first_name,
	last_name
FROM customer
WHERE customer_id IN (SELECT DISTINCT customer_id 
					  FROM payment 
					  WHERE CAST(payment_date AS DATE) = '2020-01-25')


-- Return customers first name and emails that have spent more than $30
SELECT 
	first_name,
	last_name,
	email
FROM
	customer
WHERE customer_id IN (SELECT customer_id
					  FROM payment
					  GROUP BY customer_id
					  HAVING SUM(amount) > 30)

-- Return customer first and last names that are from california and have spent more
-- than 100 in total
SELECT 
	c.first_name,
	c.last_name,
	a.district
FROM customer as c LEFT JOIN address as a
	ON c.address_id = a.address_id
WHERE a.district = 'California' 
	AND c.customer_id IN (SELECT customer_id
						  FROM payment
						  GROUP BY customer_id
						  HAVING sum(amount)>100)
ORDER BY c.first_name;



/*
CHALLENGE: Subquery in the FROM Clause

-- What is the average total amount spent per day (average daily revenue)
*/
SELECT ROUND(AVG(daily_total), 2) as avg_daily_total
FROM (SELECT 
	  	DATE(payment_date), 
		SUM(amount) as daily_total
	  FROM payment
	  GROUP BY DATE(payment_date)) as daily_rev;


/*
CHALLENGE: Subquery in the SELECT Clause

-- Show all the payments together with how much the payment amount is below
-- the maximum payment amount
*/
SELECT 
	payment_id, 
	amount, 
	(SELECT MAX(amount) FROM payment),
	(SELECT MAX(amount) FROM payment)-amount as difference
FROM payment;


/*
CHALLENGE: CORRELATED SUBQUERY IN WHERE

-- Show only those payments that have the highest amount per customer
*/
SELECT 
	customer_id,
	payment_id,
	amount
FROM payment as p1
WHERE p1.amount = (SELECT MAX(amount)
				   FROM payment as p2
				   WHERE p1.customer_id = p2.customer_id)
ORDER BY p1.customer_id;


-- Show only those movie titles, their associated film_id and replacement_cost with
-- the lowest replacement_costs for each rating category - also show the rating

SELECT 
	title,
	film_id, 
	replacement_cost,
	rating
FROM
	film as f1
WHERE f1.replacement_cost = (SELECT MIN(replacement_cost)
							 FROM film as f2
							 WHERE f1.rating = f2.rating
							 )
ORDER BY rating;




-- SHow only movie titles , film id and the length that have the highest length in each
-- rating category
SELECT 
	title,
	film_id, 
	length,
	rating
FROM
	film as f1
WHERE f1.length = (SELECT MAX(length)
							 FROM film as f2
							 WHERE f1.rating = f2.rating
							 )
ORDER BY rating;


/*
Lecture 140 Example: Correlated subquery in SELECT

Show the maximum for every customer
*/
SELECT 
	*, (SELECT MAX(amount)
	    FROM payment as p2
	    WHERE p1.customer_id = p2.customer_id
	   )
FROM payment as P1
ORDER BY customer_id;


/*
MORE CHALLENGES: Correlated Subqueries #1

Show all payments plus the total amount for every customer as well
as the number of payments of each customer
*/
SELECT 
	*, 
	(SELECT SUM(amount) 
	 FROM payment p2 
	 WHERE p1.customer_id = p2.customer_id) as sum_amount,
	(SELECT COUNT(*)
	 FROM payment p2
	WHERE p1.customer_id = p2.customer_id) as Num_payments
FROM payment p1
ORDER BY customer_id;


/*
MORE CHALLENGES: Correlated Subqueries #2

Show only those films with the highest replacement costs in their rating
category plus show the average replacement cost in their rating category.
*/
SELECT
	film_id,
	title,
	rating,
	replacement_cost,
	 (SELECT ROUND(AVG(replacement_cost),2)
	 FROM film as f2
	 WHERE f1.rating = f2.rating) as avg_replacement 
FROM 
	film as f1
WHERE f1.replacement_cost = (SELECT MAX(replacement_cost)
							 FROM film as f3
							 WHERE f1.rating = f3.rating)
ORDER BY rating;



/*
MORE CHALLENGES: Correlated Subqueries #3

Show only those payments with the highest payment for each customer's first name
	- including the payment_id of that payment
*/
SELECT 
	c.first_name, p.payment_id, p.amount
FROM payment as p LEFT JOIN customer as c
	ON p.customer_id = c.customer_id
WHERE amount = (SELECT MAX(amount)
			    FROM payment p2 LEFT JOIN customer as c2
					ON p2.customer_id = c2.customer_id
			    WHERE c.first_name = c2.first_name)
ORDER BY first_name;






