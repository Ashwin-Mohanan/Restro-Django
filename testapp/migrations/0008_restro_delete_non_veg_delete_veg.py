# Generated by Django 4.0.2 on 2022-03-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_rename_name_non_veg_nv_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Taste', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Non_Veg',
        ),
        migrations.DeleteModel(
            name='Veg',
        ),
    ]
