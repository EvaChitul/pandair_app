

class Aircraft:

    def __init__(self, manufacturer, weight, speed, consumption, identifier, number_flights_maintenance):
        self.manufacturer = manufacturer
        self.weight = weight
        self.speed = speed
        self.consumption = consumption
        self.identifier = identifier
        self.number_flights_maintenance = number_flights_maintenance

    def __str__(self):
        return f'Aircraft type {type(self).__name__}, identifier {self.identifier}, manufacturer {self.manufacturer}'

    def __repr__(self):
        return self.identifier

    def due_for_maintenance(self):

        log.info(f' Checking if Aircraft {self.identifier} is due for maintenance')
        if self.number_flights_maintenance >= 30:
            return True
        else:
            return False