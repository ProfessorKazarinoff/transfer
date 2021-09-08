# courses/views.py

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from articulations.models import Articulation

from .models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articulation_list"] = Articulation.objects.filter(
            course1_id=self.kwargs["pk"]
        )
        return context


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
