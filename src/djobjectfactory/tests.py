from django.test import TestCase
from djobjectfactory import get_factory


class BaseTestCase(TestCase):
    def setUp(self):
        self.factory = get_factory('auth.User')


class TestCreate(BaseTestCase):
    def test_create(self):
        obj = self.factory.create()
        self.assert_(obj.id)
        self.assertEquals(self.factory.get_model().objects.count(), 1)

    def test_create_two(self):
        obj = self.factory.create()
        self.assertEquals(self.factory.get_model().objects.count(), 1)
        obj = self.factory.create()
        self.assertEquals(self.factory.get_model().objects.count(), 2)

    def test_create_with_custom_data(self):
        obj = self.factory.create(username='just a test')
        self.assertEquals(obj.username, 'just a test')


class TestGetOrCreate(BaseTestCase):
    def test_get_or_create(self):
        obj1 = self.factory.get_or_create(username='user1')
        self.assertEquals(self.factory.get_model().objects.count(), 1)
        obj2 = self.factory.get_or_create(username='user1')
        self.assertEquals(obj1, obj2)
        self.assertEquals(self.factory.get_model().objects.count(), 1)
