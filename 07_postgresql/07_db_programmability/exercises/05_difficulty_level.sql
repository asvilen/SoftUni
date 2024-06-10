CREATE OR REPLACE FUNCTION fn_difficulty_level(
	level INT
) RETURNS VARCHAR(50)
AS
$$
	DECLARE
		difficulty_level VARCHAR(50);
	BEGIN
	    CASE
	        WHEN level <= 40 THEN
	            difficulty_level := 'Normal Difficulty';
	
	        WHEN level <= 60 THEN
	            difficulty_level := 'Nightmare Difficulty';
	        ELSE
	            difficulty_level := 'Hell Difficulty';
	    END CASE;
	
	    RETURN difficulty_level;
	END;
	
$$
LANGUAGE plpgsql;