# Generated by Django 4.2.7 on 2023-12-09 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
        ("function", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Audit",
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
                ("action", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("observation", models.TextField()),
                ("ip", models.CharField(max_length=16)),
                (
                    "function_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="function.function",
                    ),
                ),
                (
                    "user_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.user"
                    ),
                ),
            ],
            options={
                "verbose_name": "Audit",
                "verbose_name_plural": "Audits",
                "db_table": "sec_audit",
            },
        ),
    ]
