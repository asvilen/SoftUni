SELECT 
	town_id,
	name,
	address_text
FROM 
	addresses
JOIN 
	towns
	USING(town_id)
WHERE 
	name IN ('San Francisco', 'Sofia', 'Carnation')
ORDER BY 
	town_id,
	address_id;
