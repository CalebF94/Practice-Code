/*
SECTION 5: Challenges: Conditional Expressions

These challenges use the demo database
*/

/*
CHALLENGE: CASE STATEMENT
Notes: This challenge is using the demo database
*/
-- Create categories for ticket price and find the number of tickets sold in
-- each of the three categories. 1)amount<20,000 2)amount 20,000-150,000 3)
-- 3) Amount > 150,000

SELECT 
	CASE 
		WHEN amount <20000 THEN 'Low Price'
		WHEN amount BETWEEN 20000 AND 150000 THEN 'Mid Price'
		ELSE 'High Price'
	END as Ticket_Category,
	COUNT(*) as Tickets_Sold
FROM ticket_flights
GROUP BY Ticket_Category;
	
	
-- How many flights have departed in the four seasons
-- Winter=>Dec, jan, feb  Spring=>mar, apr, may  Summer=>Jun, jul, aug
-- Fall=> sep, oct, nov
SELECT 
	CASE
		WHEN EXTRACT(month from scheduled_departure) IN (12,1,2) THEN 'Winter'
		WHEN EXTRACT(month from scheduled_departure) IN (3,4,5) THEN 'Spring'
		WHEN EXTRACT(month from scheduled_departure) IN (6,7,8) THEN 'Summer'
		WHEN EXTRACT(month from scheduled_departure) IN (9,10,11) THEN 'Fall'
		ELSE 'No Departure'
	END as Season,
	COUNT(*) as Flights
FROM Flights
GROUP BY Season;


/*
CHALLENGE: REPLACE FUNCITON

-- Remove PG from the flight_no column in the flights table and convert to int
*/
SELECT
	flight_id,
	CAST(REPLACE(flight_no, 'PG', '') AS INT) as flight_no
FROM
	flights;
