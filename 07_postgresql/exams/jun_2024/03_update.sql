UPDATE addresses 
SET country = nv.cntry
FROM
    ( VALUES
        ('B', 'Blocked'),
        ('T', 'Test'),
        ('P', 'In Progress')
    ) as nv (sub, cntry)
WHERE SUBSTRING(country, 1, 1) = nv.sub;
