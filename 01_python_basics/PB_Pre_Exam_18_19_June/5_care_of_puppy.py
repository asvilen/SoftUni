available_food = int(input())
command = input()

available_food *= 1000
grams_eaten_food = 0

while command != "Adopted":
    grams_eaten_food += int(command)
    command = input()

difference = abs(available_food - grams_eaten_food)

if grams_eaten_food <= available_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")