CREATE OR REPLACE FUNCTION fn_full_name(
	first_name VARCHAR(20), 
	last_name VARCHAR(20)
)
RETURNS VARCHAR(40)
AS
$$
	DECLARE
		first_name VARCHAR(20) = INITCAP(first_name);
		last_name VARCHAR(20) = INITCAP(last_name);
	BEGIN
	
		IF first_name IS NULL AND last_name IS NULL THEN
			RETURN NULL;
		ELSEIF first_name IS NULL THEN
			RETURN last_name;
		ELSEIF last_name IS NULL THEN
			RETURN first_name;
		END IF;

		RETURN CONCAT_WS(' ', first_name, last_name);
	END;
$$
LANGUAGE plpgsql;
