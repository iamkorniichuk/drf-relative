from django.core.management import call_command
from django.db.models import Prefetch
from django.urls import reverse

from tests.app.models import User, Profile, Post, Like


class TestData:
    __test__ = False

    def __init__(self):
        self.load_fixtures()
        self.load_models()
        self.load_urls()

    def load_fixtures(self):
        call_command("loaddata", "users.json")
        call_command("loaddata", "profiles.json")
        call_command("loaddata", "posts.json")
        call_command("loaddata", "likes.json")

    def load_models(self):
        self.users = {
            user.pk: user
            for user in User.objects.order_by("pk").prefetch_related(
                Prefetch("profile", queryset=Profile.objects.all()),
                Prefetch("created_posts", queryset=Post.objects.all()),
                Prefetch("likes", queryset=Like.objects.all()),
            )
        }
        self.profiles = {
            user_pk: user.profile
            for user_pk, user in self.users.items()
            if hasattr(user, "profile")
        }
        self.posts = {
            pk: list(user.created_posts.all()) for pk, user in self.users.items()
        }
        self.likes = {pk: list(user.likes.all()) for pk, user in self.users.items()}

    def load_urls(self):
        self.profile_detail_url = reverse("profile-detail")
        self.profile_promote_url = reverse("profile-promote")
        self.posts_list_url = reverse("post-list")
        self.posts_detail_urls = {}
        for user_pk, queryset in self.posts.items():
            self.posts_detail_urls[user_pk] = [
                reverse("post-detail", kwargs={"pk": post.pk}) for post in queryset
            ]
        self.likes_list_url = reverse("like-list")
        self.likes_detail_urls = {}
        for user_pk, queryset in self.likes.items():
            self.likes_detail_urls[user_pk] = [
                reverse("like-detail", kwargs={"pk": like.pk}) for like in queryset
            ]
