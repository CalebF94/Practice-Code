/*
SECTION 12: GROUPING SETS, ROLLUPS, SELFJOINS LECTURE NOTES
*/

/*
LECTURE 208: GROUPING SETS
*/
SELECT 
	TO_CHAR(payment_date, 'Month') as month,
	staff_id,
	SUM(amount)
FROM payment
GROUP BY
	GROUPING SETS(
		(staff_id),
		(month),
		(staff_id, month)
	)
ORDER BY month, staff_id;

/*
LECTURE 212: ROLLUP and CUBE
*/
-- Using ROLLUP to create a hierarchy of quater month and day

SELECT
	'Q'||TO_CHAR(payment_date, 'Q') as qtr,
	EXTRACT(month from payment_date) as month,
	Date(payment_date) as date,
	SUM(amount)
FROM payment
GROUP BY
	ROLLUP(qtr, month, date)
ORDER BY qtr, month, date;

/*
LECTURE 216: CUBE
*/
SELECT 
	customer_id,
	staff_id,
	DATE(payment_date) as date,
	SUM(amount)
FROM payment
GROUP BY
	CUBE(customer_id, staff_id, date)
ORDER BY customer_id, staff_id, date;






