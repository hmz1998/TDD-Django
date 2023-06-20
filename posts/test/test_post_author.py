from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker

from posts.models import (
    Post,
)


class PostAuthorTest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(get_user_model())
        self.post = Post.objects.create(
            title="test title",
            description="test description",
            author=self.user
        )

    def test_author_is_instance_user_model(self):
        self.assertTrue(isinstance(self.user, get_user_model()))

    def test_post_belongs_to_user(self):
        self.assertTrue(hasattr(self.post, 'author'))
        self.assertEqual(self.post.author, self.user)
