
import unittest


class Tire:
    def needs_service(self, wear_values):
        raise NotImplementedError('The method needs_service should be implemented by subclasses.')

class CarriganTire(Tire):
    def needs_service(self, wear_values):
        return any(wear >= 0.9 for wear in wear_values)

class OctoprimeTire(Tire):
    def needs_service(self, wear_values):
        return sum(wear_values) >= 3.0


class TestTire(unittest.TestCase):

    def test_carrigan_tire_service(self):
        # Tire with all values less than 0.9 shouldn't need service
        tire = CarriganTire()
        self.assertFalse(tire.needs_service([0.2, 0.3, 0.1, 0.8]))

        # Tire with one or more values greater than or equal to 0.9 should need service
        self.assertTrue(tire.needs_service([0.2, 0.3, 0.1, 0.9]))

    def test_octoprime_tire_service(self):
        # Tire with sum of values less than 3 shouldn't need service
        tire = OctoprimeTire()
        self.assertFalse(tire.needs_service([0.5, 0.6, 0.7, 0.5]))

        # Tire with sum of values greater than or equal to 3 should need service
        self.assertTrue(tire.needs_service([0.8, 0.8, 0.7, 0.8]))
