contest_passwords_dict = {}
users_dict = {}
while True:
    first_inputs = input()
    if first_inputs == "end of contests":
        break
    contest, password_for_contest = first_inputs.split(":")
    contest_passwords_dict[contest] = password_for_contest

while True:
    second_inputs = input()
    if second_inputs == "end of submissions":
        break
    contest, password, username, points = second_inputs.split("=>")
    if contest in contest_passwords_dict:
        if contest_passwords_dict[contest] == password:
            if username in users_dict:
                if contest in users_dict[username]:
                    users_dict[username][contest] = max(int(points), users_dict[username][contest])
                else:
                    users_dict[username][contest] = int(points)
            else:
                users_dict[username] = {}
                users_dict[username][contest] = int(points)
best_score = 0
best_candidate = ""
for user in users_dict:
    total = 0
    for contest in users_dict[user]:
        total += users_dict[user][contest]
    if total > best_score:
        best_score = total
        best_candidate = user

print(f"Best candidate is {best_candidate} with total {best_score} points.")
print("Ranking:")
for user in sorted(users_dict):
    print(user)
    sorted_dict = dict(sorted(users_dict[user].items(), key=lambda x: x[1], reverse=True))
    for contest in sorted_dict.keys():
        print(f"#  {contest} -> {sorted_dict[contest]}")
