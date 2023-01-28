/*
SECTION 11: WINDOW FUNCTIONS

GREENCYCLES Lecture Examples
*/
	-- finding the total amount spent by customer_id
	SELECT
		*,
		SUM(amount) OVER(PARTITION BY customer_id),	
	FROM payment;

	--Multiple columns in the partition by statement
	SELECT
		*,
		COUNT(amount) OVER(PARTITION BY customer_id, staff_id)
	FROM payment;
	
	-- Leaving the OVER() function blank aggregates over entire table
	SELECT
		*, 
		ROUND(AVG(amount) OVER(), 2)--notice the round() goes around entire statement
	FROM payment;
		
		
/*
LECTURE 197: OVER() with ORDER BY
*/	

-- Basic example with just a single order by
SELECT 
	*,
	SUM(amount) OVER(ORDER BY payment_date)
FROM payment;

-- Example using PARTITION BY and ORDER BY
SELECT
	*,
	-- running total for each customer, sorted by date and then payment_id
	SUM(amount) OVER(PARTITION BY customer_id
					 ORDER BY payment_date, payment_id)
FROM payment;


/*
LECTURE 200: RANK()
*/
--RANK() Example
SELECT 
	f.title,
	c.name,
	f.length,
	RANK() OVER(ORDER BY f.length desc)
FROM 
	film as f
	LEFT JOIN film_category as fc
		ON f.film_id = fc.film_id
	LEFT JOIN category as c
		ON fc.category_id = c.category_id;

--DENSE_RANK() example
SELECT 
	f.title,
	c.name,
	f.length,
	DENSE_RANK() OVER(ORDER BY f.length desc)
FROM 
	film as f
	LEFT JOIN film_category as fc
		ON f.film_id = fc.film_id
	LEFT JOIN category as c
		ON fc.category_id = c.category_id;


--DENSE_RANK() and PARTITION BY
SELECT 
	f.title,
	c.name,
	f.length,
	DENSE_RANK() OVER(PARTITION BY c.name
					  ORDER BY f.length desc)
FROM 
	film as f
	LEFT JOIN film_category as fc
		ON f.film_id = fc.film_id
	LEFT JOIN category as c
		ON fc.category_id = c.category_id;

--Filting based on rank functions
SELECT * 
FROM
	(SELECT 
		f.title,
		c.name,
		f.length,
		DENSE_RANK() OVER(PARTITION BY c.name
					  		ORDER BY f.length desc) as rnk
	FROM 
		film as f
		LEFT JOIN film_category as fc
			ON f.film_id = fc.film_id
		LEFT JOIN category as c
			ON fc.category_id = c.category_id) as r
WHERE rnk = 1;


/*
LECTURE 203: FIRST_VALUE
*/
-- This is giving the first value for each country and the difference that the second and
--    third customers have compared to the first within each country
SELECT 
	cl.name,
	cl.country,
	COUNT(*),
	FIRST_VALUE(COUNT(*)) OVER(PARTITION BY cl.country ORDER BY COUNT(*) DESC) as f_value,
	FIRST_VALUE(COUNT(*)) OVER(PARTITION BY cl.country ORDER BY COUNT(*) DESC)-COUNT(*)  as diff
FROM 
	payment as p 
	LEFT JOIN customer_list as cl
		ON p.customer_id = cl.id
GROUP BY name, country




