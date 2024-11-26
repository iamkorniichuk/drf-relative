from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)
from drf_relative.views import OverrideDataMixin
from drf_relative.permissions import IsRelatedToUserOrReadOnly

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


class PostViewSet(OverrideDataMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_overriding_data(self):
        user = self.request.user.pk
        if self.action == "create":
            return {"created_by": user}
        elif self.action == "update":
            return {"updated_by": user}


class LikeViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        return super().get_permissions() + [IsRelatedToUserOrReadOnly("user")]
