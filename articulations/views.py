# articulations/views.py
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Articulation


class ArticulationListView(ListView):
    model = Articulation
    template_name = "articulation_list.html"


class ArticulationDetailView(DetailView):
    model = Articulation
    template_name = "articulation_detail.html"


def ArticulationFilterView(request):
    qs = Articulation.objects.all()
    university_query = request.GET.get("university")
    communitycollege_query = request.GET.get("communitycollege")
    context = {"queryset": qs.filter()}

    return render(request, "articulation_filter.html", context)
