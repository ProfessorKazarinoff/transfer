# colleges/models.py

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class College(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    URL = models.URLField()
    slug = models.CharField(max_length=10, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("college_detail", args=[str(self.slug)])
