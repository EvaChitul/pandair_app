

class PrivateAircraft(PassengerAircraft, QuickMaintenanceMixin):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_passengers, number_flights_maintenance):
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance, number_passengers)