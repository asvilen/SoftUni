SELECT 
	EXTRACT('Year' FROM booked_at) AS YEAR, 
	EXTRACT('Month' FROM booked_at) AS MONTH,
	EXTRACT('Day' FROM booked_at) AS DAY,
	EXTRACT('Hour' FROM booked_at AT TIME ZONE 'UTC') AS HOUR,
	EXTRACT('Minute' FROM booked_at) AS MINUTE,
	CEILING(EXTRACT('Second' FROM booked_at)) AS SECOND
FROM 
	bookings;