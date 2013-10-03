---
layout: default
title: What is a Design Pattern?
category: info
description: Explanation of what a Design Pattern actually is.
---

{{ page.title }}
================

A design pattern is a way to organize and structure software. While the idea
isn't quite intuitive unless you have a basic understanding of building
software, let's look at it from a neutral perspective using an analogy.

## Cathedral Analogy

Imagine you live in the 12th century and are appointed to lead the construction
of a cathedral. Your name may or may not be [Tom Builder][pillars].

This might seem like a daunting task if you don't have much experience with
building cathedrals. To give you a foundation (ha, pun) so that you can start
designing it, you want to study other famous cathedrals.

As you view more and more cathedrals and talk to various other cathedral
builders, you start to notice certain "patterns" among the great structures. For
example, you may notice that certain vaulting requires more robust support. You
might notice that certain materials work better for certain parts of the
cathedral because it is lighter or possibly sturdier than others.

In order to help future cathedral builders, you want to compile all that you've
learned into a single volume to help other builders. You want the information
to be as general as possible such that it can help the most number of people as
they design and build.

This is exactly what a design pattern is. The fact that it has to do with
architecture instead of software engineering doesn't matter. The goal of a
design pattern is always to provide a common solution to a certain problem when
designing something.

## Software as the Cathedral

This isn't the first time that software has been likened to building a
cathedral; Eric S.  Raymond also used the comparison for open source software in
his seminal essay, [The Cathedral and the Bazaar][esr].

The idea is still the same; when designing software there are times when
programming it a certain way will bring far more benefits than the easier
approach or vice versa.

The hard part is understanding the benefits and shortcomings of various design
patterns and recognizing when to use them.

## Why would you use/not use a Design Pattern?

A design pattern can improve various aspects of software engineering. Whether it
has to do with the immediate improvement of speed to develop, or the future of
the code base in ways you might not expect.

When a design pattern isn't appropriately selected, it can have negative side
effects on software development. It's important to choose design patterns based
on the problem they are trying to solve.

Here are a few important measurements that design patterns can greatly change.

### Development Speed

A design pattern can hinder the speed of development if a sophisticated design
isn't needed.

Conversely, using a known design pattern can speed up development because it
alleviates the hassle of having to think about how all your classes will
interact and work together.

### Readability

Readability in programming is a measurement of how easy it is to look at a piece
(however big) of code and understand what it is doing.

By taking software and changing it so that it fits well-known problems, it gives
people that aren't familiar with your code base (new developers, managers,
maintainers, etc.) an easier starting point and an easier time when trying to
understand the code.

Sometimes one of the hardest parts about understanding a code base is just
understanding why things are arranged the way they are. The more you can do to
put things in a logical and well-thought out manner, the less a person reading
the code will have to do to understand it. Design patterns give a tried and tested
format as guidelines for doing this.

### Maintainability

Another measurement that is closely tied to readability, is a way of looking at
how easy it is to add features and fix bugs in an existing project or code base.

While all programmers are wishful thinkers in that we hope to write code that
will solve the problem once and never be modified, that is rarely the case.

There are various design patterns (such as the [Strategy][strategy])

### Simplicity

There is no denying that a simple approach can sometimes be the best for the
given project. By using a design pattern, you risk adding more classes and
obfuscating the code.

[strategy]: /
[pillars]: http://en.wikipedia.org/wiki/The_Pillars_of_the_Earth
[esr]: http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/
