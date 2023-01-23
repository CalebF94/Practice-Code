/*
SECTION 11: WINDOW FUNCTIONS

DEMO CHALLENGES
*/


/*
CHALLENGE: OVER() WITH ORDER BY

-- Return the running total of how late the flights are ordered by flight_id
   including the departure airport
*/
	SELECT
		flight_id,
		departure_airport,
		SUM(actual_arrival-scheduled_arrival) OVER(ORDER BY flight_id)
	FROM
		flights;
	
	
/*
-- calculate the same running total but partition by departure airport
*/

	SELECT
		flight_id,
		departure_airport,
		SUM(actual_arrival-scheduled_arrival) OVER(PARTITION BY departure_airport
												   ORDER BY flight_id)
	FROM
		flights;



