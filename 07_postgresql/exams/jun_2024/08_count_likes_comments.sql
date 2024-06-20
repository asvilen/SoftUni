SELECT 
	ph.id AS photo_id,
	COUNT(DISTINCT li.id) AS likes_count,
	COUNT(DISTINCT co.id) AS comments_count
FROM photos AS ph
LEFT JOIN likes AS li
	ON ph.id = li.photo_id
LEFT JOIN comments AS co
	ON ph.id = co.photo_id
GROUP BY ph.id
ORDER BY 
	likes_count DESC,
	comments_count DESC,
	ph.id;