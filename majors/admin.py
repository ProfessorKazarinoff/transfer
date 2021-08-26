# majors/admin.py

from django.contrib import admin

from .models import CollegeMajor, Major

admin.site.register(Major)
admin.site.register(CollegeMajor)
