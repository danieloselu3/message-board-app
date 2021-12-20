from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class HomepageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')
    
    def test_view_url_exists_at_the_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('posts:home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('posts:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/home.html')

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text= "this is another test")

    def test_text_context(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'this is another test')