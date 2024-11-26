from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=16)
    description = models.TextField(max_length=64)
    created_by = models.ForeignKey(User, models.CASCADE, related_name="created_posts")
    updated_by = models.ForeignKey(
        User,
        models.CASCADE,
        related_name="updated_posts",
        null=True,
        blank=True,
    )


class Like(models.Model):
    class Meta:
        default_related_name = "likes"

    user = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(Post, models.CASCADE)


class Profile(models.Model):
    class Meta:
        default_related_name = "profile"

    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    birth_date = models.DateField(null=True, blank=True)
    is_promoted = models.BooleanField(default=True)
    user = models.OneToOneField(User, models.CASCADE)
