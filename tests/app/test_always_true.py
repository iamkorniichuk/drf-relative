from django.test import TestCase


class AlwaysTrueTestCase(TestCase):
    def test_always_true(self):
        return self.assertTrue(True)
