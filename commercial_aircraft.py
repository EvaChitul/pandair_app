

class CommercialAircraft(PassengerAircraft):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers):
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers)