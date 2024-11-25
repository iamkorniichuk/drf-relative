from django.contrib.auth import get_user_model


User = get_user_model()


class UserRelativeData:
    def __init__(self, model_related_name):
        self.model_related_name = model_related_name

        field = User._meta.get_field(self.model_related_name).field
        self.model = field.model
        self.user_field_name = field.name

    def get_instance(self, user):
        instance = getattr(user, self.model_related_name)
        return instance

    def get_queryset(self, user):
        kwargs = {self.user_field_name: user}
        queryset = self.model.objects.filter(**kwargs).all()
        return queryset
