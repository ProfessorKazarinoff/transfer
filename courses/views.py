# courses/views.py

from django.views.generic import DetailView, ListView

from .models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
