# Generated by Django 4.2.7 on 2023-12-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("function", "0001_initial"),
        ("role", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="functions",
            field=models.ManyToManyField(to="function.function"),
        ),
    ]
