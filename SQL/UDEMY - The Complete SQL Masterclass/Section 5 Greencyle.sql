/*
SECTION 5: Challenges: Conditional Expressions
THese challenges use the greencycles database
*/

-- create a list of files including the relation of rental rate/replacement 
-- cost where the rental rate is less than 4% of the replacement cost
SELECT 
	title,
	film_id,
	ROUND(ROUND(rental_rate/replacement_cost,4)*100, 2) as ratio
FROM film
WHERE ROUND(rental_rate/replacement_cost,4)<0.04
ORDER BY ratio;

-- Create a list of film_ids together with the percentage rounded to 2 
-- decimal places
SELECT
	film_id,
	ROUND(ROUND(rental_rate/replacement_cost,4)*100,2) || '%' as ratio
FROM film;

/*
CHALLENGE: CASE STATEMENT
*/
-- Create a tier list:
-- Rating is PG PG-13 or length is more than 210 min ('Tier 1')
-- Description contains drama and length is more than 90min('Tier 2')
-- description contains drama and length is not more than 90 min (Tier 3)
-- rental_rate less than $1 (Tier 4)
-- Filter movies that are not in one of the tiers
SELECT 
	CASE 
		WHEN rating IN ('PG', 'PG-13') OR length>210 THEN 'Tier 1'
		WHEN description LIKE '%Drama%' AND length>90 THEN 'Tier 2'
		WHEN description LIKE '%Drama%' AND length<=90 THEN 'Tier 3'
		WHEN rental_rate < 1 THEN 'Tier 4'
		ELSE null
	END as Tier,
	COUNT(*)
FROM film
WHERE 
	CASE 
		WHEN rating IN ('PG', 'PG-13') OR length>210 THEN 'Tier 1'
		WHEN description LIKE '%Drama%' AND length>90 THEN 'Tier 2'
		WHEN description LIKE '%Drama%' AND length<=90 THEN 'Tier 3'
		WHEN rental_rate < 1 THEN 'Tier 4'
		ELSE null
	END is not null
GROUP BY Tier
ORDER BY Tier;



-- create a 1 row by 5 column table that counts the number of movies with a given
-- rating. There are five ratings G, R, NC-17, PG-13, and PG
SELECT 
	SUM(CASE WHEN rating = 'G' THEN 1 END) as "G",
	SUM(CASE WHEN rating = 'PG' THEN 1 END) as "PG",
	SUM(CASE WHEN rating = 'PG-13' THEN 1 END) as "PG-13",
	SUM(CASE WHEN rating = 'NC-17' THEN 1 END) as "NC-17",
	SUM(CASE WHEN rating = 'R' THEN 1 END) as "R"
FROM film;
	
	
/*
CHALLENGE: Coalese and Cast

-- Replace the null values in the return_date column to read 'Not Returned'
-- Use the rental table
*/

SELECT 
	rental_date,
	COALESCE(CAST(return_date AS VARCHAR), 'Not Returned')
FROM
	rental
ORDER BY rental_date DESC;
	
	
