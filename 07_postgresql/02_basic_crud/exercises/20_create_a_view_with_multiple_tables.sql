CREATE OR REPLACE VIEW
	view_addresses
AS SELECT 
	CONCAT_WS(' ', first_name, last_name) AS full_name,
	department_id,
	CONCAT_WS(' ', number, street) AS address
FROM 
	employees AS e
JOIN 
	addresses AS a ON e.address_id = a.id
ORDER BY address;