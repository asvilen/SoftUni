CREATE OR REPLACE PROCEDURE udp_modify_account(
	address_street VARCHAR(30), 
	address_town VARCHAR(30)
)
AS
$$
BEGIN
	UPDATE accounts
	SET job_title = '(Remote) ' || job_title
	WHERE id = (
		SELECT acc.id
		FROM accounts AS acc
		JOIN addresses AS add
			ON acc.id = add.account_id
		WHERE street = address_street
		AND town = address_town
	);
END;
$$

LANGUAGE plpgsql;
