SELECT 
	CONCAT_WS(' ', mountain_range, peak_name) AS mountain_information,
	LENGTH(CONCAT_WS(' ', mountain_range, peak_name)) AS characters_length,
	BIT_LENGTH(CONCAT_WS(' ', mountain_range, peak_name)) AS bits_of_a_tring
FROM
	mountains AS mt
JOIN
	peaks AS pk
	ON 
	mt.id = pk.mountain_id;
