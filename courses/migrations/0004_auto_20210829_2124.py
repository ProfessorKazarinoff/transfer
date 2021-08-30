# Generated by Django 3.2.6 on 2021-08-30 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_auto_20210829_0918"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseType",
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
                ("name", models.CharField(max_length=30)),
                ("order", models.IntegerField(unique=True)),
                ("description", models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="course_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="courses.coursetype",
            ),
        ),
    ]
