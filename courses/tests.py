# courses/tests.py

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from colleges.models import College

from .models import Course


class CoursesListPageTests(TestCase):
    def test_courses_list_page_status_code(self):
        response = self.client.get("/courses/course_list/")
        self.assertEqual(response.status_code, 200)

    def test_courses_list_view_uses_correct_template(self):
        response = self.client.get(reverse("course_list"))
        self.assertTemplateUsed(response, "course_list.html")


class CourseTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="peter", email="peter@peter.com", password="top_secret"
        )
        College.objects.create(
            name="Mt. Hood Community College",
            abbreviation="MHCC",
            URL="https://mhcc.edu/",
            slug="mhcc",
            description="Mt. Hood Community College is in Gresham, OR",
            added_by=self.user,
        )
        college = College.objects.get(id=1)
        Course.objects.create(
            number="ENGR 114",
            name="Engineering Programming",
            credits=4.0,
            college=college,
            pre_reqs="ENGR 101",
            description="An engineering programming course",
            course_outcomes="test outcomes",
            URL="https://www.pcc.edu/ccog/engr/114/",
            added_by=self.user,
        )

    def test_text_content(self):
        course = Course.objects.get(id=1)
        expected_object_name = f"{course.number} {course.name} at {course.college}"
        self.assertEquals(
            expected_object_name,
            "ENGR 114 Engineering Programming at Mt. Hood Community College",
        )

    def test_course_list_view(self):
        response = self.client.get(reverse("course_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 114")
        self.assertTemplateUsed(response, "course_list.html")

    def test_course_detail_view(self):
        course = Course.objects.get(id=1)
        response = self.client.get(reverse("course_detail", args=[str(course.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 114")
        self.assertTemplateUsed(response, "course_detail.html")
