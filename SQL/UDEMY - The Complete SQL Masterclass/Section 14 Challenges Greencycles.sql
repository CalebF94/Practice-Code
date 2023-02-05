/*
CHALLENGE: User Defined Function

-- Create a function that expects the customer's first and last name and returns
   the total amount of payments this customer has made
*/

CREATE OR REPLACE FUNCTION name_search (f_name VARCHAR(10), l_name VARCHAR(20))
RETURNS DECIMAL(6,2)
LANGUAGE plpgsql
	AS
	$$
		DECLARE
			total_payments decimal(6,2);
		BEGIN
			SELECT SUM(amount)
			INTO total_payments
			FROM 
				payment as p
				LEFT JOIN customer as c
					ON p.customer_id = c.customer_id
			WHERE 
				UPPER(first_name) = UPPER(f_name) AND
				UPPER(last_name) = UPPER(l_name);
			RETURN
				total_payments;
		END;
	$$;
	
SELECT name_search('Amy', 'lopez')



