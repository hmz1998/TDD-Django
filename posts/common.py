from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class TimeStampModelMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name="Modified At",
        auto_now=True
    )

    class Meta:
        abstract = True


class TitleSlugLinkModelMixin(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=150,
        validators=[
            MaxLengthValidator(150),
            MinLengthValidator(3)
        ],
        unique=True
    )
    slug = models.SlugField(
        verbose_name="Slug",
        editable=False,
        allow_unicode=True,
        max_length=150,
        unique=True
    )

    class Meta:
        abstract = True
