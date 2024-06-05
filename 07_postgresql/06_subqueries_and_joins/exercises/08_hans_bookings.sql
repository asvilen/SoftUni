SELECT
	COUNT(*)
FROM 
	bookings AS b
INNER JOIN 
	customers AS c
	USING(customer_id)
WHERE last_name = 'Hahn';
