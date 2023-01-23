/*
SECTION 11: WINDOW FUNCTIONS

GREENCYCLES CHALLENGES
*/

/*
CHALLENGE: OVER() WITH PARTITION BY

-- Write a query that returns the list of movies including
	- film_id, title, length, category, avg length of movies in that category
	- Order the results by film_id
*/

SELECT 
	f.film_id,
	f.title,
	f.length,
	c.name,
	ROUND(AVG(length) OVER(PARTITION BY c.name), 3) as category_avg_length
FROM
	film as f 
	LEFT JOIN film_category as fc
		ON f.film_id = fc.film_id
	LEFT JOIN category as c
		ON fc.category_id = c.category_id
ORDER BY film_id;
	

/*
CHALLENGE: OVER() WITH PARTITION BY

-- Write a query that returns all payment details including the number of payment
   that were made by this customer and that amount
   
-- order the results by payment_id
*/

SELECT 
	*,
	COUNT(*) OVER(PARTITION BY customer_id, amount)
FROM payment
ORDER BY payment_id





