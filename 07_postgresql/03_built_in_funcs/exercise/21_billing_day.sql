ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPTZ default CURRENT_TIMESTAMP;


SELECT 
	TO_CHAR(billing_day, 'DD "DAY" MM "Month" YYYY "Year" HH24:MI:SS') AS "Billing Day"
FROM 
	bookings;