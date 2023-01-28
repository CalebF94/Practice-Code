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


/*
CHALLENGE: RANK() and DENSE_RANK()

Write a query that returns the customers name, the country and how many payments they have

Afterwards create a ranking of the top customers with most sales for each country. Filter
	results to only the top 3 customers per country
*/

SELECT * 
FROM
	(SELECT 
		cl.name,
		cl.country,
		COUNT(*),
		DENSE_RANK() OVER(PARTITION BY cl.country ORDER BY COUNT(*)) as rnk
	FROM 
		payment as p 
		LEFT JOIN customer_list as cl
			ON p.customer_id = cl.id
	GROUP BY name, country) as sub
WHERE 
	rnk <= 3
ORDER BY country, rnk;

/*
CHALLENGE: LEAD() and LAG()

-- Write a query that returns the revenue of the day and the revenue of the previous day
-- Afterwards calculate the %age growth compared to the previous day
*/
SELECT 
	DATE(payment_date) as day,
	SUM(amount) current_total,
	LAG(SUM(amount)) OVER(ORDER BY DATE(payment_date)) as previous_total,
	ROUND(100*(SUM(amount)-LAG(SUM(amount)) OVER(ORDER BY DATE(payment_date))) / LAG(SUM(amount)) OVER(ORDER BY DATE(payment_date)), 2) as perc_change
FROM payment
GROUP BY day
ORDER BY day;








