# Generated by Django 3.2.6 on 2021-08-26 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0002_course_credits"),
        ("colleges", "0004_auto_20210826_1028"),
    ]

    operations = [
        migrations.CreateModel(
            name="Major",
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
                ("abbreviation", models.CharField(max_length=10)),
            ],
            options={"ordering": ["abbreviation"],},
        ),
        migrations.CreateModel(
            name="CollegeMajor",
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
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="colleges.college",
                    ),
                ),
                (
                    "courses",
                    models.ManyToManyField(blank=True, null=True, to="courses.Course"),
                ),
                (
                    "major",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="majors.major"
                    ),
                ),
            ],
            options={"ordering": ["major"],},
        ),
    ]
