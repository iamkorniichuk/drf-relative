from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=16)
    description = models.TextField(max_length=64)
    user = models.ForeignKey(User, models.CASCADE, related_name="posts")
    created = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    class Meta:
        default_related_name = "profile"

    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    birth_date = models.DateField(null=True, blank=True)
    is_promoted = models.BooleanField(default=True)
    user = models.OneToOneField(User, models.CASCADE)
