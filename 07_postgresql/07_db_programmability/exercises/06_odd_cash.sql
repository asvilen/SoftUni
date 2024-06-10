CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
	game_name VARCHAR(50)
) RETURNS TABLE (
	total_cash NUMERIC
)
AS
$$
	DECLARE
		-- total_cash NUMERIC;
	BEGIN
		RETURN QUERY
		WITH total AS (
			SELECT 
				cash,
				ROW_NUMBER() OVER(ORDER BY ug.cash DESC) AS rn
			FROM users_games AS ug
			JOIN games AS g ON ug.game_id = g.id
			WHERE g.name = game_name
		)
		SELECT ROUND(SUM(cash), 2) AS total_cash
		FROM total
		WHERE rn = (SELECT rn FROM total WHERE rn % 2 = 1);
		
	END;
	
$$
LANGUAGE plpgsql;
