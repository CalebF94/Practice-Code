/*
SECTION 10: Views and Data Manipulation

Lecture Notes: GREENCYCLES database
*/

/*
LECTURE: UPDATE
*/
-- Change the last name of the first customer
	--first customer has last name of Smith
	SELECT * FROM customer WHERE customer_id = 1;

	--Changing last name to Brown
	UPDATE customer
	SET last_name = 'Brown'
	WHERE customer_id = 1;
	
	SELECT * FROM customer WHERE customer_id = 1;

-- Convert all emails to lower case
	SELECT email FROM customer;
	
	UPDATE customer 
		SET email = LOWER(email);
		
	SELECT email FROM customer;
	




/*
LECTURE: DELETE
*/
-- inserting some data
	INSERT INTO songs
		(song_name, genre, price, release_date)
		VALUES
			('Have a talk with Data', 'Chill out', 5.99, '01-06-1999'),
			('Tame the Data', 'Classical', 4.99, '01-06-2022');

-- Modifying some current data
	UPDATE songs
		SET genre='Country Music'
		WHERE genre='Not defined';


	SELECT * FROM songs;

-- Delete the songs with genre = Country music
	DELETE FROM songs
		WHERE genre='Country Music'
		RETURNING song_name, song_id

	SELECT * FROM songs;


/*
LECTURE: CREATE TABLE
*/
CREATE TABLE customer_address --customer_address is the name of the created table
AS
	-- These are the rows/columns that will make up the table
	SELECT 
		first_name, 
		last_name, 
		email, 
		address, 
		city
	FROM 
		customer AS c
		LEFT JOIN address AS a
			ON c.address_id = a.address_id
		LEFT JOIN city as ci
			ON ci.city_id = a.city_id;


/*
LECTURE: CREATE VIEW
*/
DROP TABLE customer_spendings;

-- This is the same as the previous challenge except we're making a view instead of a table
CREATE View customer_spendings
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

SELECT * FROM customer_spendings;



/*
LECTURE: CREATE MATERIALIZED VIEW
*/
-- Delete the previous film_category view
	CREATE VIEW mv_films_category --using prefix mv_ to distinguish object
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


	SELECT * FROM mv_films_category;

	--Update the underlying table
	UPDATE film
	SET length = 192
	WHERE title = 'SATURN NAME';

	REFRESH MATERIALIZED VIEW mv_film_category;
	
	--view updated vie
	SELECT * from mv_films_category WHERE title='SATURN NAME';
	
/*
LECTURE 192: Import and Export
*/
	CREATE TABLE sales (
		transaction_id SERIAL PRIMARY KEY,
		customer_id INT,
		payment_type VARCHAR(20),
		creditcard_no VARCHAR(20),
		cost DECIMAL(5, 2),
		quantity INT,
		price DECIMAL (5, 2));

	-- data was imported using the I/O interface by right clicking
	-- on the table name
	SELECT * FROM sales;





	
	
	