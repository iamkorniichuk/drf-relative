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

### Differentiate request's method

If you need to override data only on create or update methods, use `views.OverrideCreateDataMixin` or `views.OverrideUpdateDataMixin` respectively.

In situations where you need more flexibility you can differentiate request's method within `.get_overriding_data()`:

```py
def get_overriding_data(self):
    user = self.request.user.pk
    if self.action == "create":
        return {"created_by": user}
    elif self.action == "update":
        return {"updated_by": user}
```
