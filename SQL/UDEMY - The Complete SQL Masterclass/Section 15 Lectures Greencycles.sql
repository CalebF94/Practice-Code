/*
LECTURE 241: CREATE USER
*/

CREATE USER sarah
WITH password 'sarah1234';

CREATE ROLE alex
WITH LOGIN PASSWORD 'alex1234';

/*
LECTURE 243: HANDS ON
*/

--CREATE USERS
CREATE USER ria
WITH PASSWORD 'riah123';

CREATE USER mike
WITH PASSWORD 'mike123';

-- CREATE ROLES
CREATE ROLE read_only;
CREATE ROLE read_update;


-- GRANT USAGE (already granted)
GRANT USAGE
ON SCHEMA public
TO read_only;


-- GRANT SELECT on tables
GRANT SELECT
ON ALL TABLES IN SCHEMA public
TO READ_ONLY;

-- Granting role to user
GRANT read_only to mike;


-- Giving read_only privileges to the read_update role
GRANT read_only
TO read_update;

-- GRANTING all privileges on all tables in public to read_update role
GRANT ALL
ON ALL TABLES IN SCHEMA public
TO read_update;

--Revoking some privileges
REVOKE DELETE, INSERT
ON ALL TABLES IN SCHEMA public
FROM read_update;

-- Assign role to users
GRANT read_update
TO ria;




