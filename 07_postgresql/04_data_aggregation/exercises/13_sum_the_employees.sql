SELECT 
	COUNT(*) FILTER (WHERE department_id = 1) AS "Engineering",
	COUNT(*) FILTER (WHERE department_id = 2) AS "Tool Design",
	COUNT(*) FILTER (WHERE department_id = 3) AS "Sales",
	COUNT(*) FILTER (WHERE department_id = 4) AS "Marketing",
	COUNT(*) FILTER (WHERE department_id = 5) AS "Purchasing",
	COUNT(*) FILTER (WHERE department_id = 6) AS "Research and Development",
	COUNT(*) FILTER (WHERE department_id = 7) AS "Production"
FROM 
	employees AS e;
