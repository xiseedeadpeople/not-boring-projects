from sqlalchemy.orm import Session
from models.models import Flight

# В сервисе рейсов добавим метод для удаления
class FlightService:
    def __init__(self, db: Session):
        self.db = db

    def add_flight(self, from_city: str, to_city: str, date, time, price: float):
        new_flight = Flight(
            from_city=from_city,
            to_city=to_city,
            date=date,
            time=time,
            price=price
        )
        try:
            self.db.add(new_flight)
            self.db.commit()
            self.db.refresh(new_flight)
            return new_flight
        except Exception as e:
            self.db.rollback()
            print(f"Ошибка добавления рейса: {e}")
            return None

    def get_all_flights(self):
        return self.db.query(Flight).all()

    def delete_flight(self, flight_id: int):
        flight = self.db.query(Flight).filter(Flight.id == flight_id).first()
        if flight:
            self.db.delete(flight)
            self.db.commit()
