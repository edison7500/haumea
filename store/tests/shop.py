from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from rest_framework.test import APIClient
from rest_framework import status
from store.models import Shop


from faker import Faker
import factory

faker = Faker()


class ShopFaker(factory.django.DjangoModelFactory):
    class Meta:
        model = Shop
        django_get_or_create = ('name', 'shop_url', )
    name = faker.name()
    shop_url = faker.url()


class ShopModelTestCase(TestCase):
    def setUp(self):
        self.shop_name = 'thermos'
        self.shop_url = 'https://thermos.tmall.com'
        self.shop = Shop(name=self.shop_name,
                         shop_url=self.shop_url,
                         )

    def test_model_can_create_a_shop(self):
        old_count = Shop.objects.count()
        self.shop.save()
        new_count = Shop.objects.count()
        self.assertNotEqual(old_count, new_count)


class StoreViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.shop = ShopFaker()

    def test_store_view_template(self):
        res = self.client.get(reverse('store-list-view'))
        self.assertTemplateUsed(res, template_name='store/list.html')

    def test_can_get_store(self):
        res = self.client.get(reverse('store-list-view'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class ShopAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shop = ShopFaker()

    def test_api_can_create_a_shop(self):
        self.shop_data = {'name': 'thermos',
                          'shop_url': 'https://thermos.tmall.com/view_shop.htm?shop_id=70623347'}
        response = self.client.post(
            reverse('shop-list-create'),
            self.shop_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_shop(self):
        # shop = Shop.objects.get()
        response = self.client.get(
            reverse('shop-list-create'),
            kwargs={'pk': self.shop.id, },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.shop)

    def test_api_can_update_shop(self):
        change_shop = {'name': 'thermos new'}
        res = self.client.put(
            reverse('shop-detail', kwargs={'pk': self.shop.id}),
            change_shop,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_shop(self):
        res = self.client.delete(
            reverse('shop-detail', kwargs={'pk': self.shop.id}),
            format='json',
            follow=True,
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

