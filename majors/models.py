# majors/models.py

from django.db import models
from django.urls import reverse

from colleges.models import College
from courses.models import Course


class Major(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ["abbreviation"]

    def __str__(self):
        return f"{self.abbreviation} - {self.name}"

    def get_absolute_url(self):
        return reverse("major_detail", args=[str(self.id)])


class CollegeMajor(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, null=True, blank=True)
    courses = models.ManyToManyField(Course, blank=True)

    class Meta:
        ordering = ["major"]

    def __str__(self):
        return f"{self.major.abbreviation} - {self.major.name} at {self.college.abbreviation}"

    def get_absolute_url(self):
        return reverse("college_major_detail", args=[str(self.id)])
