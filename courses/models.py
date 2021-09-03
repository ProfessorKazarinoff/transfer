# courses/models.py

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from colleges.models import College


class CourseType(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(unique=True)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("course_type_detail", args=[str(self.id)])


class Course(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    credits = models.FloatField(null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    course_type = models.ForeignKey(
        CourseType, null=True, blank=True, on_delete=models.CASCADE
    )
    pre_reqs = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=600, blank=True)
    course_outcomes = models.TextField(max_length=1000, blank=True)
    URL = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = [
            "college",
            "number",
        ]

    def __str__(self):
        return f"{self.number} {self.name} at {self.college}"

    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.id)])
