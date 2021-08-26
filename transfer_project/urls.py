# transfer_project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("colleges/", include("colleges.urls")),
    path("courses/", include("courses.urls")),
    path("", include("pages.urls")),
]
