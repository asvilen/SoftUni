SELECT 
	e.id,
	e.first_name,
	e.last_name,
	e.salary,
	e.department_id,
	CASE
		WHEN department_id = 1 THEN 'Management'
		WHEN department_id = 2 THEN 'Kitchen Staff'
		WHEN department_id = 3 THEN 'Service Staff'
		ELSE 'Other'
	END AS perartment_name
FROM 
	employees AS e;