from django.test import TestCase
from rest_framework import status
import json

from .data import TestData


class IsRelatedToUserOrReadOnlyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_data = TestData()
        return super().setUpTestData()

    def test_on_related_user(self):
        user = self.test_data.users[1]
        urls = self.test_data.likes_detail_urls[1]

        read, delete = self._test_on_user(user, urls[0])

        self.assertTrue(status.is_success(read.status_code))
        self.assertTrue(status.is_success(delete.status_code))

    def test_on_unrelated_user(self):
        user = self.test_data.users[2]
        urls = self.test_data.likes_detail_urls[1]

        read, delete = self._test_on_user(user, urls[0])

        self.assertTrue(status.is_success(read.status_code))
        self.assertTrue(status.is_client_error(delete.status_code))

    def _test_on_user(self, user, url):
        self.client.force_login(user)

        read_response = self.client.get(url)
        delete_response = self.client.delete(url)

        return read_response, delete_response
