from Serviceable import Serviceable
from Engine import Engine
from Battery import Battery

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
        
    def needs_service(self) -> bool:
        """Determine if the car needs service."""
        return self.engine.needs_service() or self.battery.needs_service()
