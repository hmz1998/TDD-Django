from django.test import TestCase
from http import HTTPStatus

from .models import (
    Post,
)


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = Post.objects.create(
            title="Test title", description="Test content description."
        )

        self.assertEqual(str(post), post.title)


class HomePageTests(TestCase):
    def setUp(self) -> None:
        post1 = Post.objects.create(
            title="psample test 1",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        )

        post2 = Post.objects.create(
            title="psample test 2",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_posts_list(self):
        response = self.client.get("/")
        
        self.assertContains(response, "psample test 1")
        self.assertContains(response, "psample test 2")


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
        title = "Learn python in this 40 hours",
        description = "this is a begginner course on pytho`n programming."
        )
    
    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html')
        
    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)
        self.assertContains(response, self.post.created_at)