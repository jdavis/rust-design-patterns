"""
Observer Pattern

Definition:
    Define a one-to-many dependency between objects so that when one object
    changes state, all its dependents are notified and updated automatically.

Also Known As:
    Dependents
    Publish-Subscribe (PubSub)

Problem:
    An often encountered problem in programming is when a value in a class,
    Class A, must be updated. This is usually easy but what would happen if
    there are multiple classes that must be told about this value change?

Wrong Solution:
    There are a few wrong ways to solve this problem. One solution (more common
    in threaded applications, such as GUI applications) is to just poll the
    given value every x seconds. This is bad because it adds unneeded CPU usage.

    Another solution is to create some sort of update method on Class A as well
    as a method on any of the other classes that rely on the value. This update
    method would be called whenever the value changes. Once it is called it
    would would then call each method on the dependent class to let it know
    that the value changed. While this is closer to the solution, it would
    require modifying the update method of Class A everytime a new class relies
    on another class.

Correct Solution:
    The correct solution is to instead register each dependent class with Class
    A upon creation. Class A would then keep track of all the classes that are
    now 'registered' with it. Then once a value changes, it would then notify
    each class that has been registered. This allows an arbitrary number of
    classes to 'observe' a value and moves the registration act outside of the
    Class A.

Sources:
    Title: Head First Design Patterns
    Author(s): Eric Freeman & Elisabeth Freeman
    Pages: 37-78

    Title: Design Patterns
    Author(s): Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
    Pages: 293-299

Example Info:
    The example showing the Observer pattern uses a system familiar to all, a
    library. When a book is checked out, the library then creates a wait list.
    Anyone that would like to checkout the book is added to the list. Then once
    the book changes status, all* of the patrons on the list are notified.

    *This is slightly different than normal libraries. This list isn't FIFO
    like most libraries. This example was modified for pedagogical purposes;
    simpler is easier to understand.

"""

import sys


class Patron(object):
    """
    Class representing a patron of the library. Each patron has a name as well
    as a method to contact them.

    """

    def __init__(self, name):
        self.name = name

    def phone_call(self, message):
        print message


class Book(object):
    """
    Class representing a book that is at the library. The book is responsible
    for knowing who has checked it out and who is waiting for it. (Similar to
        how each book record in the database would managed.)

    """

    def __init__(self, title):
        self.title = title
        self.checked_out_by = None
        self.wait_list = []


class Library(object):
    """
    Class representing a library. It has methods for checking out a book and
    returning one.

    Note:
        It is a strange library in a way. Rather than hold the book for the
        first person on the waitlist, it just broadcasts a message to everyone
        on the waitlist and the first person to check it out gets the book.

    """

    def __init__(self):
        pass

    def checkout_book(self, patron, book):
        if book.checked_out_by is not None:
            print 'Sorry,', patron.name + '.'
            print 'The book', book.title, 'is already checked out.'
            print 'We will add you to the wait list.'
            book.wait_list.append(patron)

            return

        if patron in book.wait_list:
            book.wait_list.remove(patron)

        print patron.name, 'you have successfully checked out', book.title
        book.checked_out_by = patron

    def return_book(self, book):
        book.checked_out_by = None

        message = 'The book ' + book.title + ' has been returned.'

        for patron in book.wait_list:
            prefix = 'Hello, ' + patron.name + '. '
            patron.phone_call(prefix + message)


def main(args):
    library = Library()

    bobby = Patron('Bobby Tables')
    billy = Patron('Billy')
    isaac = Patron('Isaac')

    dune = Book('Dune')

    library.checkout_book(bobby, dune)
    library.checkout_book(billy, dune)
    library.checkout_book(isaac, dune)

    library.return_book(dune)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
