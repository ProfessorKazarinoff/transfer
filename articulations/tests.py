# articulations/tests.py

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from colleges.models import College
from courses.models import Course
from .models import Articulation


class ArticulationTests(TestCase):
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
        College.objects.create(
            name="Portland State University",
            abbreviation="PSU",
            URL="https://pdx.edu/",
            slug="psu",
            description="Portland State University is in Portland, OR",
            added_by=self.user,
        )
        college1 = College.objects.get(id=1)
        college2 = College.objects.get(id=2)
        Course.objects.create(
            number="ENGR 211",
            name="Engineering Statics",
            credits=4.0,
            college=college1,
            pre_reqs="ENGR 101",
            description="An engineering statics course",
            course_outcomes="test outcomes",
            URL="https://www.pcc.edu/ccog/engr/211/",
            added_by=self.user,
        )
        Course.objects.create(
            number="ENGR 211",
            name="Statics",
            credits=4.0,
            college=college2,
            pre_reqs="MTH 251",
            description="A course on engineering statics",
            course_outcomes="test outcomes",
            URL="https://www.pcc.edu/ccog/engr/211/",
            added_by=self.user,
        )
        course1 = Course.objects.get(id=1)
        course2 = Course.objects.get(id=2)
        Articulation.objects.create(
            course1 = course1,
            course2 = course2,
            URL = "https://pcc.edu/engineering",
            description = "Mt Hood class transfers to PSU",
        )
    def test_text_content(self):
        articulation = Articulation.objects.get(id=1)
        expected_object_name = f"{articulation.course1.number} at {articulation.course1.college.abbreviation} --> {articulation.course2.number} at {articulation.course2.college.abbreviation}"
        self.assertEquals(
            expected_object_name,
            "ENGR 211 at MHCC --> ENGR 211 at PSU",
        )

    def test_articulation_list_view(self):
        response = self.client.get(reverse("articulation_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 211")
        self.assertTemplateUsed(response, "articulation_list.html")

    def test_articulation_detail_view(self):
        articulation = Articulation.objects.get(id=1)
        response = self.client.get(reverse("articulation_detail", args=[str(articulation.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ENGR 211")
        self.assertTemplateUsed(response, "articulation_detail.html")
