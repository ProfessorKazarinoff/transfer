# majors/urls.py

from django.urls import path

from .views import (
    CollegeMajorDetailView,
    CollegeMajorListView,
    MajorDetailView,
    MajorListView,
)

urlpatterns = [
    path("major_list/", MajorListView.as_view(), name="major_list"),
    path("major/<int:pk>/", MajorDetailView.as_view(), name="major_detail"),
    path(
        "college_major_list/", CollegeMajorListView.as_view(), name="college_major_list"
    ),
    path(
        "college_major/<int:pk>/",
        CollegeMajorDetailView.as_view(),
        name="college_major_detail",
    ),
]
