SELECT 
	id || ' ' || username AS id_username,
	email
FROM accounts AS acc
JOIN accounts_photos AS aph
ON acc.id = aph.account_id
WHERE aph.account_id = aph.photo_id
ORDER BY account_id;
