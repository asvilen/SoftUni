SELECT
	booked_for,
	(booked_for * 50)::numeric AS multiplication,
	(booked_for % 50)::numeric AS modulo
INTO 
	bookings_calculation
FROM 
	bookings
WHERE 
	apartment_id = 93;
