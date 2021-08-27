# majors/views.py

from django.views.generic import DetailView, ListView

from .models import CollegeMajor, Major


class MajorDetailView(DetailView):
    model = Major
    template_name = "major_detail.html"


class MajorListView(ListView):
    model = Major
    template_name = "major_list.html"


class CollegeMajorDetailView(DetailView):
    model = CollegeMajor
    template_name = "college_major_detail.html"


class CollegeMajorListView(ListView):
    model = CollegeMajor
    template_name = "college_major_list.html"
