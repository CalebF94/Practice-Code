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



