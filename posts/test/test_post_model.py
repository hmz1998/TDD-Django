from django.test import TestCase

from model_bakery import baker

from posts.models import Post


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = baker.make(Post)

        self.assertEqual(str(post), post.title)
        self.assertTrue(isinstance(post, Post))
