# Generated by Django 4.1.3 on 2022-11-19 21:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("region", models.CharField(max_length=100)),
                ("biome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Sighting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("date", models.DateField()),
                ("start_time", models.TimeField(default=datetime.time(1, 0))),
                ("distance", models.IntegerField(default=1)),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sightings.region",
                    ),
                ),
            ],
        ),
    ]
