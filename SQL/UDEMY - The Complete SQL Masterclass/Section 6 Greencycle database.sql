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





