# Generated by Django 4.2.7 on 2023-12-09 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("role", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "username",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254)),
                ("dni", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=16)),
                ("status", models.BooleanField(default=True)),
                ("roles", models.ManyToManyField(to="role.role")),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
                "db_table": "sec_user",
            },
        ),
    ]
