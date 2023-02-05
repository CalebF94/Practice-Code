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