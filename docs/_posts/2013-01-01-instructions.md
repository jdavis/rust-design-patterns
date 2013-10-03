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

[what]: /rust-design-patterns/what/
