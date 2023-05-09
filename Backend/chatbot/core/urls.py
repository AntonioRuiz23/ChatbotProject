from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),


]
"""
    path('login/', views.login, name="login"),
    path('register/', views.Register, name="register"),
    """
