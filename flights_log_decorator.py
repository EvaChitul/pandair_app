

def flights_log(flight):

    def track_flight(*args):
        results = flight(*args)
        if results:
            aircraft, city, destination = results[0], results[1], results[2]

            flights_log_database[f'Entry {len(flights_log_database) + 1}'] = f' Aircraft {aircraft.identifier}: {city} to {destination}'
            log.info(f' New flight added to flight log: {aircraft.identifier}: {city} to {destination}')

            if aircraft.due_for_maintenance:
                print(f'Alert: Aircraft {aircraft.identifier} is due for maintenance!')
                log.info(f' Aircraft Alert: {aircraft.identifier} is due for maintenance!')
        else:
            return None

        return flight
    return track_flight


@flights_log