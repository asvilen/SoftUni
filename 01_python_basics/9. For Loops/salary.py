tab_count = int(input())
salary = int(input())

copy_salary = salary

for tabs in range(1, tab_count + 1):
    current_tab = input()
    if current_tab == "Facebook":
        copy_salary -= 150
    elif current_tab == "Instagram":
        copy_salary -= 100
    elif current_tab == "Reddit":
        copy_salary -= 50

    if copy_salary <= 0:
        break

if copy_salary <= 0:
    print("You have lost your salary.")
else:
    print(copy_salary)