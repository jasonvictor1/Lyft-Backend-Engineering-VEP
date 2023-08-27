
import unittest
from datetime import date, timedelta

from Serviceable import Serviceable
from datetime import date

class Battery(Serviceable):
    def needs_service(self) -> bool:
        """Determine if the battery needs service."""
        raise NotImplementedError("The method needs_service should be implemented by subclasses.")

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        """Determine if the SpindlerBattery needs service."""
        delta = self.current_date - self.last_service_date
        return delta.days > 1095

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        """Determine if the NubbinBattery needs service."""
        delta = self.current_date - self.last_service_date
        return delta.days > 730


class TestSpindlerBattery(unittest.TestCase):

    def setUp(self):
        self.today = date.today()
        self.three_years_ago = self.today - timedelta(days=1095)

    def test_spindler_battery_service(self):
        # Battery serviced exactly three years ago shouldn't need service
        battery = SpindlerBattery(self.three_years_ago, self.today)
        self.assertFalse(battery.needs_service())

        # Battery serviced more than three years ago should need service
        battery = SpindlerBattery(self.three_years_ago - timedelta(days=1), self.today)
        self.assertTrue(battery.needs_service())
