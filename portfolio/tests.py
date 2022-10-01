from django.test import Client, TestCase
from django.urls import reverse

from portfolio.models import Project
from django.contrib.auth.models import User
from django.db import models


class BlogTestCase(TestCase):
    def setUp(self):
        Project.objects.create(title="Python1", description="hola")
        Project.objects.create(title="Python2", description="chau")

    def test_animals_can_speak(self):
        p1 = Project.objects.get(description="hola")
        p2 = Project.objects.get(description="chau")
        self.assertEqual(p1.title, 'Python1')
        self.assertEqual(p2.title, 'Python2')


class ViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('UserLogin'))
        self.assertEqual(response.status_code, 200)

    def test_no_questions2(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        

    def test_past_question(self):
        blog = Project.objects.create(title="Python1", description="chau")
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            blog.title
        )

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', '1234Qwert_')

    def testLogin(self):
        self.client.login(username='john', password='1234Qwert_')
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)