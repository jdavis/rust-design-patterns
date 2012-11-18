"""
Strategy Pattern

Definition:
    The Strategy pattern defines a family of algorithms, encapsulates each one,
    and makes them interchangeable. Strategy lets the algorithm vary
    independently from clients that use it.

Also Known As:
    Policy

Problem:
    Almost all programmers have ran into this issue before. The issue is when a
    programmer is tasked with creating a Class A that does a task. This Class A
    performs that task like expected and works quite well. However, the problem
    arises when the programmer is told that Class A isn't sufficient. Instead,
    a Class B must also be created but that task must be performed differently.
    Since Class A isn't simple, it contains many other methods and instance
    variables. Let's view the solutions below to see what can be done to solve
    this problem.

Wrong Solution:
    The wrong solution is to think that this problem should be solved using
    inheritance. It is wrong because this solution is not scalable. Whenever
    the task needs to be completed differently, Class A needs to be inherited
    to override the task. A problem can arise when Class A adds functionality
    that shouldn't exist in Class B.

Correct Solution:
    The correct solution is to implement this Strategy pattern. Rather than
    inherit Class A and override the task, the programmer will create a
    TaskBehavior that is an interface. This interface is simple and just
    performs a single task. Now the TaskBehavior interface is implemented two
    different ways, for the first task and the second task. Next, Class A is
    just given a simple instance variable to contain this new TaskBehavior.
    Whenever Class A wishes to perform this task, it instead calls the task on
    the given TaskBehavior.

Sources:
    Title: Head First Design Patterns
    Author(s): Eric Freeman & Elisabeth Freeman
    Pages: 2-24

    Title: Design Patterns
    Author(s): Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
    Pages: 315-323

Example Info:
    This examle uses my favorite activity/sport to illustrate the Strategy
    pattern. It uses Bicycles as its example classes.

    A Bicycle is an object that consists of two algorithms that have been
    encapsulated: ShiftBehavior and RideBehavior. Essentially, the idea is that
    a Bicycle has the same universal parts across all instances. Road bikes,
    mountain bikes fixies, and all others have two wheels, a saddle, a frame,
    chain, pedals, and so on. The main difference is how it performs shifting.
    So the idea of this example abstracts that out to another class.

    The second thing that it abstracts out is the riders. Bikes can be ridden
    by many people so after a Bicycle is created, the method `set_rider` will
    allow you to change who is on it.

    This example may seem strange for a few reasons. It is using some
    psuedo-interfaces, since Python doesn't have support for real interfaces.
    Instead, a base class is created that just raises an exception if that
    class were to be instantiated and a method performed on it. This is strange
    in that interfaces might seem slightly un-pythonic in some eyes.

    Despite this, the example should (hopefully) make sense. Enjoy!

"""

import sys


class Bicycle(object):
    """
    Main class that encapsulates both of our behaviors: ShiftBehavior and
    RideBehavior.

    Allows dynamic changing of riders because bikes can be swapped.

    Methods that begin with perform_ are proxy methods for a behavior.

    """

    def __init__(self, shifter):
        self.shifter = shifter
        self.rider = None

    def set_rider(self, behavior):
        self.rider = behavior
        behavior.speed = 0

    def perform_pedal(self):
        if self.rider is None:
            print 'No one is on the bike! Call set_rider first.'
            return

        self.rider.pedal()

    def perform_shift_up(self):
        if self.rider is None:
            print 'No one is on the bike! Call set_rider first.'
            return

        self.shifter.shift_up()

    def perform_shift_down(self):
        if self.rider is None:
            print 'No one is on the bike! Call set_rider first.'
            return

        self.shifter.shift_down()

#
# Behavior "Interfaces"
#


class ShiftBehavior(object):
    """
    Our base ShiftBehavior. All new shifting behaviors should inherit from this
    class.

    """

    def __init__(self):
        pass

    def shift_up(self):
        raise NotImplementedError('Shift_up method is not implemented')

    def shift_down(self):
        raise NotImplementedError('Shift_down method is not implemented')


class RideBehavior(object):
    """
    Our base RideBehavior. All new rider behaviors should inherit from this
    class.

    """

    def __init__(self):
        pass

    def pedal(self):
        raise NotImplementedError('Pedal method is not implemented')

#
# Different Shift Behaviors
#


class RoadBikeShifter(ShiftBehavior):
    """
    Inherit our base ShiftBehavior and implement some basic road bike
    mechanics.

    """

    def __init__(self):
        super(RoadBikeShifter, self).__init__()
        self.gears = 20
        self.current_gear = 1

    def shift_up(self):
        if self.current_gear >= self.gears:
            print 'Can\'t shift up anymore! Already at gear', self.gears
            return

        self.current_gear += 1

        print 'Shifted up to:', self.current_gear

    def shift_down(self):
        if self.current_gear <= 1:
            print 'Can\'t shift down anymore! Already at the lowest gear'
            return

        self.current_gear -= 1

        print 'Shifted down to:', self.current_gear


class SingleSpeedShifter(ShiftBehavior):
    """
    Inherit our base ShiftBehavior and implement some basic single speed bike
    mechanics.

    """

    def __init__(self):
        super(SingleSpeedShifter, self).__init__()
        self.gears = 1

    def shift_up(self):
        print 'This is a single speed bike!'

    def shift_down(self):
        print 'This is a single speed bike!'

#
# Different Ride Behaviors
#


class OldGeezer(RideBehavior):
    """
    Inherit our base RideBehavior and implement the pedal method at the speed
    of an old geezer on a Sunday cruise after church.

    """

    def __init__(self):
        super(OldGeezer, self).__init__()
        self.speed = 0
        self.rate = 1

    def pedal(self):
        self.speed += self.rate

        print 'Speed is now', self.speed


class BradleyWiggins(RideBehavior):
    """
    Inherit our base RideBehavior and implement the pedal method except at the
    speed of Bradley Wiggins.

    """

    def __init__(self):
        super(BradleyWiggins, self).__init__()
        self.speed = 0
        self.rate = 10

    def pedal(self):
        self.speed += self.rate

        print 'Wow, Bradley Wiggins is a beast!'
        print 'Speed is now', self.speed


def main(args):
    # Create our RideBehaviors
    geezer = OldGeezer()
    wiggo = BradleyWiggins()

    # Create the ShiftBehaviors
    single_speed_shifter = SingleSpeedShifter()
    road_bike_shifter = RoadBikeShifter()

    # Create our bikes with the shifting
    road_bike = Bicycle(road_bike_shifter)
    single_speed = Bicycle(single_speed_shifter)

    # Mount our bikes
    road_bike.set_rider(wiggo)
    single_speed.set_rider(geezer)

    # Test out our shifting
    print '\nTesting out road bike with Wiggo...'
    road_bike.perform_shift_up()
    road_bike.perform_pedal()

    print '\nTesting out single speed bike with geezer...'
    single_speed.perform_shift_up()
    single_speed.perform_pedal()

    print '\nSwapping riders...'
    single_speed.set_rider(wiggo)
    road_bike.set_rider(geezer)

    print '\nTesting road bike with geezer...'
    road_bike.perform_shift_up()
    road_bike.perform_pedal()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
