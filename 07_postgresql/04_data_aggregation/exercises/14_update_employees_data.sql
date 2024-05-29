UPDATE employees
SET 
job_title =  
	CASE 
		WHEN hire_date < '2015-01-16' 
		THEN 'Senior ' || job_title 
		ELSE 'Mid-' || job_title
	END,
salary = 
	CASE 
		WHEN hire_date < '2015-01-16' 
		THEN salary + 2500
		ELSE salary + 1500
	END
WHERE hire_date < '2020-03-04';
