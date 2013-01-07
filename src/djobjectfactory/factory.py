from django.conf import settings
from django.db.models import get_model


__all__ = ['get_factory', 'ObjectFactory']
REGISTRY = {}


def get_factory(model):
    return REGISTRY.get(model, ObjectFactory(model))


class ObjectFactory(object):
    _counter = 0
    default_values = {}

    @classmethod
    def __init__(cls, model):
        cls.model = model

    @classmethod
    def create(cls, *args, **kwargs):
        cls._counter += 1
        values = cls.default_values.copy()
        values.update(kwargs)
        values.update(cls.default(cls._counter))
        model = cls.get_model()
        return model.objects.create(**values)

    @classmethod
    def default(cls, counter):
        return {}

    @classmethod
    def get_model(cls):
        return get_model(*cls.model.split('.'))


# Go through the installed apps and import their test helpers to register the
# object factories.
for app in getattr(settings, 'INSTALLED_APPS', []):
    app = app + '.tests'
    try:
        __import__(app + '.helpers', fromlist=app)
    except ImportError:
        pass


# Now all subclasses for ObjectFactory have been introduced.
for cls in ObjectFactory.__subclasses__():
    REGISTRY[cls.model] = cls
