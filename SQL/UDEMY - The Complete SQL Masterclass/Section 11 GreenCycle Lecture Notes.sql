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





