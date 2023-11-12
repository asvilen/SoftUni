opened_tabs = int(input())
salary = int(input())

penalty = 0

for tab in range(opened_tabs):
    page = input()
    if page == "Facebook":
        penalty += 150
    elif page == "Instagram":
        penalty += 100
    elif page == "Reddit":
        penalty += 50
    if penalty >= salary:
        break
if salary > penalty:
    difference = salary - penalty
    print(difference)
else:
    print(f"You have lost your salary.")