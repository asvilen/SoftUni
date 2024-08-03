from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.db.models import Count


# Create your models here.


def is_a_number(value):
    if not value.isdigit():
        raise ValidationError('Phone number must contain only digits.')


class AstronautManager(models.Manager):
    def get_astronauts_by_missions_count(self):
        return self\
            .annotate(missions_count=Count('missions'))\
            .order_by('-missions_count', 'phone_number')


class Astronaut(models.Model):
    objects = AstronautManager()

    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    phone_number = models.CharField(
        max_length=15,
        validators=[is_a_number],
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    spacewalks = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Spacecraft(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    manufacturer = models.CharField(
        max_length=100,
    )

    capacity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
    )

    weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    launch_date = models.DateField(
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=9,
        choices=[
            ('Planned', 'Planned'),
            ('Ongoing', 'Ongoing'),
            ('Completed', 'Completed')
        ],
        default='Planned',
    )

    launch_date = models.DateField(
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    spacecraft = models.ForeignKey(
        'Spacecraft',
        on_delete=models.CASCADE,
        related_name='missions'
    )

    astronauts = models.ManyToManyField(
        'Astronaut',
        related_name="missions",
    )

    commander = models.ForeignKey(
        'Astronaut',
        on_delete=models.SET_NULL,
        related_name='commanded_missions',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
