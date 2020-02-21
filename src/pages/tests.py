from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory, APITestCase, override_settings
from unittest.mock import patch

from .faker import fake
from .models import Page, VideoContent, AudioContent, TextContent
from .serializers import PageSerializer, PageDetailSerializer


INVALID_PAGE_ID = 123456789


class HyperlinkedContextMixin(object):
    def setUp(self):
        super().setUp()
        self.factory = APIRequestFactory()

    def get_context(self, url='/'):
        request = self.factory.get(url)
        return {'request': Request(request)}


class GetAllPagesTest(
    HyperlinkedContextMixin,
    APITestCase
):
    def setUp(self):
        super().setUp()
        for i in range(5):
            fake.model(Page).save()

    def test_get_all_pages(self):
        url = reverse('page-list')
        response = self.client.get(url)

        pages = Page.objects.all()
        context = self.get_context(url=url)
        serializer = PageSerializer(pages, many=True, context=context)

        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetPageTest(
    HyperlinkedContextMixin,
    APITestCase
):
    def setUp(self):
        super().setUp()
        self.page = fake.model(Page)
        self.page.save()
        fake.model(AudioContent, page=self.page).save()
        fake.model(VideoContent, page=self.page).save()
        fake.model(TextContent, page=self.page).save()

    @override_settings(CELERY_ALWAYS_EAGER=True)
    @patch('pages.tasks.increase_page_counters')
    def test_get_valid_single_page(self, mock_increase_page_counters):
        url = reverse('page-detail', kwargs={'pk': self.page.pk})
        response = self.client.get(url)

        page = Page.objects.get(pk=self.page.pk)
        context = self.get_context(url=url)
        serializer = PageDetailSerializer(page, context=context)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_page(self):
        response = self.client.get(reverse('page-detail', kwargs={'pk': INVALID_PAGE_ID}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
