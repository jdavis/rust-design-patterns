---
layout: default
title: How do you use a Design Pattern?
category: info
description: Explanation of how to appropriately apply a Design Pattern.
---

{{ page.title }}
================

First it is very important to understand [what a design pattern is][what].

After understanding what it is and why you would want to use a design pattern,
the steps can be summarized as below:

1. Identity the Problem
2. Find a Design Pattern
3. Understand the Design Pattern
4. Look at the Example
5. Fit the Pattern
6. Implement the Pattern

## Identity the Problem

When you are designing software, it is important to look at the trade-offs and
shortcomings whenever you make a decision about the structure of your code.

A few examples of this could be the following:

1. If I were to use inheritance here to solve X problem, what side effects would
   it have when this code needs to be extended for Y?
2. If I split up the classes in this way, it will solve X. It will make it
   easier to understand but then I introduce the problem Y.

Out of the six steps, this might be the most difficult one to master. It
requires the ability to examine decisions and being able to see the trade-offs
when designing software.

## Find a Design Pattern

If the problem has been accurately understood, the next thing to do is to find a
Design Pattern that will either solve the problem or lessen the impact of it.

This requires knowing some design patterns or at least knowing the categories
that they fall in. When you know that the problem you are solving deals with
object instances and instantiating them effectively, it would help to look at
Creational design patterns.

## Understand the Design Pattern

Once you've selected the design pattern that will help you. It is well worth
your time to understand it fully.

Each design pattern on this site has eight parts:

1. A definition
2. List of alternative names (if any)
3. A diagram showing a [UML][uml] representation of the pattern
4. A common problem the pattern solves
5. A wrong solution
6. A correct solution using the pattern
7. Consequences of using the pattern
8. Example code

After understanding it, if it doesn't actually solve your problem, you may have
to go to the previous step of finding one that might solve it.

## Look at the Example

The example will provide a self contained use case of the pattern in action. It
will show how to structure the classes/interfaces and it will show the
functions/methods that will need to interact together.

The example can be also used as a template for what you wish to do. The next
step will look what might happen if your problem requires a lot more effort to
solve. You may wish to just use it as a reference and make further
modifications based on your specific use case.


## Fit the Pattern

The problem that you have might not fit the given problem exactly. For whatever
the reason may be, it may be required to make certain changes to either your
structure or to the design pattern.

It may be the case that you are already using another design pattern as well.
You may have to make them work together and do other things to improve the
design of your software.

## Implement the Pattern

The implementation of a design pattern will vary greatly depending on the
language, package layout, and other factors of the software environment.

However, the core idea does not change. An example of this would be implementing
the [Observer pattern][observer] in Rust as compared to Java.

In Java, you could use polymorphism or an interface when creating your observer
pattern.

In Rust, this changes a bit. Rust doesn't have inheritance or polymorphism. It
does have traits which is very similar to an interface. A Rust programmer
wouldn't be able to use polymorphism in this case.

## Final Thoughts

By using a design pattern, the quality of your code and software can be greatly
increased. It's important to realize the benefit that they can provide and what
problems they may solve.

[what]: /rust-design-patterns/what/
[observer]: /rust-design-patterns/observer/
[uml]: http://en.wikipedia.org/wiki/Unified_Modeling_Language
