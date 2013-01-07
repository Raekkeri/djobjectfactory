from django.db.models import get_model


__all__ = ['ObjectFactory']


def get_factory(model):
    from models import REGISTRY
    # Now all subclasses for ObjectFactory have been introduced.
    for cls in ObjectFactory.__subclasses__():
        REGISTRY[cls.model] = cls
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
