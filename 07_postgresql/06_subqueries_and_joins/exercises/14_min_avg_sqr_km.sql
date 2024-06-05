SELECT 
    MIN(avg) 
FROM 
    (
	SELECT
		AVG(area_in_sq_km)
	FROM 
		public.countries
	GROUP BY 
		continent_code
) AS average;
