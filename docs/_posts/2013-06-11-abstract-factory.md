---
layout: default
title: Abstract Factory
category: creational
css:
    - /css/code.css
    - /lib/lightbox/css/lightbox.css
js:
    - //ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js
    - /lib/lightbox/js/lightbox.js
---

{{ page.title }}
================

Also Known As: **Kit**

## Definition

Provide an interface for creating families of related or dependent objects
without specifying their concrete classes.

## Diagram

<div class="gallery medium">
    <a href="{{ site.url }}/img/abstract-factory-structure.png" rel="lightbox" title="Structure of the Abstract Factory Pattern">
        <img src="{{ site.url }}/img/abstract-factory-structure.png" width="620">
        <span>Structure of the Abstract Factory Pattern</span>
    </a>
</div>

## Problem

There are times when one is programming on a project and there are a group of
objects that have something in common. Sometimes the project will also have a
set of these groups and need to use them interchangeably.

The problem is when we want to use these groups of objects interchangeably yet
creating the objects becomes a hassle.

## Wrong Solution

One way to handle this is to just make multiple `if` statements in the code for
when objects are created. If the system is in this state, create this object of
group A, if the system is in this state, create this object of group B and so
on.

## Correct Solution

The right way to take care of this is to use the Abstract Factory pattern.
Instead of making giant `if` statements, we want to program to an interface
instead and use the power of object-oriented programming.

## Example

Apple and Google both make tablets and phones. Each company has a different way
of creating their products and obviously have different factories where they
create them.

The thing is that a website that sells Apple and Google devices doesn't care
about how the factory makes the products. Instead it cares about how to ask the
factory for a phone/tablet when it needs to. All it cares about is that each
factory works the same way. In programmer terminology, each factory has the same
*interface*.

### Example Diagram
TODO

### Example Code

View [abstract_factory.rs][github] on GitHub

{% highlight rust %}


{% endhighlight %}

[github]: https://github.com/jdavis/rust-design-patterns/blob/master/patterns/abstract_factory.rs
