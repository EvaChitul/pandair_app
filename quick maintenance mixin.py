

class QuickMaintenanceMixin:

    def quick_maintenance(self):

        if self.number_flights_maintenance - 10 < 0:
            self.number_flights_maintenance = 0
        else:
            self.number_flights_maintenance -= 10

        log.debug(f'{time.asctime(time.localtime(time.time()))} {self} completed quick maintenance. Flights number is now {self.number_flights_maintenance}')
        return f'{self} has gone through quick maintenance. Flights number is now: {self.number_flights_maintenance}'