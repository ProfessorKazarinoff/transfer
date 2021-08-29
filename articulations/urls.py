# articulations/urls.py

from django.urls import path

from .views import ArticulationDetailView, ArticulationListView

urlpatterns = [
    path(
        "articulation/<int:pk>/",
        ArticulationDetailView.as_view(),
        name="articulation_detail",
    ),
    path(
        "articulation_list/", ArticulationListView.as_view(), name="articulation_list"
    ),
]
