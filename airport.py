

class Airport:

    def __init__(self):
        self.airport_list = []

    def __len__(self):
        return len(self.airport_list)

    def __getitem__(self, index):
        return self.airport_list[index]

    def __str__(self):
        return f'Airport: {self.airport_list}'

    def __repr__(self):
        return f'{self.airport_list}'

    def __add__(self, second_airport):
        region_airport = Airport()
        all_aircraft = self.airport_list + second_airport.airport_list
        for aircraft in all_aircraft:
            region_airport.add_aircraft(aircraft, check_duplicates=False)
        log.debug(f'{time.asctime(time.localtime(time.time()))} Created Regional Airport from {self} and {second_airport}')
        return region_airport

    def add_aircraft(self, aircraft, check_duplicates=True):

        if aircraft in fleet_database_check and check_duplicates:
            print(f'{aircraft} already in Fleet. Cannot duplicate \n')
            log.info(f' {aircraft} already in Fleet.')
        else:
            self.airport_list.append(aircraft)
            fleet_database_check.add(aircraft)
            log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} added in Airport and Fleet. Airplanes in fleet overview: {fleet_database_check}')

    def remove_aircraft(self, aircraft):
        if aircraft in self.airport_list:
            position = self.airport_list.index(aircraft)
            del self.airport_list[position]
            fleet_database_check.remove(aircraft)
            log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} removed from Airport and Fleet. Airplanes in fleet overview: {fleet_database_check}')
        else:
            print(f'{aircraft} not found at Airport. Unable to remove')
            log.info(f' {aircraft} not found at Airport.')

