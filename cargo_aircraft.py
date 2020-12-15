
class CargoAircraft(Aircraft, QuickMaintenanceMixin):

    def __init__(self, manufacturer, weight, speed, consumption, identifier, load_weight, number_flights_maintenance):
        self.load_weight = load_weight
        super().__init__(manufacturer, weight, speed, consumption, identifier, number_flights_maintenance)

    def due_for_maintenance(self):
        if self.number_flights_maintenance >= 50:
            return True
        else:
            return False