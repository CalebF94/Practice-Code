/*
CHALLENGE: GROUP BY
*/
--Which employee is responsible for a higher overlal payment amount?
SELECT 
	staff_id,
	SUM(amount),
	count(*)
FROM payment
GROUP BY staff_id
ORDER BY sum(amount);

-- How do these amounts change if we don't consider amounts equal to 0?
SELECT 
	staff_id,
	SUM(amount),
	count(*)
FROM payment
WHERE amount != 0
GROUP BY staff_id
ORDER BY sum(amount);



/*
CHALLENGE: GROUP BY multiple columns
*/

--Which employee had the highest sales amount in a single day?
SELECT
	staff_id,
	DATE(payment_date) as dt,
	SUM(amount),
	COUNT(*)
FROM 
	payment
GROUP BY staff_id, dt
ORDER BY sum(amount) DESC;

-- What if we don't consider payments where amount is 0?
SELECT
	staff_id,
	DATE(payment_date) as dt,
	SUM(amount),
	COUNT(*)
FROM 
	payment
WHERE amount != 0
GROUP BY staff_id, dt
ORDER BY sum(amount) DESC;

/*
CHALLENGE: HAVING
*/
-- What is the average payment amount grouped by customer and day. Consider 
-- only the days/customers with more than 1 payment. ORder by the average
-- amount in a descending order.
SELECT 
	customer_id,
	DATE(payment_date) as dt,
	ROUND(AVG(amount), 2) as average,
	COUNT(*)
FROM 
	payment
WHERE DATE(payment_date) IN ('2020-04-28', '2020-04-29', '2020-04-30')
GROUP BY customer_id, dt
HAVING COUNT(*) > 1
ORDER BY average DESC;






