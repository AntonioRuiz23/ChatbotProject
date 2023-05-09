from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.


class HomePageView(TemplateView):
    template_name = "core/home.html"

    """
    def login(request):
    return render(request, "core/login.html")


def register(request):
    return render(request, "core/register.html")
    
    """
