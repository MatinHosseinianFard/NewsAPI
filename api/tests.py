from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import New, Tag
from api.serializers import NewsSerializer


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='test tag')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_str_method(self):
        tag = Tag.objects.get(id=1)
        self.assertEqual(str(tag), 'test tag')


class NewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        tag = Tag.objects.create(name='test tag')
        New.objects.create(title='test title', body='test body', source='test source')
        New.objects.get(id=1).tags.add(tag)

    def test_title_label(self):
        new = New.objects.get(id=1)
        field_label = new._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        new = New.objects.get(id=1)
        max_length = new._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_body_label(self):
        new = New.objects.get(id=1)
        field_label = new._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'body')

    def test_tags_label(self):
        new = New.objects.get(id=1)
        field_label = new._meta.get_field('tags').verbose_name
        self.assertEqual(field_label, 'tags')

    def test_source_label(self):
        new = New.objects.get(id=1)
        field_label = new._meta.get_field('source').verbose_name
        self.assertEqual(field_label, 'source')

    def test_source_max_length(self):
        new = New.objects.get(id=1)
        max_length = new._meta.get_field('source').max_length
        self.assertEqual(max_length, 255)

    def test_str_method(self):
        new = New.objects.get(id=1)
        self.assertEqual(str(new), 'test title')


class NewsAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag1 = Tag.objects.create(name='test tag 1')
        self.tag2 = Tag.objects.create(name='test tag 2')
        self.new1 = New.objects.create(title='test title 1', body='test body 1', source='test source 1')
        self.new1.tags.add(self.tag1)
        self.new2 = New.objects.create(title='test title 2', body='test body 2', source='test source 2')
        self.new2.tags.add(self.tag2)

    def test_get_all_news(self):
        response = self.client.get(reverse('news-list'))
        news = New.objects.all()
        serializer = NewsSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_news_by_tag(self):
        response = self.client.get(reverse('news-list') + '?tags__name=test tag 1')
        news = New.objects.filter(tags__name='test tag 1')
        serializer = NewsSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_news_by_nonexistent_tag(self):
        response = self.client.get(reverse('news-list') + '?tags__name=nonexistent tag')
        self.assertEqual(response.data, [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

