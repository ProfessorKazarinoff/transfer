# majors/tests.py

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from colleges.models import College
from courses.models import Course

from .models import CollegeMajor, Major


class MajorListPageTests(TestCase):
    def test_major_list_page_status_code(self):
        response = self.client.get("/majors/major_list/")
        self.assertEqual(response.status_code, 200)

    def test_major_list_view_uses_correct_template(self):
        response = self.client.get(reverse("major_list"))
        self.assertTemplateUsed(response, "major_list.html")


class MajorTests(TestCase):
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
        course = Course.objects.get(id=1)
        Major.objects.create(
            name="Mechanical Engineering",
            abbreviation="ME",
            description="Study of mechanical components",
        )

    def test_text_content(self):
        major = Major.objects.get(id=1)
        expected_object_name = f"{major.abbreviation} - {major.name}"
        self.assertEquals(
            expected_object_name,
            "ME - Mechanical Engineering",
        )

    def test_major_list_view(self):
        response = self.client.get(reverse("major_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mechanical Engineering")
        self.assertTemplateUsed(response, "major_list.html")

    def test_major_detail_view(self):
        major = Major.objects.get(id=1)
        response = self.client.get(reverse("major_detail", args=[str(major.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ME")
        self.assertTemplateUsed(response, "major_detail.html")
