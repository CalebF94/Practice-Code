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
