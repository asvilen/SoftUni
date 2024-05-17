SELECT 
	REPLACE(title, 'The', '***') AS title
FROM 
	books
WHERE title ILIKE 'The%';