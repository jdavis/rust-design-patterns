# In the process of being converted from Python to Rust

Design Patterns in Rust
=========================

Implementation of various design patterns in a new and the new and exciting
language called [Rust][rust].

These are supposed to be simple examples to not only illustrate the design
pattern, but to make it easier to remember.

Using
-----

To learn about a given pattern, open up the source code. All of the patterns are
defined in the [patterns][patterns] directory.

To run a given pattern, just run it like this:

```bash

# Be in the repository
cd design-patterns/

# Run the Adapter pattern
rust run patterns/adapter.rs

```

Be sure to take a look at the [list of patterns][list].

Also included is the complete list of [Design Principles][principles] listed in
the book, [Head First Design Patterns][hfdp], from order of introduction. It is
a great resource that reminds one on some very important principles when it
comes to software design.


Learning
--------

All of the patterns can be found in the [patterns][patterns] directory.

To learn about a given pattern, just navigate to the [documentation][docs] page for the
design patterns.

Each design pattern will have:

1. A definition
2. List of alternative names
3. A common problem the pattern solves
4. A wrong solution
5. The correct solution using the pattern
6. Sources used for the pattern for continued reading

List of Patterns
----------------

* [Adapter](patterns/adapter.rs)

Sources
-------
 1. **Title**: Head First Design Patterns

    **Author(s)**: Eric Freeman & Elisabeth Freeman

    **Link(s)**: [Site][hfdp], [Amazon][hfdpa]


 2. **Title**: Design Patterns: Elements of Reusable Object-Oriented Software

    **Author(s)**: Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides

    **Link(s)**: [Wikipedia][GoFW], [Amazon][GoFA]

[rust]: http://www.rust-lang.org/
[documentation]: http://joshldavis.com/design-patterns/
[GoFA]: http://amzn.com/0201633612
[GoFW]: http://en.wikipedia.org/wiki/Design_Patterns
[list]: https://github.com/jdavis/design-patterns#list-of-patterns
[hfdp]: http://www.headfirstlabs.com/books/hfdp/
[hfdpa]: http://amzn.com/0596007124
[patterns]: patterns/
[principles]: PRINCIPLES.md
