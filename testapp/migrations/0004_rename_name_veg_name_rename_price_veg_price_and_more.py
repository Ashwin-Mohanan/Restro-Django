# Generated by Django 4.0.2 on 2022-03-25 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_veg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veg',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='veg',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='veg',
            old_name='Taste',
            new_name='taste',
        ),
    ]
