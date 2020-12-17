

class AlterAircraft:

    def __init__(self, plane):
        self.plane = plane

    def __enter__(self):
        self.pandair_status = open('pandair_status.txt', 'w')
        self.pandair_status.write('Altering behaviour of due for maintenance method. Be careful with the flights! \n')

        self.original_maintenance_method = self.plane.due_for_maintenance
        self.plane.due_for_maintenance = lambda: False

        log.info(f'Behaviour of {self.plane} has been changed')
        log.debug(f'{time.asctime(time.localtime(time.time()))} Due for maintenance method for {self.plane} now returning {self.plane.due_for_maintenance}')

        return self.plane

    def __exit__(self, exc_type, exc_value, traceback):
        self.pandair_status.write(f'Due for maintenance method of aircraft returned to original state\n')
        self.pandair_status.write('Closing down Pandair App. Travel safe!\n')

        self.plane.due_for_maintenance = self.original_maintenance_method

        log.info(f'Behaviour of {self.plane} has returned to original')
        log.debug(f'{time.asctime(time.localtime(time.time()))} Due for maintenance method for {self.plane} now back to original form')
