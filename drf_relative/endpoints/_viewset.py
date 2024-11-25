from rest_framework import mixins, viewsets
from drf_relative.views import OverrideDataMixin


def create_user_relative_viewset_class(user_data, serializer_cls, **actions):
    class UserRelativeViewset(
        OverrideDataMixin,
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet,
    ):
        data = user_data
        serializer_class = serializer_cls

        @property
        def user(self):
            return self.request.user

        def get_object(self):
            instance = self.data.get_instance(self.user)
            return instance

        def get_queryset(self):
            queryset = self.data.get_queryset(self.user)
            return queryset

        def get_populated_data(self):
            data = {self.data.user_field_name: self.user}
            return data

    for name, func in actions.items():
        setattr(UserRelativeViewset, name, func)

    return UserRelativeViewset
