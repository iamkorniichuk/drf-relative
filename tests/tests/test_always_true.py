from django.test import TestCase


class AlwaysTrueTestCase(TestCase):
    fixtures = ["users", "profiles", "posts"]

    def test_always_true(self):
        return self.assertTrue(True)
