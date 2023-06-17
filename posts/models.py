from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .common import (
    TimeStampModelMixin,
    TitleSlugLinkModelMixin,
)


class Post(TimeStampModelMixin, TitleSlugLinkModelMixin):
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ("-created_at",)
