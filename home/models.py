from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


"""User profile model which extends the user account model to add premium member status"""
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    email = models.CharField(max_length=255, null=True)
    premium_member = models.BooleanField()

    def __str__(self) -> str:
        return self.email
