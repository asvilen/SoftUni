import os
import django
from django.db.models import Count, Q, Sum, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission
# Create queries within functions


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    matches = Astronaut.objects.filter(query).order_by('name')

    if not matches.exists():
        return ""

    result = [
        (f"Astronaut: {astr.name}, "
         f"phone number: {astr.phone_number}, "
         f"status: {'Active' if astr.is_active else 'Inactive'}")
        for astr
        in matches
    ]
    return "\n".join(result)


def get_top_astronaut():
    top_astro = Astronaut.objects\
        .get_astronauts_by_missions_count()\
        .filter(missions_count__gt=0)\
        .order_by('phone_number')\
        .first()

    if top_astro:
        return f"Top Astronaut: {top_astro.name} with {top_astro.missions_count} missions."
    return "No data."


def get_top_commander():
    top_commander = Astronaut.objects\
        .annotate(commanders_count=Count('commanders'))\
        .filter(commanders_count__gt=0)\
        .order_by('phone_number')\
        .first()

    if top_commander:
        return f"Top Commander: {top_commander.name} with {top_commander.commanders_count} commanded missions."
    return "No data."


def get_last_completed_mission():
    last_completed_mission = Mission.objects\
        .filter(status='Completed')\
        .order_by('-launch_date')\
        .first()

    if not last_completed_mission:
        return "No data."

    commander_name = last_completed_mission.commander.name if last_completed_mission.commander else 'TBA'
    astronauts = last_completed_mission.astronauts.order_by('name')
    astronauts_names = [astr.name for astr in astronauts]
    total_spacewalks = sum([astr.spacewalks for astr in astronauts])

    return (f"The last completed mission is: {last_completed_mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {', '.join(astronauts_names)}. "
            f"Spacecraft: {last_completed_mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():
    # Get all spacecrafts with the count of missions and unique astronauts
    spacecrafts = Spacecraft.objects.annotate(
        num_missions=Count('spacecrafts', distinct=True),
        num_astronauts=Count('spacecrafts__astronauts', distinct=True)
    ).filter(num_missions__gt=0).order_by('-num_missions', 'name')

    # Check if we have any spacecrafts
    if not spacecrafts.exists():
        return "No data."

    # Get the first spacecraft in the ordered list
    most_used_spacecraft = spacecrafts.first()

    # Construct the result string
    result = (
        f"The most used spacecraft is: {most_used_spacecraft.name}, "
        f"manufactured by {most_used_spacecraft.manufacturer}, "
        f"used in {most_used_spacecraft.num_missions} missions, "
        f"astronauts on missions: {most_used_spacecraft.num_astronauts}."
    )

    return result


def decrease_spacecrafts_weight():
    # Get all spacecrafts currently assigned to planned missions
    planned_spacecrafts = Spacecraft.objects.filter(
        spacecrafts__status='Planned',
        weight__gte=200.0
    ).distinct()

    # Check if there are any spacecrafts to update
    if not planned_spacecrafts.exists():
        return "No changes in weight."

    # Decrease weight by 200.0 kg for each eligible spacecraft
    num_of_spacecrafts_affected = 0
    for spacecraft in planned_spacecrafts:
        new_weight = spacecraft.weight - 200.0
        spacecraft.weight = max(new_weight, 0.0)
        spacecraft.save()
        num_of_spacecrafts_affected += 1

    # Calculate the new average weight of all spacecrafts
    avg_weight = Spacecraft.objects.aggregate(
        avg_weight=Avg('weight')
    )['avg_weight']

    # Format the result
    result = (
        f"The weight of {num_of_spacecrafts_affected} spacecrafts has been decreased. "
        f"The new average weight of all spacecrafts is {avg_weight:.1f}kg"
    )

    return result


