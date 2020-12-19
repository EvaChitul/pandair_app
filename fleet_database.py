

class FleetDatabase:

    def __init__(self):
        self.fleet = {}

    def __getitem__(self, key):
        if key not in self.fleet:
            print(f'Airport {key} not in Fleet Database. Airport will be added')
            log.info(f' Airport {key} not in Fleet Database.')
            self.fleet[key] = Airport()
            log.debug(f'{time.asctime(time.localtime(time.time()))} Airport {key} not found. Airport was added to Fleet Database. Fleet Overview: {self.fleet}')
        return self.fleet[key]

    def __delitem__(self, key):
        del self.fleet[key]

    def __setitem__(self, key, value):
        self.fleet[key] = value

    def __len__(self):
        return len(self.fleet)

    def __iter__(self):
        return iter(self.fleet)

    def __str__(self):
        return f'Fleet and Location Overview: {self.fleet}'

    def __repr__(self):
        return f'{self.fleet}'

    def add_airport(self, airport_name, airport_list):
        if airport_name.title() in self.fleet.keys():
            print('Airport already in Fleet Database. The new aircrafts will replace the old ones')
            log.info(f' {airport_name.title()} already in Fleet Database.')
            for aircraft in self.fleet[airport_name.title()]:
                fleet_database_check.remove(aircraft)
                log.debug(f'{time.asctime(time.localtime(time.time()))} {airport_name} removed from Fleet Database. Fleet Overview {fleet_database_check}')

        for new_aircraft in airport_list:
            fleet_database_check.add(new_aircraft)
            log.debug(f'{time.asctime(time.localtime(time.time()))} {new_aircraft} added to Fleet Database. Fleet Overview {fleet_database_check}')

        self.fleet[airport_name.title()] = airport_list
        log.debug(f'{time.asctime(time.localtime(time.time()))} {airport_name.title()} fleet replaced. New {airport_name.title()} {airport_list} ')

    def remove_airport(self, airport_name):
        if airport_name.title() in self.fleet.keys():
            for aircraft in self.fleet[airport_name.title()]:
                fleet_database_check.remove(aircraft)
                log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} removed from Fleet Database. Fleet overview {fleet_database_check}')
            del self.fleet[airport_name.title()]
            log.debug(f'{time.asctime(time.localtime(time.time()))} {airport_name.title()} removed from Fleet Database. Overview of airports {self.fleet}')
        else:
            print(f'{airport_name.title()} Airport not found in Fleet Database. Unable to remove')
            log.info(f' {airport_name.title()} not found in Fleet. ')