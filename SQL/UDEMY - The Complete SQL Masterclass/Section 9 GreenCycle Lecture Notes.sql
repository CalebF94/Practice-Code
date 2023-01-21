/*
SECTION 9: Managing tables and Databases
Lecture Notes
*/

CREATE TABLE director (
director_id SERIAL PRIMARY KEY, --Serial just means increaments by 1
director_account_name VARCHAR(20) UNIQUE,
first_name VARCHAR(50),
last_name VARCHAR(50) DEFAULT 'Not Specified',
date_of_birth DATE,
address_id INT REFERENCES address(address_id) --This creates a foreign key
)


/*
LECTURE NOTES: DROP and TRUNCATE Table
*/
	CREATE TABLE emp_table
	(--these are the fields in the table
		emp_id SERIAL PRIMARY KEY,
		emp_name TEXT
	);

	-- querying the table
	SELECT * FROM emp_table;

	-- Dropping table	
	DROP TABLE emp_table;

	-- querying the table, but you'll get an error
	SELECT * FROM emp_table;
	
	
	-- Recreating table
	CREATE TABLE emp_table
	(--these are the fields in the table
		emp_id SERIAL PRIMARY KEY,
		emp_name TEXT
	);
	
	-- Inserting data
	INSERT INTO emp_table
		VALUES (1, 'Frank'),
			   (2, 'Maria'),
			   (3, 'Caleb');

	-- Query the emp_table
	SELECT * FROM emp_table;
	
	-- Truncating rows from table
	TRUNCATE emp_table; --TRUNCATE TABLE emp_table
	
	-- Query the emp_table, table is empty
	SELECT * FROM emp_table;
	
	
	
	