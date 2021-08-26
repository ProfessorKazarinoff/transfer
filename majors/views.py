# majors/views.py

from django.views.generic import DetailView, ListView

from .models import Major


class MajorDetailView(DetailView):
    model = Major
    template_name = "major_detail.html"


class MajorListView(ListView):
    model = Major
    template_name = "major_list.html"
