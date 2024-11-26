from rest_framework import viewsets
from drf_relative.views import OverrideDataMixin
from drf_relative.permissions import IsRelatedToUserOrReadOnly

from .models import Post
from .serializers import PostSerializer


class PostViewSet(OverrideDataMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        return super().get_permissions() + [IsRelatedToUserOrReadOnly("post")]
