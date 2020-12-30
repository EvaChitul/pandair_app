

def generate_pairs(fleet_database):

    list_origin = set([origin for origin, fleet in fleet_database.fleet.items() for aircraft in fleet
                   if isinstance(aircraft, PassengerAircraft) and aircraft.number_passengers > 100])

    list_destination = set([destination for destination, planes in fleet_database.fleet.items() if len(planes) <= 3])

    print(list_origin)
    print(list_destination)

    for origin, destination in itertools.product(list_origin, list_destination):
        if origin != destination:
            log.debug(f'{time.asctime(time.localtime(time.time()))} New origin-destination pair was generated: {origin} - {destination}')
            yield f'Possible origin destination pair: {origin} - {destination}'