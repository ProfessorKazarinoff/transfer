# articulations/models.py

from django.db import models
from django.urls import reverse
from courses.models import Course

class Articulation(models.Model):
    course1 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course1")
    course2 = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course2")
    URL = models.URLField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.course1.number} at {self.course1.college.abbreviation} --> {self.course2.number} at {self.course2.college.abbreviation}"

    def get_absolute_url(self):
        return reverse("articulation_detail", args=[str(self.id)])
