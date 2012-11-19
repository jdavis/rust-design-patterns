Design Patterns in Python
=========================

Implementation of various design patterns in everyone's favorite language,
Python.

These are supposed to be simple examples to not only illustrate the design
pattern, but to make it easier to remember.

How to Use
----------

To learn about a given pattern, open up the source code. All of the patterns are
defined in the [patterns][patterns] module.

To run a given pattern, just run it like this:

```bash

# Be in the repository
cd design-patterns/

# Run the Observer pattern
python -m patterns.observer

```

Be sure to take a look at the [list of patterns][list].

Also included is the complete list of [Design Principles][principles] listed in
the book, [Head First Design Patterns][hfdp], from order of introduction. It is
a great resource that reminds one on some very important principles when it
comes to software design.


Pattern Format
--------------

All of the patterns can be found in the [patterns][patterns] module.

To learn about a given pattern, just open up the file. Each pattern is self
contained and contains the following:

1. A definition
2. List of alternative names
3. A common problem the pattern solves
4. A wrong solution
5. The correct solution using the pattern
6. Sources used for the pattern for continued reading

List of Patterns
----------------

* [Decorator](https://github.com/jdavis/design-patterns/blob/master/patterns/decorator.py)
* [Observer](https://github.com/jdavis/design-patterns/blob/master/patterns/observer.py)
* [Strategy](https://github.com/jdavis/design-patterns/blob/master/patterns/strategy.py)

Sources
-------
 1. **Title**: Head First Design Patterns
 
    **Author(s)**: Eric Freeman & Elisabeth Freeman
    
    **Link(s)**: [Site][hfdp], [Amazon][hfdpa]  
  

 2. **Title**: Design Patterns
 
    **Author(s)**: Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides
    
    **Link(s)**: [Wikipedia][GoFW], [Amazon][GoFA]

[GoFA]: http://amzn.com/0201633612
[GoFW]: http://en.wikipedia.org/wiki/Design_Patterns
[list]: https://github.com/jdavis/design-patterns#list-of-patterns
[hfdp]: http://www.headfirstlabs.com/books/hfdp/
[hfdpa]: http://amzn.com/0596007124
[patterns]: https://github.com/jdavis/design-patterns/blob/master/patterns/
[principles]: https://github.com/jdavis/design-patterns/blob/master/PRINCIPLES.md
