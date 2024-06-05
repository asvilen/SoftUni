SELECT
	name,
	SUM(booked_for)
FROM 
	apartments AS a
JOIN 
	bookings AS b
USING
	(apartment_id)
GROUP BY
	name
ORDER BY
	name;
