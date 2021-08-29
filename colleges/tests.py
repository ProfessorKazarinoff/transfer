# colleges/tests.py

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser

from .models import College


class CollegesListPageTests(TestCase):
    def test_colleges_list_page_status_code(self):
        response = self.client.get("/colleges/college_list/")
        self.assertEqual(response.status_code, 200)

    def test_colleges_list_view_uses_correct_template(self):
        response = self.client.get(reverse("college_list"))
        self.assertTemplateUsed(response, "college_list.html")


class CollegeTests(TestCase):
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

    def test_text_content(self):
        college = College.objects.get(id=1)
        expected_object_name = f"{college.name} - {college.abbreviation}"
        self.assertEquals(expected_object_name, "Mt. Hood Community College - MHCC")

    def test_college_list_view(self):
        response = self.client.get(reverse("college_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "is in Gresham, OR")
        self.assertTemplateUsed(response, "college_list.html")

    def test_college_detail_view(self):
        college = College.objects.get(id=1)
        response = self.client.get(reverse("college_detail", args=[str(college.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mt. Hood Community College")
        self.assertTemplateUsed(response, "college_detail.html")
