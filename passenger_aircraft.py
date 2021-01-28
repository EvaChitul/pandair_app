

class PassengerAircraft(Aircraft):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers):
        self.number_passengers = number_passengers
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance)