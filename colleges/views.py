# colleges/views.py

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from majors.models import CollegeMajor

from .models import College


class CollegeDetailView(DetailView):
    model = College
    template_name = "college_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.college = get_object_or_404(College, slug=self.kwargs["slug"])
        context["college_major_list"] = CollegeMajor.objects.filter(
            college=self.college
        )
        return context


class CollegeListView(ListView):
    model = College
    template_name = "college_list.html"
