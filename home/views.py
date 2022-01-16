from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from home.models import Profile
from home.context_processor import is_premium_member

# Create your views here.


def index(request):
    """A view to return the index page"""
    if str(request.user) == "AnonymousUser":
        return render(request, "home/index.html")

    request = is_premium_member(request)

    return render(request, "home/index.html")


def logout(request):

    request = is_premium_member(request)

    return render(request, "home/logout.html")
