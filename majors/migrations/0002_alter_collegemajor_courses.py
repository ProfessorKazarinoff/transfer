# Generated by Django 3.2.6 on 2021-08-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_course_credits"),
        ("majors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collegemajor",
            name="courses",
            field=models.ManyToManyField(blank=True, to="courses.Course"),
        ),
    ]
