


def operate_flight(fleet_data, city, destination, aircraft):

    if aircraft in fleet_data[city.title()]:

        fleet_data[city.title()].remove_aircraft(aircraft)
        log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} removed from {city.title()} airport. {city.title()} airport overview: {fleet_data[city.title()]}')

        fleet_data[destination.title()].add_aircraft(aircraft)
        log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} added to {destination} airport. {destination.title()} airport overview: {fleet_data[destination.title()]}')

        aircraft.number_flights_maintenance += 1
        log.debug(f'{time.asctime(time.localtime(time.time()))} {aircraft} number of flights increased by 1. Number of flights operated now at {aircraft.number_flights_maintenance}')

    else:
        print(f'{aircraft} not in {city}. Cannot perform flight ')
        log.info(f' {aircraft} not found in {city} airport.')
        return None

    return aircraft, city, destination