SELECT
	CONCAT_WS(' ', address, address_2) AS apartment_address,
	booked_for AS nights
FROM 
	apartments AS a
JOIN 
	bookings AS b
	USING (booking_id)
ORDER BY 
	a.apartment_id;
