from django.urls import path
from .views import welcome_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
]

# reporters/urls.py
from django.urls import path
from .views import welcome_view, register_view, login_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
