CREATE OR REPLACE VIEW view_continents_countries_currencies_details
AS
SELECT
	CONCAT_WS(
		': ', 
		TRIM(continent_name),
		continent_code
	) AS continent_details,
	CONCAT_WS(
		' - ',
		country_name,
		capital,
		area_in_sq_km,
		'km2'
	) AS country_information,
	CONCAT(description, ' (', currency_code, ')') AS currencies
FROM 
	continents AS con
JOIN 
	countries AS cou
	USING(continent_code)
JOIN 
	currencies
	USING(currency_code)
ORDER BY 
	country_information, currencies;
