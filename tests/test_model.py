from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car, Driver


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="test",
            country="test country"
        )
        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="first_test",
            last_name="last_test",
            license_number="license number test"
        )

        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_car_str(self):
        driver = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="first_test",
            last_name="last_test",
            license_number="license number test"
        )
        manufacturer = Manufacturer.objects.create(
            name="test",
            country="test country"
        )
        car = Car.objects.create(
            model="test",
            manufacturer=manufacturer,
        )

        self.assertEqual(
            str(car),
            car.model
        )

    def test_create_driver_with_license_number(self):
        username = "test"
        password = "test1234"
        license_number = "license number test"
        first_name = "first_test"
        last_name = "last_test"

        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)
