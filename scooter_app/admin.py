from django.contrib import admin
from .models import Scooter, Company, Charging_station, User

# Register your models here.
admin.site.register(Scooter)
admin.site.register(Company)
admin.site.register(Charging_station)
admin.site.register(User)