# DRF Relative

Fast ways to handle model relations for CRUD.

# Install

```sh
pip install drf-relative
```

# Use

## Override request's data

Your model need to have consistent field's data.
For example, field `user` of `Post` model have to refer to a user that changes/creates it:

```py
from drf_relative.views import OverrideDataMixin

class PostViewset(OverrideDataMixin, viewsets.ModelViewSet)
    queryset = Post.objects.all()
    ...
    def get_overriding_data(self):
        return {"user": self.request.user.pk}
```
