
import unittest
from datetime import date, timedelta
from Serviceable_real import Serviceable
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
        return delta.days > 365

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self) -> bool:
        """Determine if the NubbinBattery needs service."""
        delta = self.current_date - self.last_service_date
        return delta.days > 730


class TestBattery(unittest.TestCase):

    def setUp(self):
        self.today = date.today()
        self.one_year_ago = self.today - timedelta(days=365)
        self.two_years_ago = self.today - timedelta(days=730)

    def test_spindler_battery_service(self):
        battery = SpindlerBattery(self.one_year_ago, self.today)
        self.assertFalse(battery.needs_service())
        battery = SpindlerBattery(self.two_years_ago, self.today)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_service(self):
        battery = NubbinBattery(self.two_years_ago, self.today)
        self.assertFalse(battery.needs_service())
        battery = NubbinBattery(self.two_years_ago - timedelta(days=1), self.today)
        self.assertTrue(battery.needs_service())

