/* 
CHALLENGE: TRANSACTIONS
	-- The two employees Miller McQarter and Christalle Mckenny have agreed to 
	   swap their positions including their salaries
*/

SELECT 
	emp_id, first_name, last_name, position_title, salary
FROM 
	employees
WHERE 
	emp_id IN(2, 3);


BEGIN;
	UPDATE employees
	SET position_title = 'Head of Sales'
	WHERE emp_id = 2;
	
	UPDATE employees
	SET position_title = 'Head of BI'
	WHERE emp_id = 3;
	
	UPDATE employees
	SET salary = 12587.00
	WHERE emp_id = 2;
	
	UPDATE employees
	SET salary = 14614.00
	WHERE emp_id = 2;
	COMMIT;
	
	
/*
CHALLENGE: STORED PROCEDURES

-- Create a stored procedure called emp_swap that accepts two parameters emp1 and
   emp2 as input and swaps the two employees position and salary
   
-- Test the stored procedure with emp_id 2 and 3
*/
CREATE OR REPLACE PROCEDURE emp_swap (emp1 INT, emp2 INT)
	LANGUAGE plpgsql
	AS
	$$
	DECLARE
		salary1 DECIMAL(8,2);
		salary2 DECIMAL(8,2);
		position1 TEXT;
		position2 TEXT;
	BEGIN
		-- Assigning values to variables
		SELECT salary INTO salary1 FROM employees WHERE emp_id = emp1;
		SELECT salary INTO salary2 FROM employees WHERE emp_id = emp2;
		SELECT position_title INTO position1 FROM employees WHERE emp_id = emp1;
		SELECT position_title INTO position2 FROM employees WHERE emp_id = emp2;
	
		--Swapping salaries
		UPDATE employees
		SET salary = salary2
		WHERE emp_id = emp1;
		
		UPDATE employees
		SET salary = salary1
		WHERE emp_id = emp2;

		--Swapping titles
		UPDATE employees
		SET position_title = position2
		WHERE emp_id = emp1;
		
		UPDATE employees
		SET position_title = position1
		WHERE emp_id = emp2;
	COMMIT;
	END;
	$$


SELECT emp_id, salary, position_title, first_name, last_name
FROM employees
WHERE emp_id IN(1,2);

CALL emp_swap(1,2);

-- reverting back to original
CALL emp_swap(1,2);