/*
LECTURE 229: User Defined Functions

-- Create a function that counts the number of films that are in a range of 
   rental rates. Takes two parameters and returns count
*/

	-- creating function called count_rr
	CREATE FUNCTION count_rr (min_r decimal(4,2), max_r decimal(4,2))-- two parameters
		RETURNS INT
		LANGUAGE plpgsql
		AS
		$$ --starts the body of function
			DECLARE
				movie_count INT;
			BEGIN
				SELECT COUNT(*)
				INTO movie_count -- Into always comes before the FROM command
				FROM film
				WHERE rental_rate BETWEEN min_r AND max_r;
				RETURN movie_count;
			END;
		$$

	-- Calling the function in a query
	-- 336
	SELECT count_rr(3, 6) 
	
	
	
/*
LECTURE 232: TRANSACTIONS
*/
	-- Creating example table
	CREATE TABLE acc_balance (
		id SERIAL PRIMARY KEY,
		first_name TEXT NOT NULL,
		last_name TEXT NOT NULL,
		amount DEC(9,2) NOT NULL
	);

	INSERT INTO acc_balance
	VALUES 
	(1,'Tim','Brown',2500),
	(2,'Sandra','Miller',1600);

	SELECT * FROM acc_balance;
	
	
	-- starting a transaction
	BEGIN;
		UPDATE acc_balance
		SET amount = amount - 100
		WHERE id=1;
		
		UPDATE acc_balance
		SET amount = amount + 100
		WHERE id=2;
		
		COMMIT;--This makes the changes appear in other sessions
	
	
	
/*
LECTURE 235: ROLLBACKS
*/

SELECT *
FROM acc_balance

BEGIN; -- starts transaction
	UPDATE acc_balance
	SET amount=amount-100
	WHERE id=2;
	SAVEPOINT s1; --everything up to this point is correct
	
	--The following is a mistake
	DELETE FROM acc_balance
	WHERE id=2
	
	ROLLBACK TO SAVEPOINT s1; --undoes the DELETE FROM command

	ROLLBACK -- undoes everything


/*
LECTURE 236: STORED PROCEDURES
*/
CREATE PROCEDURE sp_transfer (tr_amount INT, sender INT, recipient INT)
	LANGUAGE plpgsql
	AS
	$$
	BEGIN
		--subtrack from sender's balance
		UPDATE acc_balance
		SET amount = amount - tr_amount
		WHERE id = sender;
		
		-- add to recipient's balance
		UPDATE acc_balance
		SET amount = amount + tr_amount
		WHERE id = recipient;
		
		COMMIT;
	END;
	$$

--calling the stored procedure
CALL sp_transfer(100, 1, 2);
SELECT * FROM acc_balance;

-- reverting back to original
CALL sp_transfer(-100, 1, 2);
SELECT * FROM acc_balance;



