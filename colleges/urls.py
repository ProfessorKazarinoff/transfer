# colleges/urls.py

from django.urls import path

from .views import CollegeDetailView, CollegeListView

urlpatterns = [
    path("college_list/", CollegeListView.as_view(), name="college_list"),
    path("college/<int:pk>/", CollegeDetailView.as_view(), name="college_detail"),
]
