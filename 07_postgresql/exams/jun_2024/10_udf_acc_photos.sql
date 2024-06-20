CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
	account_username VARCHAR(30)
) RETURNS INT
AS
$$
BEGIN
	RETURN (
		SELECT COUNT(*)
		FROM accounts AS acc
		JOIN accounts_photos AS ap
			ON acc.id = ap.account_id
		WHERE username = account_username
	);
END;
$$
LANGUAGE plpgsql;
