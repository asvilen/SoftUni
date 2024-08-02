import os

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from typing import List
from django.db.models import Case, When, Value


def show_highest_rated_art() -> str:
    highest_rater_art = ArtworkGallery.objects.order_by("-rating", "id").first()
    return f"{highest_rater_art.art_name} is the highest-rated art with a {highest_rater_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop() -> str:
    most_expensive_laptop = Laptop.objects.order_by("-price", "-id").first()
    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=('Asus', 'Lenovo')).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=('Apple', 'Dell', 'Acer')).update(memory=16)


def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
            When(brand='Asus', then=Value("Windows")),
            When(brand='Apple', then=Value("MacOS")),
            When(brand__in=('Dell', 'Acer'), then=Value("Linux")),
            When(brand='Lenovo', then=Value("Chrome OS")),
        )
    )


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title__contains="GM").update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title='no title').update(games_won=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2500).update(title="GM")


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title="IM")


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title="FM")


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title="regular player")


def set_new_chefs() -> None:
    Meal.objects.update(
        chef=Case(
            When(meal_type="Breakfast", then=Value("Gordon Ramsay")),
            When(meal_type="Lunch", then=Value("Julia Child")),
            When(meal_type="Dinner", then=Value("Jamie Oliver")),
            When(meal_type="Snack", then=Value("Thomas Keller")),
        )
    )


def set_new_preparation_times() -> None:
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type="Breakfast", then=Value("10 minutes")),
            When(meal_type="Lunch", then=Value("12 minutes")),
            When(meal_type="Dinner", then=Value("15 minutes")),
            When(meal_type="Snack", then=Value("5 minutes")),
        )
    )


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=("Breakfast", "Dinner")).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=("Lunch", "Snack")).delete()


def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(
        difficulty="Hard"
    ).order_by("-location")  # Z - A

    return "\n".join(str(d) for d in hard_dungeons)


def bulk_create_dungeons(args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(args)


def update_dungeon_names() -> None:
    Dungeon.objects.filter(
        difficulty="Easy"
    ).update(name="The Erased Thombs")

    Dungeon.objects.filter(
        difficulty="Medium"
    ).update(name="The Coral Labyrinth")

    Dungeon.objects.filter(
        difficulty="Hard"
    ).update(name="The Lost Haunt")


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(
        difficulty="Easy"
    ).update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.filter(
        difficulty="Easy"
    ).update(recommended_level=25)

    Dungeon.objects.filter(
        difficulty="Medium"
    ).update(recommended_level=50)

    Dungeon.objects.filter(
        difficulty="Hard"
    ).update(recommended_level=75)


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(
        boss_health=500
    ).update(reward="1000 Gold")

    Dungeon.objects.filter(
        location__startswith="E"
    ).update(reward="New dungeon unlocked")
    # UPDATE dungeon
    # SET reward = "New dungeon unlocked"
    # WHERE location LIKE "E%"

    Dungeon.objects.filter(
        location__endswith="s"
    ).update(reward="Dragonheart Amulet")
    # UPDATE dungeon
    # SET reward = "New dungeon unlocked"
    # WHERE location LIKE "%s"


def set_new_locations() -> None:
    Dungeon.objects.filter(
        recommended_level=25
    ).update(location="Enchanted Maze")

    Dungeon.objects.filter(
        recommended_level=50
    ).update(location="Grimstone Mines")

    Dungeon.objects.filter(
        recommended_level=75
    ).update(location="Shadowed Abyss")


def show_workouts() -> str:
    workouts = Workout.objects.filter(
        workout_type__in=("Calisthenics", "CrossFit")
    ).order_by("id")

    return "\n".join([
        f"{w.workout_name} from {w.workout_type} type has {w.difficulty} difficulty!"
        for w in workouts
    ])


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(
        workout_type="Cardio",
        difficulty="High"
    ).order_by('instructor')


def set_new_instructors() -> None:
    Workout.objects.filter(workout_type="Cardio").update(instructor="John Smith")
    Workout.objects.filter(workout_type="Strength").update(instructor="Michael Williams")
    Workout.objects.filter(workout_type="Yoga").update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type="CrossFit").update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type="Calisthenics").update(instructor="Chris Heria")


def set_new_duration_times() -> None:
    Workout.objects.filter(instructor="John Smith").update(duration="15 minutes")
    Workout.objects.filter(instructor="Sarah Davis").update(duration="30 minutes")
    Workout.objects.filter(instructor="Chris Heria").update(duration="45 minutes")
    Workout.objects.filter(instructor="Michael Williams").update(duration="1 hour")
    Workout.objects.filter(instructor="Emily Johnson").update(duration="1 hour and 30 minutes")


def delete_workouts() -> None:
    Workout.objects.exclude(
        workout_type__in=("Calisthenics", "Strength")
    ).delete()