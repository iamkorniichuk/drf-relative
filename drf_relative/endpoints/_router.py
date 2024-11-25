from rest_framework import routers


def create_user_relative_router_class(extra_routes=[]):
    class UserRelativeRouter(routers.SimpleRouter):
        routes = [
            routers.Route(
                url=r"^{prefix}{trailing_slash}$",
                mapping={
                    "get": "retrieve",
                    "put": "update",
                    "patch": "partial_update",
                    "delete": "destroy",
                },
                name="{basename}-detail",
                detail=True,
                initkwargs={"suffix": "Instance"},
            ),
            routers.DynamicRoute(
                url=r"^{prefix}/{url_path}{trailing_slash}$",
                name="{basename}-{url_name}",
                detail=True,
                initkwargs={},
            ),
        ] + extra_routes

    return UserRelativeRouter
