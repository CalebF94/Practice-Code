/*Udemy: The Complete SQL Masterclass

Mid-Course Project: 
	- This is a series of 14 questions
	- Goal is to complete 12 questions correctly
*/

/*
Question 1:
Topic: Distint
Task: Create a list of all the different replacement costs
	  and find the lowest value
	  
Result: Correct (9.99)
*/
SELECT DISTINCT replacement_cost
FROM film
ORDER BY replacement_cost;


/*
Question 2
Topic: CASE and GROUP BY
Task: Write a query giving an overview of films with the following replacement costs
		1) LOW 9.99-19.99
		2) MEDIUM 20.00-24.99
		3) HIGH 25.00-29.99
	  How many movies are in the LOW category
	  
Result: Correct (514)
*/
SELECT 
	(CASE 
		WHEN replacement_cost <= 19.99 THEN 'LOW'
		WHEN replacement_cost BETWEEN 20.00 AND 24.99 THEN 'MEDIUM'
		WHEN replacement_cost >= 25 THEN 'HIGH'
		ELSE 'Replacement Cost Unknown'
	 END) as Category,
	 COUNT(*)
FROM film
GROUP BY Category;


/*
Question 3
Topic: JOIN
Task: 
	- Create a list of film titles including title, length, and Category
	- Order descending by length
	- Filter results to only movies in categories drama or sports
	- Which category has the longest film and what is the length?

Notes: Need to perform two joins to bring in category name (in the category table)
	- The film table maps to film category table
	- The film category table maps to the category table

Result: Correct (Sports, 184 minutes, SMOOCHY CONTROL)
*/
SELECT 
	f.title, 
	c.name, 
	f.length
FROM 
	film as f 
	LEFT JOIN film_category as fc
		ON f.film_id = fc.film_id
	LEFT JOIN category as c
		ON fc.category_id = c.category_id
WHERE UPPER(c.name) IN('SPORTS', 'DRAMA')
ORDER BY f.length DESC;



/*
Question 4
Topic: JOIN and GROUP BY
Task: 
	- Create an overview of how many movies there are in each category
	- Which category is the most common among the films

Notes: 
	Need to perform two joins to bring in category name (in the category table)
	- The film table maps to film category table
	- The film category table maps to the category table

Result: Correct (SPORTS 74 titles)
*/
SELECT 
	c.name,
	COUNT(*)
FROM 
	film as f 
	LEFT JOIN film_category as fc
		ON f.film_id = fc.film_id
	LEFT JOIN category as c
		ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY COUNT(*) DESC;


/*
Question 5
Topic: JOIN and GROUP BY
Task: 
	- Create an overview of the actors first and last names and in how many movies they appear
	- Which actor is in the most movies?

Notes: 
	- Need to perform one joins to bring in all information
	- film_actor contains all actors that appeared in all movies
	- film_actor maps to actor which contains the first and last names

Result: Correct (Susan Davis, 54 movies)
*/
SELECT 
	a.first_name,
	a.last_name,
	COUNT(*) as movies
FROM 
	film_actor as fa
	LEFT JOIN actor as a
		ON fa.actor_id = a.actor_id
GROUP BY a.first_name, a.last_name
ORDER BY movies DESC;

/*
Question 6
Topic: LEFT JOIN and Filtering
Task: 
	- Create an overview of the addresses that are not associated to any customer
	- How many addresses are there?

Notes: 
	- The address table contains the list of all addresses
	- Address table maps to customer
	- return the rows that have a null customer_id

Result: Correct (4)
*/
SELECT
	a.address,
	c.customer_id
FROM 
	address as a 
	LEFT JOIN customer as c
		ON a.address_id = c.address_id
WHERE c.customer_id is null;


/*
Question 7
Topic: JOIN and GROUP BY
Task: 
	- Create an overview of the cities and how much sales have occured in each
	- Which city has the most sales?

Notes: 
	- City is referring to the city of the customer not the city of the store
	- starting with the payment table
	- payment table maps to the customer table
	- customer table maps to the address table
	- address table maps to the city table which contains the city name

Result: Correct (Cape Coral 221.55)
*/
SELECT
	SUM(p.amount),
	cy.city
FROM 
	payment as p 
	LEFT JOIN customer as c
		ON p.customer_id = c.customer_id
	LEFT JOIN address as a
		ON c.address_id = a.address_id
	LEFT JOIN city as cy
		ON a.city_id = cy.city_id
GROUP BY 
	cy.city
ORDER BY SUM(p.amount) DESC;
	
/*
Question 8
Topic: JOIN and GROUP BY
Task: 
	- Create an overview of the revenue grouped by a column in the format "country, city"
	- Which country, city has the least sales?

Notes: 
	- Start with the payment table and use four joins to bring in all needed information
	- payment maps to customer thru customer_id
	- customer maps to address thru address_id
	- address maps to city thru city_id. City contains the city name
	- city maps to country thru country_id. Country contains the Country name
	- use the || operator to concatenate

Result: correct (United States, Tallahassee 50.85)
*/
SELECT 
	SUM(p.amount) as revenue,
	co.country || ', ' || ci.city as location
FROM 
	payment as p 
	LEFT JOIN customer as cu
		ON p.customer_id = cu.customer_id
	LEFT JOIN address as a
		ON cu.address_id = a.address_id
	LEFT JOIN city as ci
		ON a.city_id = ci.city_id
	LEFT JOIN country as co
		ON ci.country_id = co.country_id
GROUP BY location
ORDER BY revenue;

/*
Question 9
Topic: Uncorrelated subquery
Task: 
	- Create a list with the average of the sales amount each staff_id has per customer
	- Which staff_id makes the most revenue per customer

Notes: 
	- The subquery goes in the FROM Clause

Result: Partially Correct. I had to watch the beginning of the solution for a hint (staff_id = 2, 56.64)
*/
-- This gives the correct answer without a subquery
SELECT 
	staff_id,
	ROUND(SUM(amount)/COUNT(DISTINCT customer_id), 2) as avg_revenue	
FROM payment
GROUP BY staff_id;
	

SELECT
	staff_id,
	ROUND(AVG(amount),2) as avg_per_cust
FROM
	(SELECT
		staff_id,
		customer_id,
		SUM(amount) as amount
	FROM payment
	GROUP BY staff_id, customer_id) as agg
GROUP BY staff_id
ORDER BY avg_per_cust DESC;

/*
Question 10
Topic: EXTRACT and Uncorrelated subquery
Task: 
	- Create a query that shows average daily revenue of all Sundays
	- What is the daily average revenue of all Sundays?

Notes: 
	- Field for EXTRACT is isodow 1=Monday 7=Sunday

Result: Correct (my timezone is different so total doesn't match tutorial)
*/
SELECT 
	DOW,
	AVG(daily_total)
FROM
	(SELECT 
		DATE(payment_date) as date,
		EXTRACT(dow from payment_date) as DOW,
		SUM(amount) as daily_total
	FROM payment
	GROUP BY date, DOW) as daily_amounts
GROUP BY DOW
ORDER BY DOW;


/*
Question 11
Topic: Correlated Subquery
Task: 
	- Create a list of movies with length and replacement cost that are longer than
	  the average length in each replacement cost group
	- Which two movies are the shortest in that list and how long are they?

Notes: 
	- The question is poorly worded. It should say which movies are longer than the average of all
	  movies with the same replacement cost. Do not use the groups that were used in previous questions

Result: CORRECT (Celebrity Horn and Seattle Expectations 110 minutes)
*/
SELECT 
	title,
	length,
	replacement_cost
FROM film as f1
WHERE 
	f1.length > (SELECT AVG(length)
				 FROM film as f2
				 WHERE f1.replacement_cost = f2.replacement_cost
			)
ORDER BY length;


/*
Question 12
Topic: Uncorrelated Subquery
Task: 
	- Create a list that shows how much the average customer spent in total grouped by the different districts
	- Which district has the highest average customer life-time value

Notes: 
	- The subquery returns a table that has customer totals along with customer_id and district
	
Result: CORRECT (Saint Denis 216.54)
*/

SELECT 
	district,
	AVG(amount) as dist_avg,
	COUNT(*)
FROM
	(SELECT
		SUM(p.amount) as amount,
		c.customer_id,
		a.district
	FROM 
		payment as p 
		LEFT JOIN customer as c
			ON p.customer_id = c.customer_id
		LEFT JOIN address as a
			ON a.address_id = c.address_id
	GROUP BY c.customer_id, a.district) as cust_tot
GROUP BY district
ORDER BY dist_avg DESC;


/*
Question 13
Topic: Uncorrelated Subquery
Task: 
	- Create a list showing all payments, payment_ids, and film category plus the total amount that was made in this category.
		- Order results ascendingly by the category (name) and payment_id
	- What is the total revenue of the category 'Action' and what is the lowest payment_id in the action category

Notes: 
	- The key is to use a subquery that creates a table that sums amounts by category and then inner join that table to the 
	  payment table that also has the other required information joined to it.
	
Result: 
*/
SELECT 
	p1.payment_id,
	p1.amount,
	f1.title,
	c1.name,
	cat_total.category_total
FROM
	payment as p1
	LEFT JOIN rental as r1
		ON p1.rental_id = r1.rental_id
	LEFT JOIN inventory as i1
		ON r1.inventory_id = i1.inventory_id
	LEFT JOIN film as f1
		ON i1.film_id = f1.film_id
	LEFT JOIN film_category as fc1
		ON f1.film_id = fc1.film_id
	LEFT JOIN category as c1
	 	ON fc1.category_id = c1.category_id
INNER JOIN (SELECT 
				c2.name,
	 			SUM(amount) as category_total
	 		FROM 
	 			payment as p2  
				LEFT JOIN rental as r2
					ON p2.rental_id = r2.rental_id
				LEFT JOIN inventory as i2
					ON r2.inventory_id = i2.inventory_id
				LEFT JOIN film as f2
					ON i2.film_id = f2.film_id
				LEFT JOIN film_category as fc2
					ON f2.film_id = fc2.film_id
				LEFT JOIN category as c2
					ON fc2.category_id = c2.category_id
		GROUP BY c2.name) as cat_total-- end subquery
	ON c1.name = cat_total.name
ORDER BY
	c1.name, p1.payment_id