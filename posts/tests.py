from django.test import TestCase


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()

        self.assertEqual(posts, [])