SELECT 
	magic_wand_creator,
	MIN(magic_wand_size) AS minimum_wand_size
FROM 
	public.wizard_deposits
GROUP BY 
	magic_wand_creator
ORDER BY 
	minimum_wand_size
LIMIT 5;
