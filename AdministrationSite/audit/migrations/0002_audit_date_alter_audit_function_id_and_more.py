# Generated by Django 4.2.7 on 2023-12-09 20:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("function", "0001_initial"),
        ("audit", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="audit",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="audit",
            name="function_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="function.function",
            ),
        ),
        migrations.AlterField(
            model_name="audit",
            name="observation",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="audit",
            name="user_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.user",
            ),
        ),
    ]
