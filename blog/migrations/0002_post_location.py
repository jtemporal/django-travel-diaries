# Generated by Django 5.1.7 on 2025-03-09 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
        ("map", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="place",
                to="map.location",
            ),
        ),
    ]
