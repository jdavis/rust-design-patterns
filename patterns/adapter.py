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
    Back in the 60s there were tons of Astronatus working for NASA. At the
    time, all they needed to learn was how to fly NASA's ships. When ever NASA
    came out with a new ship, it was similar to the olds ones. This worked for
    decades. All was well in the galaxy.

    However in 2010, NASA shut down the Space Shuttle program. The Astronauts
    were out of jobs and started to look for new ones. Once the Astronauts
    realized that their space suits made for poor work attire on Earth, they
    new they had to revist the stars. So they went to the next best company to
    work for, SpaceX. When they got to SpaceX they realized that technology
    had changed quite a bit since the 60s. SpaceX realized this as well, so to
    compensate for the Astronauts they came up with an idea to use the Adapter
    pattern.

    The smart SpaceX engineers made a new class that just 'Adapted' the old
    interface of the NASA Space Shuttles to SpaceX's new rocket ships. The
    Astronauts now had no problem flying SpaceX's ships through the galaxy.

    Together the Astronauts and SpaceX were able to settle the galaxy far
    and wide with SpaceX's reusable rockets.
"""


class RocketShip(object):
    def turn_on(self):
        raise NotImplementedError()

    def turn_off(self):
        raise NotImplementedError()

    def blast_off(self):
        raise NotImplementedError()

    def fly(self):
        raise NotImplementedError()


class NASAShip(RocketShip):
    def turn_on(self):
        print('NASAShip turning on')

    def turn_off(self):
        print('NASAShip turning off')

    def blast_off(self):
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

    def turn_on(self):
        self.ship.on()
        self.ship.ignition()

    def turn_off(self):
        self.ship.off()

    def blast_off(self):
        self.ship.launch()

    def fly(self):
        self.ship.fly()
