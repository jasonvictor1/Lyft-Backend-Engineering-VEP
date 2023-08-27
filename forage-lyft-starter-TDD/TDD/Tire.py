
class Tire:
    def needs_service(self, wear_values):
        raise NotImplementedError('The method needs_service should be implemented by subclasses.')

class CarriganTire(Tire):
    def needs_service(self, wear_values):
        return any(wear >= 0.9 for wear in wear_values)

class OctoprimeTire(Tire):
    def needs_service(self, wear_values):
        return sum(wear_values) >= 3.0
