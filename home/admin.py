from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "premium_member",
    )

admin.site.register(Profile, ProfileAdmin)
