Example: create a factory for auth.User:

# myapp/tests/helpers.py (remember to add myapp to INSTALLED APPS)

```python
from django.contrib.auth.models import User
from djobjectfactory.factory import ObjectFactory


class UserFactory(ObjectFactory):
    model = 'auth.User'
    @classmethod
    def default(cls, counter):
        return {'username': 'user%d' % counter}

```


In myapp tests:

```python
Class TestUserResource(TestCase):
    def setUp(self):
        self.user = get_factory('auth.User').create()

```
