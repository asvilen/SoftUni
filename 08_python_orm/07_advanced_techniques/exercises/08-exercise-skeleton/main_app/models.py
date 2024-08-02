from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.db import models


class RechargeEnergyMixin:

    def recharge_energy(self, amount: int):
        self.energy = min(100, self.energy + amount)
        self.save()


def validate_name(value):
    for char in value:
        if not (char.isalpha() or char.isspace()):
            raise ValidationError(
                "Name can only contain letters and spaces"
            )


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_name]
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18,"Age must be greater than or equal to 18")]
    )
    email = models.EmailField(
        error_messages={'invalid': "Enter a valid email address"}
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(
            regex=r'^\+359[0-9]{9}$',
            message="Phone number must start with '+359' followed by 9 digits"
        )]
    )
    website_url = models.URLField(
        error_messages={'invalid': "Enter a valid URL"}
    )


class BaseMedia(models.Model):
    class Meta:
        abstract = True
        ordering = ["-created_at", "title"]

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)


class Book(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'

    author = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, "Author must be at least 5 characters long")]
    )
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6, "ISBN must be at least 6 characters long")]
    )


class Movie(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'

    director = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8, "Director must be at least 8 characters long")]
    )


class Music(BaseMedia):
    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'

    artist = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(9, "Artist must be at least 9 characters long")]
    )


class Product(models.Model):
    TAX_RATE = 0.08
    SHIPPING_COSTS = 2.00

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self) -> Decimal:
        return self.price * Decimal(self.TAX_RATE)

    def calculate_shipping_cost(self, weight: Decimal) -> Decimal:
        return weight * Decimal(self.SHIPPING_COSTS)

    def format_product_name(self) -> str:
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    TAX_RATE = 0.05
    SHIPPING_COSTS = 1.5
    DISCOUNT = 0.2

    class Meta:
        proxy = True

    def calculate_price_without_discount(self) -> Decimal:
        return self.price * Decimal(1 + self.DISCOUNT)

    def calculate_tax(self) -> Decimal:
        return self.price * Decimal(self.TAX_RATE)

    def calculate_shipping_cost(self, weight: Decimal) -> Decimal:
        return weight * Decimal(self.SHIPPING_COSTS)

    def format_product_name(self) -> str:
        return f"Discounted Product: {self.name}"


class Hero(models.Model, RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField(validators=[MinValueValidator(0)])


class SpiderHero(Hero):
    SWING_ENERGY = 80

    class Meta:
        proxy = True

    def swing_from_buildings(self):
        if self.energy < self.SWING_ENERGY:
            return f"{self.name} as Spider Hero is out of web shooter fluid"

        self.energy -= self.SWING_ENERGY

        if self.energy == 0:
            self.energy = 1
        self.save()

        return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):
    RUN_ENERGY = 65

    class Meta:
        proxy = True

    def run_at_super_speed(self):
        if self.energy < self.RUN_ENERGY:
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.energy -= self.RUN_ENERGY

        if self.energy == 0:
            self.energy = 1
        self.save()

        return f"{self.name} as as Flash Hero runs at lightning speed, saving the day"



