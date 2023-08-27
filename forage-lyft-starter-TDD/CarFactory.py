from datetime import date
from Car import Car
from Engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = None
        return Car(engine, battery)
    
    # ... [other methods of CarFactory]
