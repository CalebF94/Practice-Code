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
	
	
	
/*
CHALLENGE: LEFT JOIN

-- FIND aircrafts that have not been used in any flights
-- Finding aircraft where the flight id is null
*/
SELECT * 
FROM aircrafts_data as a LEFT JOIN flights as f	
	ON a.aircraft_code = f.aircraft_code
WHERE a.aircraft_code is not null AND flight_id is null;
	
-- Which seat is the most commonly chosen spot?
-- Make sure all seats are included even if they have never been chosen
SELECT 
	s.seat_no as seat,
	COUNT(*) as times_chosen
FROM seats AS s LEFT JOIN boarding_passes AS bp
	ON s.seat_no = bp.seat_no
GROUP BY seat
ORDER BY times_chosen DESC;


-- Which line(A, B,...H) has been chosen most
SELECT 
	RIGHT(s.seat_no, 1) as row,
	COUNT(*) as times_chosen
FROM seats AS s LEFT JOIN boarding_passes AS bs
	ON s.seat_no = bs.seat_no
GROUP BY row
ORDER BY times_chosen DESC;
	

/*
CHALLENGE: JOINS ON MULTIPLE CONDITIONS

-- Find the average price for different seat numbers
*/

SELECT 
	bp.seat_no as seat_no,
	ROUND(AVG(tf.amount), 2) as avg_amount
FROM ticket_flights AS tf LEFT JOIN boarding_passes AS bp 
	ON tf.ticket_no = bp.ticket_no 
	AND tf.flight_id = bp.flight_id
GROUP BY seat_no
ORDER BY avg_amount DESC;
	
	
	
	
	