# Generated by Django 4.2.1 on 2023-07-03 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("first_name", models.CharField(max_length=25)),
                ("last_name", models.CharField(max_length=25)),
                ("user_name", models.CharField(max_length=25)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Section",
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
                ("name", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Writing.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Page",
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
                ("title", models.CharField(max_length=50)),
                ("text", models.TextField()),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Writing.section",
                    ),
                ),
            ],
        ),
    ]
