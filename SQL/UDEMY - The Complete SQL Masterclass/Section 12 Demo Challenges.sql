/*
SECTION 12 CHALLENGES DEMO Database*/

/*
CHALLENGE: ROLLUP

-- write a query that calculates a booking amount rollup for the hierarchy of qtr, mon, week
   in month and day
*/
SELECT 
	TO_CHAR(book_date, 'Q') as qtr,
	TO_CHAR(book_date, 'MM') as month,
	TO_CHAR(book_date, 'W') as week,
	DATE(book_date) as date,
	SUM(total_amount)
FROM
	bookings
GROUP BY
	ROLLUP(qtr, month, week, date)
ORDER BY qtr, month, week, date;