CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT AS
$$
	BEGIN
		RETURN 
			
				COUNT(*)
			FROM
				employees AS e
			JOIN
				addresses AS a
			USING
				(address_id)
			JOIN 
				towns
			USING
				(town_id)
			WHERE 
				name = town_name;
	END;
$$
LANGUAGE plpgsql
;
