# Generated by Django 2.2.3 on 2019-07-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0102_unique_slug_attributes")]

    operations = [
        migrations.AddField(
            model_name="attribute",
            name="available_in_grid",
            field=models.BooleanField(blank=True, default=True),
        )
    ]