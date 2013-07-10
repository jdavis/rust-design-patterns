---
layout: default
title: Abstract Factory
category: creational
description: Abstract factory design pattern in the Rust programming language with example.
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

<div class="gallery medium">
    <a href="{{ site.url }}/img/abstract-factory-example.png" rel="lightbox" title="Example of the Abstract Factory Design Pattern.">
        <img src="{{ site.url }}/img/abstract-factory-example.png" width="620">
        <span>Example of the Abstract Factory Design Pattern.</span>
    </a>
</div>

### Example Code

View [abstract_factory.rs][github] on GitHub

{% highlight rust %}

/*
 * Abstract Factory Design Pattern
 * http://joshldavis.com/rust-design-patterns/abstract-factory/
 */

/*
 * Core Trait that defines a Phone
 */
trait Phone {
    fn call(&self);
}

/*
 * Core Trait that defines a Tablet
 */
trait Tablet {
    fn play_games(&self);
}

/*
 * Core Trait that defines a Factory
 */
trait Factory<P: Phone, T: Tablet> {
    fn new_phone(&self) -> P;
    fn new_tablet(&self) -> T;
}


/*
 * Define our Apple products. Normally these structs would contain a lot more
 * data.
 */
struct iPhone;

impl Phone for iPhone {
    fn call(&self) {
        println("Look! I'm calling on an iPhone!");
    }
}

struct iPad;

impl Tablet for iPad {
    fn play_games(&self) {
        println("Just playing some games on my iPad.");
    }
}

/*
 * Create AppleFactory and implement it for our Apple devices
 */
struct AppleFactory;

impl Factory<iPhone, iPad> for AppleFactory {
    fn new_phone(&self) -> iPhone {
        return iPhone;
    }

    fn new_tablet(&self) -> iPad {
        return iPad;
    }
}

/*
 * Define our Google products. Like with Apple's products, these are
 * simplified.
 */

struct Nexus4;

impl Phone for Nexus4 {
    fn call(&self) {
        println("Look! I'm calling on a Nexus 4!");
    }
}

struct Nexus10;

impl Tablet for Nexus10 {
    fn play_games(&self) {
        println("Just playing some games on my Nexus 10.");
    }
}

/*
 * Create GoogleFactory and implement it for our Google devices
 */
struct GoogleFactory;

impl Factory<Nexus4, Nexus10> for GoogleFactory {
    fn new_phone(&self) -> Nexus4 {
        return Nexus4;
    }

    fn new_tablet(&self) -> Nexus10 {
        return Nexus10;
    }
}


fn main() {
    // Create our two different factories
    let apple = AppleFactory;
    let google = GoogleFactory;

    // Both factories use the same interface, so let's just use them

    // Test out creating phones
    let phone = apple.new_phone();
    phone.call();

    let phone = google.new_phone();
    phone.call();

    // Test out creating tablets
    let tablet = apple.new_tablet();
    tablet.play_games();

    let tablet = google.new_tablet();
    tablet.play_games();
}

{% endhighlight %}

[github]: https://github.com/jdavis/rust-design-patterns/blob/master/patterns/abstract_factory.rs
