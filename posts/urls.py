from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="homepage"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]
