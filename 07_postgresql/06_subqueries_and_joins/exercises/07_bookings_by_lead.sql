SELECT
	apartment_id,
	booked_for,
	first_name,
	country
FROM 
	bookings AS b
INNER JOIN 
	customers AS c
	USING(customer_id)
WHERE job_type = 'Lead';
