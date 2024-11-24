class BaseOverrideDataMixin:
    def override_request_data(self, request):
        if hasattr(request.data, "_mutable") and request.data._mutable is False:
            request.data._mutable = True
        request.data.update(self.get_overriding_data())
        return request

    def get_overriding_data(self):
        raise NotImplementedError()


class OverrideCreateDataMixin(BaseOverrideDataMixin):
    """
    Overrides request's data with POST method.
    Works with `ModelViewSet` and `ApiView`.

    Implement `.get_overriding_data()` to provide the new data:
    ```
    def get_overriding_data(self):
        return {"field": "value"}
    ```
    """

    def create(self, request, *args, **kwargs):
        request = self.override_request_data(request)
        response = super().create(request, *args, **kwargs)
        return response


class OverrideUpdateDataMixin(BaseOverrideDataMixin):
    """
    Overrides request's data with PUT, PATCH methods.
    Works with `ModelViewSet` and `ApiView`.

    Implement `.get_overriding_data()` to provide the new data:
    ```
    def get_overriding_data(self):
        return {"field": "value"}
    ```
    """

    def update(self, request, *args, **kwargs):
        request = self.override_request_data(request)
        response = super().update(request, *args, **kwargs)
        return response


class OverrideDataMixin(
    OverrideCreateDataMixin,
    OverrideUpdateDataMixin,
):
    """
    Overrides request's data with POST, PUT, PATCH methods.
    Works with `ModelViewSet` and `ApiView`.

    Implement `.get_overriding_data()` to provide the new data:
    ```
    def get_overriding_data(self):
        return {"field": "value"}
    ```
    """

    pass
