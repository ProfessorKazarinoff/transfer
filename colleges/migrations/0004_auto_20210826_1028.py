# Generated by Django 3.2.6 on 2021-08-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("colleges", "0003_college_slug"),
    ]

    operations = [
        migrations.RemoveField(model_name="college", name="abbreviationn",),
        migrations.AddField(
            model_name="college",
            name="abbreviation",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
