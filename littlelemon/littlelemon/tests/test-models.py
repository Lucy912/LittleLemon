from django.test import TestCase
from restaurant.models import Menu

# Testcase class for Menu Model
class MenuItemTest(TestCase):
    def test_get_item(self):
        # Create a MenuItem instance
        item = Menu.objects.create(title="IceCreamBoat", price=80, inventory = 100)

        # Check the string representation
        self.assertEqual(str(item),"IceCreamBoat : 80")