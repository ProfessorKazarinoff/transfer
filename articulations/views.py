# articulations/views.py

from django.views.generic import ListView, DetailView

from .models import Articulation

class ArticulationListView(ListView):
    model = Articulation
    template_name = "articulation_list.html"

class ArticulationDetailView(DetailView):
    model = Articulation
    template_name = "articulation_detail.html"
