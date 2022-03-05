from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from home.models import Profile
from home.context_processor import is_premium_member


def index(request):
    """A view to return the index page"""
    if request.user.is_anonymous:
        return render(request, "home/index.html")

    context = {
        "is_premium_member": is_premium_member(request),
    }

    return render(request, "home/index.html", context)


def logout(request):

    context = {
        "is_premium_member": is_premium_member(request),
    }

    return render(request, "home/logout.html", context)
