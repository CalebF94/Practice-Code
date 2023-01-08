/*
CHALLENGES: JOINS

These challenges use the demo database.
*/

/*
CHALLENGE: INNER JOIN

-- How many people choose seats in the categories Business, economy, 
   or comfort? Use the seats and boarding_passes tables.
*/
SELECT 
	s.fare_conditions,
	COUNT(*)
FROM seats s INNER JOIN boarding_passes bs
	ON s.seat_no=bs.seat_no
GROUP BY s.fare_conditions;


/*
CHALLENGE: OUTER JOIN

-- Find the tickets that don't have a boarding pass related to it
*/

SELECT COUNT(*)
FROM boarding_passes b FULL OUTER JOIN tickets t
	ON b.ticket_no = t.ticket_no
WHERE b.boarding_no IS null;
	
	
	
	
	