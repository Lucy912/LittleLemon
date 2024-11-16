from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient

# TestCase class for Menu View
class MenuViewTest(TestCase):
    def setUp(self):
        # add test data
        self.client = APIClient()
        self.item1 = Menu.objects.create(title = "Pizza", price = 120, inventory = 50)
        self.item2 = Menu.objects.create(title = "Burger", price = 50, inventory = 100)

    def test_getall(self):
        # get all menu items using the API endpoint
        response = self.client.get(reverse('menu-list'))

        # Serialize the expected data
        serialized_data = MenuSerializer([self.item1, self.item2], many= True).data

        # Assert the API response matches the serialized data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_data)