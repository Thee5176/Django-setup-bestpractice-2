from django.test import TestCase
from django.urls import reverse

from .models import Post
class PostTests(TestCase):
    """Model test"""
    @classmethod
    def setUpTestData(cls):
        """Store in class instance"""
        cls.post = Post.objects.create(text="This is a test.")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test.")

class HomePageViewTest(TestCase):
    def test_url_exist_at_correct_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Message board homepage")
    
    