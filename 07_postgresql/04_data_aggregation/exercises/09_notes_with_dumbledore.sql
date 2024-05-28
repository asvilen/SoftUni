SELECT 
	last_name,
	COUNT(notes) AS notes_with_dumbledore
FROM 
	public.wizard_deposits
WHERE
	notes ILIKE '%Dumbledore%'
GROUP BY 
	last_name;
