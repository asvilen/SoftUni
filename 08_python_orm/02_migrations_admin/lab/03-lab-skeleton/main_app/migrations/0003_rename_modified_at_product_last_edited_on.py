# Generated by Django 5.0.4 on 2024-06-23 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_product_created_on_product_modified_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='modified_at',
            new_name='last_edited_on',
        ),
    ]