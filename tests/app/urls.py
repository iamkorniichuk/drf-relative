from rest_framework import routers

from .viewsets import PostViewSet
from .endpoints import profile_endpoints


app_name = "app"


router = routers.SimpleRouter()
router.register("posts", PostViewSet, "post")
urlpatterns = profile_endpoints.get_urls("profile", "profile") + router.urls
