/*
SECTION 9: GREENCYCLE Challenges
*/

/*Create a table with 5 columns
	- transaction id
	- customer_id
	- film_id
	- amount
	- promotion_code
	
	ransaction_id shoul be the primary key.
The columns customer_id and film_id should be foreign keys to the relevant tables.
The amount column can contain values from 0.00 to 999.99 - nulls should not be allowed.
The column promotion_code contains a promotion code of at maximum 10 characters. 
If there is no value you should set the default value 'None'.
*/

CREATE TABLE online_sales (
transaction_id SERIAL PRIMARY KEY,
customer_id INT REFERENCES customer(customer_id),
film_id INT REFERENCES film(film_id),
amount NUMERIC(5, 2) NOT NULL CHECK (amount BETWEEN 0.00 AND 999.99),
promotion_code VARCHAR(10) DEFAULT('None')
)


/*
INSERT Assignment

Insert these values in the table online_sales:
	- transaction_id (1,2,3)
	- customer_id (124, 225, 119)
	- film_id (65, 231, 53)
	- amount (14.99, 12.99, 15.99)
	- promotion_code (PROMO2022, JULYPROMO, SUMMERDEAL)
*/
INSERT INTO online_sales
	(transaction_id, customer_id, film_id, amount, promotion_code)
	VALUES (1, 124, 65, 14.99, 'PROMO2022'),
		   (2, 225, 231, 12.99, 'JULYPROMO'),
		   (3, 119, 53, 15.99, 'SUMMERDEAL');


/*
CHALLENGE: ALTER TABLE

Make the following modifications to the director table:
	- director_account_name to VARCHAR(30)
	- drop the default on last_name
	- add the constraint not null to last name
	- add the column email of data type VARCHAR(40)
	- rename the director_account_name to account_name
	- rename the table from director to directors
*/
ALTER TABLE director
	ALTER COLUMN director_account_name TYPE VARCHAR(30),-- type only needed for alter
	ALTER COLUMN last_name DROP DEFAULT,
	ALTER COLUMN last_name SET NOT NULL,
	ADD COLUMN email VARCHAR(40);
	
ALTER TABLE director
	RENAME director_account_name TO account_name;
	
ALTER TABLE director
	RENAME TO directors;

SELECT * FROM directors




