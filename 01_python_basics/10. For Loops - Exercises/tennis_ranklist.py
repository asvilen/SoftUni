from math import floor

tour_count = int(input())
starting_points = int(input())

tour_points = 0
wins = 0

for tour in range(tour_count):
    tour_stage = input()
    if tour_stage == "W":
        tour_points += 2000
        wins += 1
    elif tour_stage == "F":
        tour_points += 1200
    elif tour_stage == "SF":
        tour_points += 720
final_points = starting_points + tour_points
average_points = tour_points / tour_count
win_perc = wins / tour_count * 100
print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_perc:.2f}%")