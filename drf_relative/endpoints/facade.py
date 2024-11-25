from typing import Callable
from rest_framework import decorators

from ._data import UserRelativeData
from ._serializer import create_user_relative_serializer_class
from ._viewset import create_user_relative_viewset_class
from ._router import create_user_relative_router_class


class UserRelativeEndpointsFacade:
    """
    Provides simple implementation of components for endpoints:
    `ModelSerializer`, `ModelViewSet`, `SimpleRouter`.

    Works only with models that have one-to-one relation to `User`.

    Use `.add_action()` to implement custom viewset's actions.
    """

    def __init__(self, model_related_name):
        self.data = UserRelativeData(model_related_name)
        self.fields = None
        self.exclude_fields = None
        self._actions = {}

    def add_action(self, name, method: Callable, **decorator_kwargs):
        result = decorators.action(**decorator_kwargs)(method)
        self._actions[name] = result

    def get_urls(self, prefix, basename):
        serializer_class = create_user_relative_serializer_class(
            self.data.model,
            include_fields=self.fields,
            exclude_fields=self.exclude_fields,
        )
        viewset_class = create_user_relative_viewset_class(
            self.data, serializer_class, **self._actions
        )
        router_class = create_user_relative_router_class()

        router = router_class()
        router.register(prefix, viewset_class, basename)
        return router.urls
