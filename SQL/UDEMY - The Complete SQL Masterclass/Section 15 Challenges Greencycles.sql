/*
SECTION 15: CHALLENGES GREENCYLES Database
*/

/*
CHALLENGE: PRIVILEGES

1) create user mia with password 'mia123'
2) create analyst_emp role
3) grant select on all tables in the public schema to that role
4) grant insert and update on the employees table to that role
5) add permission to create databases to that role
6) assign that role to mia and test the priveleges with that user
*/

-- 1)
CREATE USER mia
PASSWORD 'mia123';

--2)
CREATE ROLE analyst_emp;

--3)
GRANT SELECT ON ALL TABLES IN SCHEMA public
TO analyst_emp;

--4)
GRANT INSERT, UPDATE ON employees 
TO analyst_emp;

--5)
ALTER ROLE analyst_emp CREATEDB;

--6)
GRANT analyst_emp
TO mia;