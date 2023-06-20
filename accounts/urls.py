from . import views
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.register_user, name='signup_page'),
    path('login/', views.login_page, name='login_page')
]
