# majors/views.py

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from courses.models import CourseType

from .models import CollegeMajor, Major


class MajorDetailView(DetailView):
    model = Major
    template_name = "major_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.major = get_object_or_404(Major, id=self.kwargs["pk"])
        context["college_major_list"] = CollegeMajor.objects.filter(major=self.major)
        return context


class MajorListView(ListView):
    model = Major
    template_name = "major_list.html"


class CollegeMajorDetailView(DetailView):
    model = CollegeMajor
    template_name = "college_major_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course_types"] = CourseType.objects.all()
        return context


class CollegeMajorListView(ListView):
    model = CollegeMajor
    template_name = "college_major_list.html"
