from django.shortcuts import get_object_or_404
from home.models import Profile

""" Function to check if user is a premium member """
def is_premium_member(request):
    if str(request.user) != 'AnonymousUser':
        profile = get_object_or_404(Profile, email=request.user.email)
        if profile.premium_member:
            request.META["premium_member"] = True
        else:
            request.META["premium_member"] = False
    else:
        request.META["premium_member"] = False
    return request