from django.db.models import get_model


__all__ = ['get_factory', 'ObjectFactory']


def get_factory(model):
    from models import REGISTRY
    # Now all subclasses for ObjectFactory have been introduced.
    for cls in ObjectFactory.__subclasses__():
        REGISTRY[cls.model] = cls(cls.model)
    return REGISTRY.get(model, ObjectFactory(model))


class ObjectFactory(object):
    _counter = 0
    default_values = {}

    def __init__(self, model):
        self.model = model
        self._model = self.get_model()

    def create(self, *args, **kwargs):
        self._counter += 1
        values = self.default_values.copy()
        values.update(self.default(self._counter))
        values.update(kwargs)
        return self._model.objects.create(**values)

    def get_or_create(self, **kwargs):
        qs = self._model.objects.filter(**kwargs)
        try:
            return qs.get()
        except self._model.DoesNotExist:
            return self.create(**kwargs)

    def default(self, counter):
        return {}

    def get_model(self):
        return get_model(*self.model.split('.'))
