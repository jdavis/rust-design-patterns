"""
Adapter Pattern

Definition:
    Convert the interface of a class into another interface clients expect.
    Adapter lets classes work together that couldn't otherwise because of
    incompatible interfaces.

Also Known As:
    Wrapper

Problem:
    pass

Wrong Solution:
    pass

Correct Solution:
    pass

Sources:
    Title: Head First Design Patterns
    Author(s): Eric Freeman & Elisabeth Freeman
    Pages: 232-274

    Title: Design Patterns
    Author(s): Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
    Pages: 139-150

Example Info:
    pass

"""


class RocketShip(object):
    def turnOn(self):
        raise NotImplementedError()

    def turnOff(self):
        raise NotImplementedError()

    def blastOff(self):
        raise NotImplementedError()

    def fly(self):
        raise NotImplementedError()


class NASAShip(RocketShip):
    def turnOn(self):
        print('NASAShip turning on')

    def turnOff(self):
        print('NASAShip turning off')

    def blastOff(self):
        print('NASAShip blasting off')

    def fly(self):
        print('NASAShip flying!')


class SpaceXShip(object):
    def ignition(self):
        print('Starting SpaceXShip ignition')

    def on(self):
        print('Turning on SpaceXShip')

    def off(self):
        print('Turning off SpaceXShip')

    def launch(self):
        print('Launching SpaceXShip')

    def fly(self):
        print('SpaceXShip flying!')


class SpaceXAdapter(RocketShip):
    def __init__(self):
        self.ship = SpaceXShip()

    def turnOn(self):
        self.ship.on()
        self.ship.ignition()

    def turnOff(self):
        self.ship.off()

    def blastOff(self):
        self.ship.launch()

    def fly(self):
        self.ship.fly()
