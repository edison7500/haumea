from django.test import TestCase, Client
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from store.models import Entry
from store.tests.shop import ShopFaker

from faker import Faker
import factory

faker = Faker()


class EntryFacker(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry
        django_get_or_create = ('name', 'shop', 'url')

    name = faker.name()
    shop = factory.SubFactory(ShopFaker)
    url = faker.url()


class EntryModelTestCase(TestCase):

    def setUp(self):
        self.entry = EntryFacker()

    def test_model_can_create_a_entry(self):
        old_count = Entry.objects.count()
        EntryFacker.create(name=faker.name(), url=faker.url())
        new_count = Entry.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_update_a_entru(self):
        entry = Entry.objects.get()
        old_name = entry.name
        entry.name = faker.name()
        entry.save()
        self.assertNotEqual(old_name, entry.name)

    def test_model_can_delete_a_entry(self):
        entry = Entry.objects.get()
        entry.delete()
        self.assertIsNone(entry.pk)


class EntryAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.entry = EntryFacker()

    def test_api_can_create_entry(self):

        entry_data = {
            'name': faker.name(),
            'url': faker.url(),
            'shop': self.entry.shop.id,
        }
        res = self.client.post(
            reverse('entry-list-create'),
            data=entry_data,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_entry_list(self):
        res = self.client.get(
            reverse('entry-list-create'),
            # kwargs={'pk', self.entry.pk},
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.entry)

    def test_api_can_get_entry(self):
        res = self.client.get(
            reverse('entry-detail', kwargs={'pk': self.entry.id}),
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_update_entry(self):
        change_entry = {
            'name': faker.name(),
            'url': faker.url(),
        }
        res = self.client.patch(
            reverse('entry-detail', kwargs={'pk': self.entry.id}),
            change_entry,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_entry(self):
        res = self.client.delete(
            reverse('entry-detail', kwargs={'pk': self.entry.id}),
            format='json',
            follow=True,
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)