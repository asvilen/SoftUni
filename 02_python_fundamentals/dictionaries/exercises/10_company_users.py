companies_info = {}
while True:
    command = input().split(" -> ")
    if len(command) < 2:
        break
    company_name, employee_id = command[0], command[1]
    if company_name not in companies_info:
        companies_info[company_name] = []
    if employee_id not in companies_info[company_name]:
        companies_info[company_name].append(employee_id)
for company_name, employee_id in companies_info.items():
    print(company_name)
    for id in employee_id:
        print(f"-- {id}")