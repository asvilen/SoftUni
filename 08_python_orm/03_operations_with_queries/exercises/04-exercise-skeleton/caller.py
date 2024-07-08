import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species
    )

    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all()
    all_locations = [str(location) for location in locations]
    return "\n".join(all_locations)


def new_capital():
    first_loc = Location.objects.first()

    first_loc.is_capital = True
    first_loc.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount() -> None:
    cars = Car.objects.all()
    for car in cars:
        discount_perc = sum([int(year) for year in str(car.year)])
        price_with_discount = car.price * (100 - discount_perc) / 100
        car.price_with_discount = price_with_discount
        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    all_unfinished = [str(unfinished) for unfinished in Task.objects.filter(is_finished=False)]
    return "\n".join(all_unfinished)


def complete_odd_tasks():
    odd_tasks_pks = [task.pk for task in Task.objects.all() if task.pk % 2 != 0]
    Task.objects.filter(pk__in=odd_tasks_pks).update(is_finished=True)


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_deluxe_rooms = [str(r) for r in deluxe_rooms if r.id % 2 == 0]
    return '\n'.join(even_deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')  # id 1, id 2...

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue

        if previous_room_capacity is not None:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room() -> None:
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room() -> None:
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()
