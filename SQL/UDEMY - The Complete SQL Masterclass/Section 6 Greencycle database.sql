/*
CHALLENGES: JOINS

These challenges use the demo database.
*/


/*
CHALLENGE: JOINS

-- Company wants to run a phone campaign on all customers in Texas (district)
*/	
-- What are the customers from Texas? (first and last name, phone, and district)
SELECT  
	c.first_name,
	c.last_name,
	a.phone,
	a.district
FROM customer AS c LEFT JOIN address AS a 
	ON c.address_id = a.address_id
WHERE a.district = 'Texas';


-- Are there any old addresses that are not related to any customer?
SELECT *
FROM address AS a LEFT JOIN customer AS c
	ON a.address_id = c.address_id
WHERE c.customer_id is NULL;


/*
CHALLENGE: JOINING MULTIPLE TABLES

-- Write a query to get first_name, last_name, email and country from all 
   customers from Brazil
   
customer (address_id) => address (address_id)

 ==> city (city id)
 ==> country (country id)
*/	
SELECT
	first_name,
	last_name, 
	email,
	country
FROM customer as c
	LEFT JOIN address as a 
		ON c.address_id = a.address_id
	LEFT JOIN city
		ON a.city_id = city.city_id
	INNER JOIN country --inner b/c we only want rows that have matches
		ON city.country_id = country.country_id
WHERE country='Brazil'


/*
CHALLENGE: More Challenges Section Question 3

-- Which title has GEORGE LINTON rented most often
*/
SELECT 	
	f.title as movie,
	COUNT(*) as times_rented
FROM rental as r
	INNER JOIN customer as c
		ON r.customer_id = c.customer_id
		AND first_name = 'GEORGE' AND last_name='LINTON'
	INNER JOIN inventory as i
		ON r.inventory_id = i.inventory_id
	INNER JOIN film as f
		ON i.film_id = f.film_id
GROUP BY f.title
ORDER BY times_rented DESC;


-- Given solution
    SELECT first_name, last_name, title, COUNT(*)
    FROM customer cu
    INNER JOIN rental re
    ON cu.customer_id = re.customer_id
    INNER JOIN inventory inv
    ON inv.inventory_id=re.inventory_id
    INNER JOIN film fi
    ON fi.film_id = inv.film_id
    WHERE first_name='GEORGE' and last_name='LINTON'
    GROUP BY title, first_name, last_name
    ORDER BY 4 DESC;
