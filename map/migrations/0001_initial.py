# Generated by Django 5.1.7 on 2025-03-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=100)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=12, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=12, null=True
                    ),
                ),
            ],
        ),
    ]
