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
7. Consequences
8. Example code

[what]: /rust-design-patterns/what/
[uml]: http://en.wikipedia.org/wiki/Unified_Modeling_Language
