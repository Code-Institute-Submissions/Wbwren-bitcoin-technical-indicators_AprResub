from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    email = models.CharField(max_length=255, null=True)
    premium_member = models.BooleanField()

    def __str__(self) -> str:
        return self.email