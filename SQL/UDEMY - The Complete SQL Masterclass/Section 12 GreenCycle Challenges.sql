/*
CHALLENGE: GROUPING SETS

--Write a query that returns the sum of the amount for each customer(first and last name) and
 each staff_id. Also add the overall revenue per customer
*/

SELECT
	first_name,
	last_name,
	staff_id,
	SUM(amount)
FROM
	payment as p
	LEFT JOIN customer as c
		ON p.customer_id = c.customer_id
GROUP BY
	GROUPING SETS(
		(first_name, last_name),
		(staff_id),
		(first_name, last_name, staff_id))
ORDER BY first_name, last_name, staff_id;


/*
CHALLENGE: GROUPING SETS ADDITIONAL CHALLENGE

-- Write a query that calculates the share of revenue each staff_id makes per customer
*/
SELECT
	first_name,
	last_name,
	staff_id,
	SUM(amount) as total,
	ROUND(100*SUM(amount) / FIRST_VALUE(SUM(amount)) OVER(PARTITION BY first_name, last_name 
														  ORDER BY  SUM(amount) DESC), 2)
FROM
	payment as p
	LEFT JOIN customer as c
		ON p.customer_id = c.customer_id
GROUP BY
	GROUPING SETS(
		(first_name, last_name),
		(first_name, last_name, staff_id))
ORDER BY first_name, last_name, staff_id;


/*
CHALLENGE: CUBE

-- Write a query that returns all grouping sets in all combinations of customer_id,
   date and title with the aggregation of the payment amount
*/
SELECT 
	p.customer_id,
	DATE(payment_date) as date,
	f.title,
	SUM(amount) as total
FROM 
	payment as p
	LEFT JOIN rental as r
		ON p.rental_id = r.rental_id
	LEFT JOIN inventory as i 
		ON r.inventory_id = i.inventory_id
	LEFT JOIN film as f
		ON f.film_id = i.film_id
GROUP BY
	CUBE(1,2,3)
ORDER BY 1,2,3;





