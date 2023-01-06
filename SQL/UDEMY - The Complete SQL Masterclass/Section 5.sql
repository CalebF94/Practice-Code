/*
SECTION 5: Challenges: Conditional Expressions
*/
-- create a list of files including the relation of rental rate/replacement 
-- cost where the rental rate is less than 4% of the replacement cost
SELECT 
	title,
	film_id,
	ROUND(ROUND(rental_rate/replacement_cost,4)*100, 2) as ratio
FROM film
WHERE ROUND(rental_rate/replacement_cost,4)<0.04
ORDER BY ratio

-- Create a list of film_ids together with the percentage rounded to 2 
-- decimal places
SELECT
	film_id,
	ROUND(ROUND(rental_rate/replacement_cost,4)*100,2) || '%' as ratio
FROM film;
	
	
	
	
	
	
	