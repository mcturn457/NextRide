from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Scooter(models.Model):
    created_at = models.DateField(default=date.today)
    scooter_id = models.IntegerField()
    user_id = models.IntegerField(default=0)
    company_id = models.IntegerField()
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=-1)
    longitude = models.FloatField(default=-1)
    state_of_charge = models.IntegerField(default=100)
    current_earnings = models.DecimalField(default=0.0, max_digits=10, decimal_places=10)
    driven_distance = models.DecimalField(default=0.0, max_digits=10, decimal_places=10)
    current_ride_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Company(models.Model):
    created_at = models.DateField(default=date.today)
    company_id = models.IntegerField()
    name = models.CharField(max_length=200)
    cost_per_kilometer = models.DecimalField(default=0.0, max_digits=10, decimal_places=10)
    income = models.DecimalField(default=0.0, max_digits=10, decimal_places=10)
    street = models.CharField(max_length=200)
    postalcode = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Charging_station(models.Model):
    created_at = models.DateField(default=date.today)
    station_id = models.IntegerField()
    company_id = models.IntegerField()
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=-1)
    longitude = models.FloatField(default=-1)
    capacity = models.IntegerField()
    used_loading_places = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=date.today)
    company_id = models.IntegerField()
    mode = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postalcode = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id
