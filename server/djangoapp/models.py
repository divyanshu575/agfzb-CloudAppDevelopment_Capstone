from django.db import models
from django.utils.timezone import now

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=30, default='car make')
    description = models.CharField(max_length=1000, default='car make description')

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

class CarModel(models.Model):
    SEDAN = 'SEDAN'
    SUV = 'SUV'
    TRUCK = 'TRUCK'
    TYPE_CHOICES = (
        (SEDAN, "SEDAN"),
        (SUV, "SUV"),
        (TRUCK, "TRUCK")
    )
    dealer_id = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='car model')
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=SEDAN)
    year = models.DateField(default=now)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "DealerId: " + self.dealer_id.__str__() + "," + \
               "Type: " + self.type + "," + \
               "Year: " + self.year.__str__()

class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
    def __str__(self):
        return "Dealer name: " + self.full_name
