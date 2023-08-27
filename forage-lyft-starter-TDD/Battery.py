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
