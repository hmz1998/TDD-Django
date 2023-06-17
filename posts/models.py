from django.db import models
from .common import (
    TimeStampModelMixin,
    TitleSlugLinkModelMixin,
)

class Post(TimeStampModelMixin, TitleSlugLinkModelMixin):
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
    )
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ('-created_at', )
    