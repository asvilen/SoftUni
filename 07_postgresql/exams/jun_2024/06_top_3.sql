SELECT
	ph.id AS photo_id,
	ph.capture_date,
	ph.description,
	COUNT(*) AS comments_count
FROM photos AS ph
JOIN comments AS co
	ON ph.id = co.photo_id
WHERE description IS NOT NULL
GROUP BY 
	ph.id,
	ph.capture_date,
	ph.description
ORDER BY 
	comments_count DESC,
	photo_id
LIMIT 3;
