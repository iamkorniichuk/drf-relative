from rest_framework import routers

from .app.viewsets import PostViewSet, LikeViewSet
from .app.endpoints import profile_endpoints


router = routers.SimpleRouter()
router.register("posts", PostViewSet, "post")
router.register("likes", LikeViewSet, "like")
urlpatterns = profile_endpoints.get_urls("profile", "profile") + router.urls
