days = int(input())
total_amount_of_food = float(input())

day_counter = 0
biscuits_eaten = 0
dog_eaten = 0
cat_eaten = 0

for day in range(days):
    dog_portion = int(input())
    cat_portion = int(input())
    dog_eaten += dog_portion
    cat_eaten += cat_portion
    day_counter += 1
    if day_counter % 3 == 0:
        biscuits_eaten += (dog_portion + cat_portion) * 0.1

percent_eaten_food = (dog_eaten + cat_eaten) / total_amount_of_food * 100
percent_dog_eaten_food = dog_eaten / (dog_eaten + cat_eaten) * 100
percent_cat_eaten_food = cat_eaten / (dog_eaten + cat_eaten)  * 100

print(f"Total eaten biscuits: {round(biscuits_eaten)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_eaten_food:.2f}% eaten from the dog.")
print(f"{percent_cat_eaten_food:.2f}% eaten from the cat.")