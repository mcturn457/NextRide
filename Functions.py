#Hauptbibliothek für alle Klassen und Funktionen
from scooter_app.models import Scooter, User, Charging_station, Company
import random
import bcrypt


# Hauptfunktionen
def create_id():
    return random.uniform(100000, 999999)


# Object Funktionen

def scooter_ausleihen():
    return

def scooter_zurückgeben():
    return

def scooter_charge(scooter_id):
    # Setze akkustand auf 100%
    return

def user_mode(user_id):
    user = User.objects.get(user__exact=user_id)
    return user.mode

def verify_pw(email, pw):

    hashed = User.objects.get(email__exact=email)
    hashed = bytes(hashed.pw, 'utf-8')

    pw = bytes(pw, 'utf-8')

    if bcrypt.checkpw(pw, hashed):
        return True
    else:
        return False


# Funktonen zum anlegen und löschen in Datenbanken
def create_scooter(name, company_id, latitude, longitude):

    Scooter.objects.create(name=name,
                           scooter_id=get_scooterID(),
                           company_id=company_id,
                           latitude=latitude,
                           longitude=longitude)


def create_chargingStation(name, company_id, latitude, longitude):

    Charging_station.objects.create(station_id=get_stationID(),
                                    company_id=company_id,
                                    name=name,
                                    latitude=latitude,
                                    longitude=longitude,
                                    capacity=0,
                                    used_loading_places=0)


def create_company():
    return

def delete_scooter(id):
    Scooter.objects.filter(scooter_id__exact=id).delete()

def delete_chargingStation(id):
    Charging_station.objects.filter(station_id__exact=id).delete()

def delete_company():
    return

def get_companyID():
    id = create_id()
    while Company.objects.filter(company_id__exact=id).exists():
        id = create_id()

    return id


def get_scooterID():
    id = create_id()
    while Scooter.objects.filter(scooter_id__exact=id).exists():
        id = create_id()

    return id


def get_stationID():
    id = create_id()
    while Charging_station.objects.filter(station_id__exact=id).exists():
        id = create_id()

    return id


def pw_generator(length):

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]()-!#_?"

    all = lower + upper + numbers + symbols

    password = "".join(random.sample(all,length))

    return password

