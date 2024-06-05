SELECT
	country_name,
	river_name
FROM
	countries AS c
LEFT JOIN
	countries_rivers AS cr
USING
	(country_code)
LEFT JOIN 
	rivers AS r
ON
	cr.river_id = r.id
WHERE 
	continent_code = 'AF'
ORDER BY
	country_name
LIMIT 5;
