
import unittest
from Serviceable_real import Serviceable
class Engine(Serviceable):
    def needs_service(self) -> bool:
        """Determine if the engine needs service."""
        raise NotImplementedError("The method needs_service should be implemented by subclasses.")
        
class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
    def needs_service(self) -> bool:
        """Determine if the CapuletEngine needs service."""
        return (self.current_mileage - self.last_service_mileage) > 5000

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on
        
    def needs_service(self) -> bool:
        """Determine if the SternmanEngine needs service."""
        return self.warning_light_on

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
    def needs_service(self) -> bool:
        """Determine if the WilloughbyEngine needs service."""
        return (self.current_mileage - self.last_service_mileage) > 7000


class TestEngine(unittest.TestCase):

    def test_capulet_engine_service(self):
        engine = CapuletEngine(1000, 4000)
        self.assertFalse(engine.needs_service())
        engine = CapuletEngine(1000, 6000)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_service(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_service(self):
        engine = WilloughbyEngine(2000, 8000)
        self.assertFalse(engine.needs_service())
        engine = WilloughbyEngine(2000, 10000)
        self.assertTrue(engine.needs_service())

