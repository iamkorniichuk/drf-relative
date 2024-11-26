from django.http import HttpResponse
from drf_relative.endpoints import UserRelativeEndpointsFacade


def promote(self, request, *args, **kwargs):
    profile = self.get_object()
    profile.is_promoted = True
    profile.save()
    return HttpResponse("Successful operation.", content_type="text/plain")


profile_endpoints = UserRelativeEndpointsFacade("profile")
profile_endpoints.fields = "__all__"
profile_endpoints.add_action("promote", promote, detail=True, methods=["post"])
