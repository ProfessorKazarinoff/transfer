# Generated by Django 3.2.6 on 2021-09-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0007_alter_course_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursetype", name="name", field=models.CharField(max_length=50),
        ),
    ]
