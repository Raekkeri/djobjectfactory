Add ``djobjectfactory`` to INSTALLED_APPS

Example: create a factory for auth.User:

In myapp/tests.py (remember to add ``myapp`` to INSTALLED APPS)

```python
from django.contrib.auth.models import User
from djobjectfactory.factory import ObjectFactory, get_factory


class UserFactory(ObjectFactory):
    model = 'auth.User'
    def default(cls, counter):
        return {'username': 'user%d' % counter}


Class TestUserResource(TestCase):
    def setUp(self):
        self.user = get_factory('auth.User').create()

```
