from rest_framework import serializers


def create_user_relative_serializer_class(
    model_cls, include_fields=None, exclude_fields=None
):
    class UserRelativeSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_cls
            fields = include_fields
            exclude = exclude_fields

    return UserRelativeSerializer
