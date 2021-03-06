# Generated by Django 3.2.6 on 2021-08-28 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0002_course_credits"),
    ]

    operations = [
        migrations.CreateModel(
            name="Articulation",
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
                ("URL", models.URLField(blank=True, null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "course1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course1",
                        to="courses.course",
                    ),
                ),
                (
                    "course2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course2",
                        to="courses.course",
                    ),
                ),
            ],
        ),
    ]
