from django.conf import settings

REGISTRY = {}

# Go through the installed apps and import their test helpers to register the
# object factories.
for app in getattr(settings, 'INSTALLED_APPS', []):
    app_tests = app + '.tests'
    try:
        __import__(app_tests + '.helpers', fromlist=app_tests)
    except ImportError, e:
        pass
    try:
        __import__(app_tests, fromlist=app)
    except ImportError, e:
        pass


