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