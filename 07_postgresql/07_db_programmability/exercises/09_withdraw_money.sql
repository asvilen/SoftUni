CREATE OR REPLACE PROCEDURE sp_withdraw_money(
	account_id INT,
	money_amount NUMERIC(4)
)
AS
$$
DECLARE
	account_balance NUMERIC;
BEGIN
	account_balance := (SELECT balance FROM accounts WHERE id = account_id);
	IF money_amount > account_balance THEN
		RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
	ELSE
		UPDATE
			accounts
		SET 
			balance = balance - money_amount
		WHERE 
			id = account_id;
	END IF;
END;
$$
LANGUAGE plpgsql;
