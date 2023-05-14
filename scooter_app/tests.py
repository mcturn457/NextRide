from django.test import TestCase
from scooter_app.models import Company, Charging_station, Scooter

# Create your tests here.
class ScooterTestCase(TestCase):
    def setUp(self) -> None:
        
        return super().setUp()

    def test_scooter_lat(self):
        scooter = Scooter.objects.get(scooter_id__exact=174280)

        test_lat = scooter.latitude

        self.assertEqual(test_lat, 51.7313608382461)

    def test_scooter_lng(self):
        scooter = Scooter.objects.get(scooter_id__exact=174280)

        test_lng = scooter.longitude

        self.assertEqual(test_lng, 6.625807285308839)

