from django.db import models

# Create your models here.


# Booking Model
class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # ID (int(11), Primary Key)
    name = models.CharField(max_length=255)  # Name (varchar(255))
    no_of_guests = models.IntegerField()  # No_of_guests (int(6))
    booking_date = models.DateTimeField()  # BookingDate (datetime)

    def __str__(self):
        return f"{self.name} - {self.booking_date}"


# Menu Model
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # ID (int(5), Primary Key)
    title = models.CharField(max_length=255)  # Title (varchar(255))
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price (decimal(10,2))
    inventory = models.IntegerField()  # Inventory (int(5))

    def __str__(self):
        return f'{self.title} : {str(self.price)}'