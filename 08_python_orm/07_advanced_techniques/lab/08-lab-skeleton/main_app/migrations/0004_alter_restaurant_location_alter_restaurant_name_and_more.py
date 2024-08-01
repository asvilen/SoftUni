# Generated by Django 5.0.4 on 2024-07-31 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, message='Location must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(200, 'Location cannot exceed 200 characters.')]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, 'Name must be at least 2 characters long.'), django.core.validators.MaxLengthValidator(100, message='Name cannot exceed 100 characters.')]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0, 'Rating must be at least 0.00.'), django.core.validators.MaxValueValidator(5.0, 'Rating cannot exceed 5.00.')]),
        ),
    ]
