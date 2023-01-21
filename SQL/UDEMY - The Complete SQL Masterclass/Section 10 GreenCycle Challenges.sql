/*
SECTION 10: Views and Data Manipulation

Challenges: Greencycles database
*/

/*
CHALLENGES: UPDATE
*/
	-- Update all rental prices that are 0.99 to 1.99
	UPDATE film
		SET rental_rate = 1.99
		WHERE rental_rate = 0.99;
		
	-- Alter the customer table
		--1) add the column initials VARCHAR(10)
		--2) Update the values in initials be F.L.
	ALTER TABLE customer
		ADD initials VARCHAR(10);
		
	UPDATE customer
		SET initials = LEFT(first_name, 1)||'.'||LEFT(last_name, 1)||'.';
		
		
	SELECT * FROM customer;
	
	
/*
CHALLENGE: DELETE
*/
--Delete the rows in the payment table with payment_id 17064 or 17067
SELECT * FROM payment WHERE payment_id IN (17064, 17067);

DELETE FROM payment
	WHERE payment_id IN (17064, 17067)
	RETURNING *


/*
CHALLENGE: DELETE
*/
--Create a table called customer_spendings with the first and last name along
-- with their total spendings
	CREATE TABLE customer_spendings
	AS
		SELECT 
			first_name || ' ' || last_name AS name,
			SUM(amount) AS total_amount
		FROM
			customer as c
			LEFT JOIN payment as p
				ON p.customer_id = c.customer_id
		GROUP BY first_name || ' ' || last_name;

	SELECT * FROM customer_spendings;

/*
CHALLENGE: CREATE VIEW 
*/
-- CREATE VIEW called 'films_category' that shows a list of the film titles that includes:
	-- title, length, and category name ordered by descending length
	-- Filter the results to only the movies in the Action and Comedy genres
CREATE VIEW films_category
AS
	SELECT
		f.title,
		f.length,
		c.name as category
	FROM 
		film as f 
		LEFT JOIN film_category as fc
			ON f.film_id = fc.film_id
		LEFT JOIN category as c
			ON fc.category_id = c.category_id
	WHERE c.name IN ('Action', 'Comedy')
	ORDER BY f.length;
	

/*
CHALLENGE: MANAGING VIEWS
*/
    CREATE VIEW v_customer_info
    AS
		SELECT cu.customer_id,
			cu.first_name || ' ' || cu.last_name AS name,
			a.address,
			a.postal_code,
			a.phone,
			city.city,
			country.country
			 FROM customer cu
			 JOIN address a ON cu.address_id = a.address_id
			 JOIN city ON a.city_id = city.city_id
			 JOIN country ON city.country_id = country.country_id
    	ORDER BY customer_id;
-- Using the above view perform the following tasks
		--1) rename view to v_customer_information
		--2) rename the customer_id column to c_id
		--3) add the initial column as the third column to the view by replacing the view	

--1)
ALTER VIEW v_customer_info 
	RENAME TO v_customer_information;
	
SELECT * FROM v_customer_information;	
	
--2)
ALTER VIEW v_customer_information
	RENAME customer_id TO c_id;
	
SELECT * FROM v_customer_information;

--3)
CREATE OR REPLACE VIEW v_customer_information
AS
	SELECT 	cu.customer_id,
			cu.first_name || ' ' || cu.last_name AS initials,
			LEFT(cu.first_name, 1) || ' ' || LEFT(cu.last_name,1) AS name,
			a.address,
			a.postal_code,
			a.phone,
			city.city,
			country.country
			 FROM customer cu
			 JOIN address a ON cu.address_id = a.address_id
			 JOIN city ON a.city_id = city.city_id
			 JOIN country ON city.country_id = country.country_id
	ORDER BY customer_id;

	