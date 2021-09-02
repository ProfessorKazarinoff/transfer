# articulations/urls.py

from django.urls import path

from .views import ArticulationDetailView, ArticulationFilterView, ArticulationListView

urlpatterns = [
    path(
        "articulation/<int:pk>/",
        ArticulationDetailView.as_view(),
        name="articulation_detail",
    ),
    path(
        "articulation_list/", ArticulationListView.as_view(), name="articulation_list"
    ),
    path("articulation_filter/", ArticulationFilterView, name="articulation_filter"),
]
